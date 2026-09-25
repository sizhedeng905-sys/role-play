"""Generate Chinese year and theme indexes from catalog/papers.jsonl."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "papers.jsonl"
YEAR_DIR = ROOT / "literature" / "by-year"
THEME_DIR = ROOT / "literature" / "by-theme"
THEMES = {
    "persona-dialogue": ("角色对话、语料与风格", "历史起点、台词模仿、角色语料与微调。"),
    "psychology-decisions": ("目标、心理与场景决策", "内心状态、价值观、信念与具体行动选择。"),
    "ability-boundaries": ("知识与能力边界", "区别角色不知道的事实、做不到的技能、笨拙的社交反应与求助。"),
    "agent-memory": ("Agent、记忆与世界状态", "关系、情节记忆、可执行动作、动态环境与长期变化。"),
    "interventions": ("提示以外的干预途径", "行为规则、检索约束、表示编辑、steering、偏好优化与强化学习。"),
    "evaluation": ("评测方法", "未见场景、多轮轨迹、匿名角色、人评与 LLM 裁判。"),
}


def anchor(row: dict) -> str:
    return "paper-" + re.sub(r"[^a-z0-9]+", "-", row["id"].lower()).strip("-")


def status(row: dict) -> str:
    state = row.get("download_status", "pending")
    if state == "downloaded":
        return f"本地 PDF：`{row['local_path']}`；SHA-256：`{row['sha256']}`"
    return f"原文状态：**{state}**" + (f"（{row['download_error']}）" if row.get("download_error") else "")


def render_year(year: int, rows: list[dict]) -> None:
    lines = [f"# {year} 年首次公开的相关论文", "", "按首次可核实公开年份归类。正式会议或期刊年份可能不同。标题、作者和版本以各条原始发布页为准。", ""]
    if not rows:
        lines += ["本次检索未纳入该年**首次公开**的论文；在此年正式发表的论文可能已归入其预印本首发年份。", ""]
    for row in sorted(rows, key=lambda r: (r["first_public_date"], r["title"].casefold())):
        lines += [f'<a id="{anchor(row)}"></a>', f"## [{row['title']}]({row['source_url']})", "",
                  f"- **作者**：{', '.join(row['authors']) if isinstance(row.get('authors'), list) else row.get('authors', '')}",
                  f"- **时间**：首次公开 {row['first_public_date']}；正式发表 {row.get('publication_date') or '未核实 / 暂无'}；{row.get('venue') or '未核实'}",
                  f"- **标识**：{row['id']}" + (f"；arXiv {row['arxiv_id']}" if row.get("arxiv_id") else "") + (f"；DOI {row['doi']}" if row.get("doi") else ""),
                  f"- **线索**：{', '.join(THEMES[t][0] for t in row['themes'])}",
                  f"- **关联程度**：{row.get('relevance', '未标注')}",
                  f"- **原文**：[PDF]({row['pdf_url']})" if row.get("pdf_url") else "- **原文**：未找到合法开放 PDF",
                  f"- **本地**：{status(row)}", ""]
        if row.get("abstract_summary"):
            lines += [f"**内容提要**（来源页摘要层级）：{row['abstract_summary']}", ""]
        if row.get("verification_notes"):
            lines += [f"**版本核对**：{row['verification_notes']}", ""]
        other_links = [link for link in row.get("source_links", []) if link != row["source_url"]]
        if other_links:
            lines += ["**其他合法版本**：" + "；".join(f"[链接 {i+1}]({link})" for i, link in enumerate(other_links)), ""]
    (YEAR_DIR / f"{year}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def render_theme(theme: str, rows: list[dict]) -> None:
    title, explanation = THEMES[theme]
    lines = [f"# {title}", "", explanation, "", "同一论文只有一条书目记录及一份本地 PDF；这里链接到其首次公开年份索引。", ""]
    for row in sorted(rows, key=lambda r: (r["year"], r["first_public_date"], r["title"].casefold())):
        link = f"../by-year/{row['year']}.md#{anchor(row)}"
        lines += [f"- **{row['year']}** [{row['title']}]({link}) · {row['id']} · {row.get('download_status', 'pending')}"]
    (THEME_DIR / f"{theme}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line.strip()]
    years: dict[int, list[dict]] = defaultdict(list)
    themes: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        years[int(row["year"])].append(row)
        for theme in row["themes"]:
            if theme not in THEMES:
                raise ValueError(f"Unknown theme: {theme}")
            themes[theme].append(row)
    YEAR_DIR.mkdir(parents=True, exist_ok=True)
    THEME_DIR.mkdir(parents=True, exist_ok=True)
    for year in range(2018, 2027):
        render_year(year, years.get(year, []))
    for theme in THEMES:
        render_theme(theme, themes.get(theme, []))
    print(json.dumps({"papers": len(rows), "by_year": dict(sorted(Counter(r["year"] for r in rows).items())),
                      "by_theme": {key: len(themes.get(key, [])) for key in THEMES}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
