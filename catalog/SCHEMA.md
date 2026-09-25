# 书目字段说明

`papers.jsonl` 为一行一篇、UTF-8 编码的 JSON Lines。`seed-*.jsonl` 保留分段核验结果；运行 `python scripts/build_catalog.py` 按 DOI、arXiv ID、ACL ID 与标准化题名合并。再运行下载和索引脚本，状态、SHA-256 会写回主目录。不要把预印本与会议版各算一篇。

| 字段 | 含义 |
| --- | --- |
| `id` | 稳定主标识；优先 ACL ID，否则 arXiv ID 或其他官方标识。 |
| `title`, `authors` | 正式发表版书目标题、作者及顺序；若 PDF 首页与出版元数据冲突，保留 `pdf_title` 等差异字段并写 `verification_notes`。 |
| `first_public_date`, `year` | 能在原始发布页核实的最早公开日期及其年份；只核到月份时用 `YYYY-MM`。 |
| `publication_date`, `venue` | 正式版时间与出版场所，允许为空。 |
| `doi`, `arxiv_id`, `acl_id` | 同一工作的不同标识；允许为空。 |
| `source_url`, `source_links`, `pdf_url` | 主原始页、其他合法版本页、实际尝试下载的 PDF URL；预印本与正式版链接都保留。 |
| `themes`, `relevance` | 六个主题标签可多选；`direct`、`high` 为核心研究，`medium` 为历史对照、综述或可迁移方法。 |
| `local_path` | 相对仓库根目录的本地 PDF 路径，按首发年和主要主题归档；Git 忽略其父目录 `papers/`。 |
| `download_status` | `pending`、`downloaded`、`unavailable`、`failed` 或 `conflict`。只有 `downloaded` 表示本机实际存在且通过校验。 |
| `sha256`, `size_bytes`, `download_error`, `downloaded_at` | 下载文件摘要、大小、失败原因与 UTC 时间。再次下载会先核对已有文件。 |
| `abstract_summary`, `verification_notes` | 检索阶段的简要线索与版本/日期审计备注。`abstract_summary` 仅属摘要层级，**不能冒充全文精读**；详见 `notes/`。 |

`catalog/download-failures.jsonl` 是事件日志，可能包含后来成功重试的旧失败。最终成功或无法取得清单，应以 `papers.jsonl` 的最新 `download_status` 为准。
