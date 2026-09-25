"""Independently verify every downloaded PDF against catalog SHA-256 and size."""

from __future__ import annotations

import json
from pathlib import Path

from download_papers import CATALOG, ROOT, inspect_pdf


def main() -> None:
    rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line.strip()]
    bad = []
    good = 0
    known = {"downloaded", "unavailable", "failed", "conflict", "pending"}
    for row in rows:
        if row.get("download_status") != "downloaded":
            continue
        path = ROOT / row["local_path"]
        try:
            size, sha = inspect_pdf(path)
            if size != row.get("size_bytes") or sha != row.get("sha256"):
                raise ValueError("Catalog size or SHA-256 mismatch")
            good += 1
        except (OSError, ValueError) as exc:
            bad.append({"id": row["id"], "error": str(exc)})
    unresolved = [
        {"id": row["id"], "status": row.get("download_status")}
        for row in rows if row.get("download_status") not in ("downloaded", "unavailable")
    ]
    statuses = {status: sum(row.get("download_status") == status for row in rows)
                for status in sorted(known)}
    print(json.dumps({"included": len(rows), "verified_downloads": good,
                      "unavailable": sum(row.get("download_status") == "unavailable" for row in rows),
                      "statuses": statuses, "failed": bad, "unresolved": unresolved},
                     ensure_ascii=False, indent=2))
    if bad or unresolved:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
