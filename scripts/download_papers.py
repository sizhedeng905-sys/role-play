"""Download open paper PDFs with resume, retry, throttling, and SHA-256 checks.

Run from anywhere: python scripts/download_papers.py [--only ID] [--limit N]
The only output below 原文/ is public research PDFs, which are gitignored.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "papers.jsonl"
FAILURES = ROOT / "catalog" / "download-failures.jsonl"
MIN_BYTES = 4096
MAX_BYTES = 80 * 1024 * 1024
USER_AGENT = "RolePlayResearchLibrary/1.0 (personal academic use; contact via repository)"


def load() -> list[dict]:
    return [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line.strip()]


def save(rows: list[dict]) -> None:
    temporary = CATALOG.with_suffix(".jsonl.tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    os.replace(temporary, CATALOG)


def inspect_pdf(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ValueError("PDF header is missing")
        handle.seek(0)
        total = 0
        while block := handle.read(1024 * 1024):
            total += len(block)
            if total > MAX_BYTES:
                raise ValueError("PDF exceeds 80 MiB limit")
            digest.update(block)
    if total < MIN_BYTES:
        raise ValueError(f"PDF too small: {total} bytes")
    return total, digest.hexdigest()


def fetch(url: str, part: Path, timeout: int) -> None:
    if urllib.parse.urlparse(url).scheme != "https":
        raise ValueError("Only HTTPS PDF URLs are permitted")
    offset = part.stat().st_size if part.exists() else 0
    headers = {"User-Agent": USER_AGENT, "Accept": "application/pdf", "Accept-Encoding": "identity"}
    if offset:
        headers["Range"] = f"bytes={offset}-"
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as exc:
        if exc.code == 416 and offset:
            inspect_pdf(part)
            return
        raise
    with response:
        status = response.status
        resumed = status == 206 and offset > 0
        if resumed:
            content_range = response.headers.get("Content-Range", "")
            if not content_range.startswith(f"bytes {offset}-"):
                raise ValueError(f"Unexpected Content-Range: {content_range}")
        elif status != 200:
            raise ValueError(f"Unexpected HTTP status {status}")
        mode = "ab" if resumed else "wb"
        # HTTP 200 after a Range request means the host does not support resume.
        with part.open(mode) as output:
            while block := response.read(128 * 1024):
                output.write(block)
                if output.tell() > MAX_BYTES:
                    raise ValueError("Download exceeds 80 MiB limit")


def record_failure(row: dict, error: str) -> None:
    event = {
        "at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "id": row.get("id"), "url": row.get("pdf_url"),
        "status": row.get("download_status"), "error": error,
    }
    with FAILURES.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def process(row: dict, retries: int, timeout: int) -> str:
    url = row.get("pdf_url")
    if not url:
        row["download_status"] = "unavailable"
        row["download_error"] = row.get("download_error") or "No legal open PDF URL verified"
        return "unavailable"
    local = ROOT / row["local_path"]
    if not local.resolve().is_relative_to((ROOT / "原文").resolve()):
        raise ValueError(f"Output path escapes 原文/: {row['local_path']}")
    local.parent.mkdir(parents=True, exist_ok=True)
    if local.exists():
        try:
            size, sha = inspect_pdf(local)
            if row.get("sha256") and row["sha256"].lower() != sha:
                raise ValueError("Existing file hash differs from catalog; left untouched")
        except ValueError as exc:
            row["download_status"] = "conflict"
            row["download_error"] = str(exc)
            record_failure(row, str(exc))
            return "conflict"
        row.update(download_status="downloaded", download_error="", sha256=sha, size_bytes=size)
        return "verified-skip"
    part = local.with_suffix(local.suffix + ".part")
    last_error = ""
    for attempt in range(retries + 1):
        try:
            fetch(url, part, timeout)
            size, sha = inspect_pdf(part)
            if row.get("sha256") and row["sha256"].lower() != sha:
                raise ValueError("Downloaded hash differs from catalog")
            part.replace(local)
            row.update(download_status="downloaded", download_error="", sha256=sha,
                       size_bytes=size, downloaded_at=datetime.now(timezone.utc).isoformat(timespec="seconds"))
            return "downloaded"
        except (urllib.error.URLError, socket.timeout, TimeoutError, OSError, ValueError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                time.sleep(min(2 ** attempt * 2, 16))
    row["download_status"] = "unavailable" if any(
        f"HTTP Error {code}" in last_error for code in (403, 404, 410)
    ) else "failed"
    row["download_error"] = last_error
    record_failure(row, last_error)
    return row["download_status"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", default=[], help="stable ID, repeatable")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.8, help="seconds between papers")
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=45)
    args = parser.parse_args()
    if args.delay < 0 or args.retries < 0:
        parser.error("delay and retries must be nonnegative")
    rows = load()
    selected = [row for row in rows if (not args.only or row["id"] in args.only)
                and row.get("relevance", "direct") in ("direct", "high", "medium")]
    if args.limit:
        selected = selected[:args.limit]
    for index, row in enumerate(selected, 1):
        outcome = process(row, args.retries, args.timeout)
        save(rows)
        print(f"[{index}/{len(selected)}] {row['id']}: {outcome}", flush=True)
        if index < len(selected):
            time.sleep(args.delay)
    counts = {status: sum(row.get("download_status") == status for row in rows)
              for status in ("downloaded", "unavailable", "failed", "conflict", "pending")}
    print(json.dumps(counts, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
