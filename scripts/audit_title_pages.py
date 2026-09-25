"""Check a spread of downloaded PDF title pages with optional pypdf.

Use .venv/Scripts/python on Windows after installing requirements-qa.txt.
Only bibliographic matches, never PDF body text, are written to the report.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "papers.jsonl"
REPORT = ROOT / "research" / "pdf-title-page-check.md"


def words(value: str) -> set[str]:
    value = unicodedata.normalize("NFKD", value).casefold()
    return {word for word in re.findall(r"[a-z0-9]+", value) if len(word) > 2}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", default=[], help="stable paper ID, repeatable")
    args = parser.parse_args()
    records = [json.loads(s) for s in CATALOG.read_text(encoding="utf-8").splitlines() if s.strip()]
    selected = [r for r in records if r["id"] in args.only] if args.only else [
        r for r in records if r.get("download_status") == "downloaded"
    ]
    lines = ["# PDF 标题页抽查", "", "使用 `pypdf` 解析**本地 PDF 第一页**，核对目录标题的非短词是否出现；此自动结果须结合低分项人工复核。报告不收录论文正文。", "",
             "| ID | 首次公开年 | 页数 | 标题词覆盖率 | 结果 |", "| --- | ---: | ---: | ---: | --- |"]
    issues = 0
    for record in selected:
        if record.get("download_status") != "downloaded":
            continue
        reader = PdfReader(str(ROOT / record["local_path"]))
        # Keep the comparison near the title block; abstract/body words can
        # otherwise hide a genuinely different title printed on the PDF.
        first_page = (reader.pages[0].extract_text() or "")[:900]
        title_words = words(record["title"])
        ratio = len(title_words & words(first_page)) / max(len(title_words), 1)
        result = "一致" if ratio >= 0.75 else "待人工复核"
        issues += result != "一致"
        lines.append(f"| `{record['id']}` | {record['year']} | {len(reader.pages)} | {ratio:.0%} | {result} |")
        print(f"{record['id']}: {len(reader.pages)} pages, title-word coverage {ratio:.0%}, {result}")
    lines += ["", f"抽查 {len(selected)} 条；自动待复核 {issues} 条。此检查仅确认标题页与目录大体一致，不能替代全文质量或书目版本人工核查。", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
