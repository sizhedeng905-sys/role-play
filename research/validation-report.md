# 文献库核验报告

核验日期：2026-09-25。统计单位为**去重后的论文**，年份按首次可核实公开日期。主题可多选，主题数量之和不等于论文总数。

| 指标 | 结果 |
| --- | ---: |
| 用户起始入口 | 51 个；RoleLLM 的 arXiv 与 ACL 入口合并，计 50 篇 |
| 纳入论文 | 87 篇 |
| 成功下载并通过本机文件头、大小及 SHA-256 核验 | 86 篇 |
| 无法获取合法开放 PDF | 1 篇 |
| 下载后仍失败或校验冲突 | 0 篇 |
| 本地 PDF 标题页自动匹配 | 83 篇达到阈值，3 篇另行复核 |

分年：2018 年 3 篇，2019 年 1 篇，2020 年 2 篇，2021 年 0 篇，2022 年 4 篇，2023 年 10 篇，2024 年 24 篇，2025 年 22 篇，2026 年 21 篇。

分主题：角色对话、语料与风格 28 篇；目标、心理与场景决策 49 篇；知识与能力边界 23 篇；Agent、记忆与世界状态 40 篇；提示以外的干预途径 32 篇；评测方法 67 篇。

唯一无法下载项是 [Act-LLM](https://www.sciencedirect.com/science/article/pii/S0957417425026417)。已核实的公开 SSRN PDF 地址在本机返回 HTTP 403；目录记为 `unavailable`，没有将摘要页当作原文。重试或查找合法作者稿时，以 [目录记录](../catalog/papers.jsonl) 的 `pdf_url`、`download_error` 和最新状态为准。

本次本地执行并通过：

```powershell
python -m compileall -q scripts
python scripts/build_catalog.py --dry-run
python scripts/verify_papers.py
python scripts/build_indexes.py
```

`verify_papers.py` 返回 `included=87`、`verified_downloads=86`、`unavailable=1`、`failed=[]`；本地恰有 86 个 `.pdf`，无 `.part` 残留。标题页报告见 [自动抽查](pdf-title-page-check.md)及[三项复核](pdf-title-page-manual-review.md)。自动抽取核对的是第一页标题词，不表示逐篇人工核实正文实验。

起始集的 ACL、arXiv、PMLR、ICLR 标识已逐一与目录的主标识及版本链接核对；未发现遗漏、重复论文 ID、重复 PDF SHA-256、未来日期或缺失哈希。`MORTISE` 的撤回状态及 `Character is Destiny` 的书目页/PDF 标题差异见[检索日志](../search-log.md)。
