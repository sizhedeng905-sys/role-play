# PDF 标题页人工复核

2026-09-25 对 [自动报告](pdf-title-page-check.md) 的 3 个低覆盖率条目，直接查看了**本地 PDF 第一页提取的标题和作者区**。其余 83 篇达到自动标题词匹配阈值；自动匹配不代表逐篇人工通读。

| ID | 原因 | 复核结果 |
| --- | --- | --- |
| `2025.findings-emnlp.813` | ACL 书目页题名和下载的正式 PDF 首页**确实不同**，不是抽取错误。 | ACL 页面：*Character is Destiny: Can Persona-assigned Language Models Make Personal Choices?*；PDF 首页：*Character is Destiny: Can Role-Playing Language Agents Make Persona-Driven Decisions?*。PDF 首页作者为 `Xiaoqing Dong`，书目页写 `Xiaoqingdong`。目录保留官方书目题名，另存 `pdf_title` 与 `pdf_author_variant`；精读笔记明确版本。 |
| `arxiv-2602.15669` | PDF 抽取器把大写题名中的空格压缩，出现 `ANDCOMPOSITIONAL` 等连写。 | 第一页标题实际词序与目录 `PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra` 一致；作者区可读。 |
| `arxiv-2606.25632` | PDF 抽取器把大写标题多处词组连写。 | 第一页标题实际词序与目录 `Staying In Character: Perspective-Bounded Memory For Book-Based Role-Playing Agents` 一致；作者区可读。 |

这项复核验证的是标题页与书目关联，不能据此断言正文排版、实验或所有版本元数据无误。全部 86 个本地 PDF 的文件头、大小和 SHA-256 已由 `scripts/verify_papers.py` 独立核验。
