# Role Play：原作人物扮演研究文献库

本仓库使用英文和中文检索词，整理截至 **2026-09-25** 已公开、与大型语言模型扮演已有原作虚构人物相关的论文。本次纳入的 87 篇均为英文论文；中文相关工作的遗漏风险见[检索日志](search-log.md)。目标是研究角色在新情境中的**可知事实、技能与社交能力边界、价值与动机、关系和情绪变化、行动选择**，并区分原作明示设定与研究推断。目前只有通用文献库与评测草案；尚未选择具体角色或训练模型。

## 快速导航

| 内容 | 位置 |
| --- | --- |
| 机器可读书目、PDF 链接、路径、SHA-256 与下载状态 | [catalog/papers.jsonl](catalog/papers.jsonl) |
| 2018–2026 年中文索引 | [literature/by-year/](literature/by-year/) |
| 六条研究线索中文索引 | [literature/by-theme/](literature/by-theme/) |
| 重点论文全文精读笔记 | [notes/](notes/) |
| 路线比较、评测草案、未解问题 | [research/architecture-options.md](research/architecture-options.md)、[research/evaluation-design.md](research/evaluation-design.md)、[research/open-questions.md](research/open-questions.md) |
| 检索词、筛选与版本修正 | [search-log.md](search-log.md) |
| 本次下载与完整性核验结果 | [research/validation-report.md](research/validation-report.md) |
| 下载、核验、索引维护脚本 | [scripts/](scripts/) |

年份按**首次可核实公开日期**，正式发表日期另列。因此某篇 2026 年正式论文可能出现在 2025 年索引。预印本和正式版合并一条书目，保留两个来源链接；优先保存正式 PDF。论文跨线索只存一份 PDF，通过 `themes` 多标签交叉引用。`relevance=medium` 表示历史起点、综述或方法对照，效果外推需格外谨慎。

## 研究线索

- [角色对话、语料与风格](literature/by-theme/persona-dialogue.md)
- [目标、心理与场景决策](literature/by-theme/psychology-decisions.md)
- [知识与能力边界](literature/by-theme/ability-boundaries.md)：分别看「不知道」「不会做」「想做但做不好」「该求助」
- [Agent、记忆与世界状态](literature/by-theme/agent-memory.md)
- [提示以外的干预途径](literature/by-theme/interventions.md)
- [评测方法](literature/by-theme/evaluation.md)

## 本地使用

要求 Python 3.10+。下载、SHA-256 核验和索引脚本只使用标准库；标题页抽查可选装 `pypdf`。从仓库根目录运行：

```powershell
python scripts/build_catalog.py
python scripts/download_papers.py --delay 0.8 --retries 3
python scripts/verify_papers.py
python scripts/build_indexes.py
```

`download_papers.py` 顺序下载并限速；断线后复用 `.part` 文件向支持 Range 的服务续传，对不支持 Range 的服务从头重取临时文件。已有 PDF 要通过文件头、大小和 SHA-256 检查才会跳过；发现校验冲突会保留原文件并记录 `conflict`。每篇下载状态、文件大小与 SHA-256 写入 `catalog/papers.jsonl`；失败事件追加到 `catalog/download-failures.jsonl`。可用 `--only <stable-id>` 重试一篇，或 `--limit N` 试跑。

需要抽查标题页时，可在本地虚拟环境安装唯一的 QA 依赖：

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-qa.txt
.\.venv\Scripts\python scripts/audit_title_pages.py --only 2024.findings-acl.197 --only 2025.findings-acl.1082
```

脚本从**本地 PDF 第一页**提取标题词，报告仅保存页数和匹配率，不保存论文正文。若原站 PDF 撤回、付费或拒绝访问，以目录中的实际状态和检索日志为准；摘要页不能当作已下载全文。

## 文件与版权边界

`papers/`、临时缓存和虚拟环境在 `.gitignore` 中。私有 GitHub 仓库只保存原创中文分析、代码、书目信息和链接；论文 PDF 以及任何受版权保护的原作台词、剧本、书籍全文只留本地。没有批量下载原作材料或角色数据集。

方法效果以各笔记所引原论文为限；自己的设计推断标记为「研究设想」。从文献库进入具体角色研究时，应先建立带场景与时间戳的原作证据卡，再做人物级评测。没有原作证据的特质允许写成「未知」，不能把通用高能力、高情商或反过来的笨拙预设给所有角色。
