"""Merge verified seed records into a stable, rerunnable research catalog."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "papers.jsonl"
THEMES = {
    "persona-dialogue", "psychology-decisions", "ability-boundaries",
    "agent-memory", "interventions", "evaluation",
}
ALIASES = {
    "persona": "persona-dialogue", "dialogue": "persona-dialogue",
    "psychology": "psychology-decisions", "decision": "psychology-decisions",
    "knowledge-boundary": "ability-boundaries", "ability": "ability-boundaries",
    "memory": "agent-memory", "agent": "agent-memory",
    "training": "interventions", "steering": "interventions",
    "benchmark": "evaluation", "eval": "evaluation",
}


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{number}: {exc}") from exc
    return rows


def clean_date(value: object) -> str:
    value = str(value or "").strip()
    if not value:
        return ""
    match = re.fullmatch(r"(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?", value)
    if not match:
        raise ValueError(f"Invalid ISO-like date: {value}")
    year, month, day = match.groups()
    if month and not 1 <= int(month) <= 12:
        raise ValueError(f"Invalid month in date: {value}")
    if day:
        try:
            date(int(year), int(month), int(day))
        except ValueError as exc:
            raise ValueError(f"Invalid day in date: {value}") from exc
    return year + (f"-{int(month):02d}" if month else "") + (f"-{int(day):02d}" if day else "")


def title_key(row: dict) -> str:
    return re.sub(r"[^a-z0-9]", "", str(row.get("title", "")).lower())


def identity_keys(row: dict) -> set[str]:
    result = set()
    for name in ("arxiv_id", "acl_id", "doi"):
        value = str(row.get(name) or "").strip().lower()
        if value:
            result.add(f"{name}:{value}")
    if title_key(row):
        result.add(f"title:{title_key(row)}")
    return result


def normalized_themes(value: object) -> list[str]:
    if isinstance(value, str):
        value = re.split(r"[,;|]", value)
    output = []
    for item in value or []:
        theme = ALIASES.get(str(item).strip().lower(), str(item).strip().lower())
        if theme not in THEMES:
            raise ValueError(f"Unknown theme {theme!r}; use one of {sorted(THEMES)}")
        if theme not in output:
            output.append(theme)
    return output or ["evaluation"]


def merge(a: dict, b: dict) -> dict:
    # Prefer the formally published record while retaining earliest release data.
    if not a.get("acl_id") and b.get("acl_id"):
        a, b = b, a
    for key, value in b.items():
        if key in ("themes", "source_links"):
            a[key] = list(dict.fromkeys(list(a.get(key) or []) + list(value or [])))
        elif key == "first_public_date":
            dates = [clean_date(v) for v in (a.get(key), value) if v]
            if dates:
                a[key] = min(dates)
        elif key == "authors":
            if len(value or []) > len(a.get(key) or []):
                a[key] = value
        elif not a.get(key) and value:
            a[key] = value
    return a


def slug(value: str, max_length: int) -> str:
    ascii_text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    ascii_text = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return (ascii_text[:max_length].rstrip("-") or "paper")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    seeds = sorted((ROOT / "catalog").glob("seed-*.jsonl"))
    if not seeds:
        raise SystemExit("No seed-*.jsonl files found")
    entries: list[dict] = []
    for seed in seeds:
        for row in read_jsonl(seed):
            if not row.get("title") or not row.get("source_url"):
                raise ValueError(f"{seed}: missing title/source_url: {row.get('id')}")
            row["themes"] = normalized_themes(row.get("themes"))
            row["source_links"] = list(dict.fromkeys([row["source_url"]] + list(row.get("source_links") or [])))
            matches = [i for i, old in enumerate(entries) if identity_keys(old) & identity_keys(row)]
            if matches:
                entries[matches[0]] = merge(entries[matches[0]], row)
                for index in reversed(matches[1:]):
                    entries[matches[0]] = merge(entries[matches[0]], entries.pop(index))
            else:
                entries.append(row)
    existing = read_jsonl(CATALOG)
    previous = {key: old for old in existing for key in identity_keys(old)}
    seen_paths = set()
    for row in entries:
        row["first_public_date"] = clean_date(row.get("first_public_date"))
        row["publication_date"] = clean_date(row.get("publication_date"))
        if not row["first_public_date"]:
            raise ValueError(f"Missing first public date: {row['title']}")
        row["year"] = int(row["first_public_date"][:4])
        row["id"] = row.get("acl_id") or ("arxiv-" + row["arxiv_id"] if row.get("arxiv_id") else row.get("id"))
        if not row["id"]:
            raise ValueError(f"Missing stable ID: {row['title']}")
        old = next((previous[k] for k in identity_keys(row) if k in previous), None)
        if old and old.get("local_path"):
            row["local_path"] = old["local_path"]
            for field in ("sha256", "size_bytes", "download_status", "download_error", "downloaded_at"):
                if old.get(field) is not None:
                    row[field] = old[field]
        else:
            safe_id = slug(row["id"], 48)
            short_title = slug(row["title"], 56)
            row["local_path"] = f"papers/{row['themes'][0]}/{row['year']}/{safe_id}__{short_title}.pdf"
            row.setdefault("sha256", "")
            row.setdefault("size_bytes", 0)
            row.setdefault("download_status", "pending" if row.get("pdf_url") else "unavailable")
        if row["local_path"].lower() in seen_paths:
            raise ValueError(f"Duplicate output path: {row['local_path']}")
        seen_paths.add(row["local_path"].lower())
    entries.sort(key=lambda row: (row["year"], row["first_public_date"], row["title"].casefold()))
    print(f"Merged {sum(len(read_jsonl(s)) for s in seeds)} seed rows into {len(entries)} papers")
    if not args.dry_run:
        temp = CATALOG.with_suffix(".jsonl.tmp")
        temp.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in entries), encoding="utf-8")
        temp.replace(CATALOG)


if __name__ == "__main__":
    main()
