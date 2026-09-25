# 检索、筛选与核验日志

**执行日期：2026-09-25（Asia/Shanghai）**。使用英文和中文检索词搜索截至当天已公开的论文；本次纳入的 87 篇均为英文论文。文献首次公开年份范围为 2018–2026；更早文献仅作必要背景，没有为了凑数量纳入。此库是目标导向的检索与引用扩展，**不声称穷尽全部论文**。

## 检索入口和实用词组

实际使用网页搜索定位候选，然后逐条回到 ACL Anthology、arXiv、PMLR、OpenReview、ICLR、AAAI、COLM、TMLR、ACM/作者公开页核实作者、题名、日期、版本与 PDF。直接按用户提供的 ACL / arXiv / PMLR / ICLR 编号打开起始集，共 51 个入口；其中 RoleLLM 预印本和会议版是一篇，合并为 50 条。按标题再搜预印本与正式版，避免把会议年份误作首次公开年份。

| 阶段 | 实际检索词示例（各词组独立或组合） | 处理结果 |
| --- | --- | --- |
| 起始集核验 | 用户列出的 51 个原始入口；`<paper title> arxiv ACL proceedings PDF`、`RoleLLM 2310.00746 2024.findings-acl.878`、`Character is Destiny 2404.12138 2025.findings-emnlp.813` | 检查正式页、预印本 v1、作者表、发表月份、DOI 与开放 PDF；合并跨年版本。全部起始入口可识别。 |
| 第一轮主题扩展 | `persona dialogue fictional character fine tuning`、`character action decision belief goal role playing`、`fictional character knowledge boundary timeline skill limit`、`role playing memory world state action`、`role-playing social emotion benchmark`、`角色扮演 知识边界 能力边界 社交能力 行动 决策`、`虚构角色 场景 行动 目标 动机` | 找到角色行动层 [STSS](https://aclanthology.org/2024.findings-acl.526/)、场景技能 [DMT-RoleBench](https://ojs.aaai.org/index.php/AAAI/article/view/34768)、动态社会评测 [AgentSense](https://aclanthology.org/2025.naacl-long.257/) 等，并对主题相邻工作作纳排。 |
| 第二轮引文扩展 | 阅读 [TimeChara](https://aclanthology.org/2024.findings-acl.197/)、[RoleMRC](https://aclanthology.org/2025.findings-acl.1082/)、[CharacterBox](https://aclanthology.org/2025.naacl-long.323/)、[Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591/)、[CDT](https://aclanthology.org/2026.acl-long.568/) 的相关工作或参考文献；用 `RoleEval`、`MORTISE`、`WikiRole`、`boundary-aware learning`、`DMT-RoleBench professional skill`、`role playing finite state machine` 回查原始页 | 补入 Harry Potter 对话情节数据、RoleKE-Bench、Roleplay-doh、Codified Finite-state Machines、BOOKMARKS 等；将 2025/2026 后续研究作为向前引用追踪。 |
| 第三轮定向查漏 | `socially awkward role play LLM`、`role-playing try fail ask for help ability`、`fictional character skill cannot role-playing`、`角色 安慰 笨拙 社交反应 大模型`、`角色扮演 匿名评测 情绪变化`、`villain role playing alignment`；限定原始出版站点再查 | 检得 [Too Good to be Bad](https://aclanthology.org/2026.findings-acl.282/) 等价值偏差工作；未发现已核实且直接定义「原作角色应有的社交笨拙/技能上限」金标准的高相关新论文，停止本支扩展。 |

更细的检索词、引文路线及分年筛选记录见 [2018–2024](research/seed-early-findings.md)、[2025](research/seed-2025-findings.md)、[2026](research/seed-2026-findings.md)。检索引擎结果仅用于发现；收录元数据必须有原始论文页支持。中文词组搜到的英文论文转述页没有代替正式来源。

## 纳入、排除与证据等级

纳入：直接研究已有原作人物扮演、角色知识与技能边界、价值/心理/行动、记忆与世界状态、干预或与这些问题直接可迁移的评测。`high`/`direct` 表示核心证据，`medium` 表示历史基线、相邻机制或综述；后者的结论仅在原论文范围内解释。论文 PDF 在合法开放来源可得时尝试下载；没有可访问 PDF 时写实际状态与原因。没有下载原作书籍、剧本、角色数据集。

排除的典型例子：[SweetieChat](https://aclanthology.org/2025.coling-main.312/) 研究通用情感支持，没定义原作角色应当不会的反应；[KnowAgent](https://aclanthology.org/2025.findings-naacl.205/) 研究通用任务规划，缺乏人物忠实性；[ESC-Eval](https://aclanthology.org/2024.emnlp-main.883/) 没有固定原作人物及能力上限；纯多智能体分工中借用 “role-playing” 的工作也不纳入。扩展检索出现大量聊天产品、博客、第三方摘要以及无原始论文的页面，均未用于目录。

## 版本纠正记录

1. **首发日期与正式日期分开。** [2021.naacl-main.64](https://aclanthology.org/2021.naacl-main.64/) 的 [arXiv 初稿](https://arxiv.org/abs/2010.00685) 公开于 2020-10-01；[CharacterBox](https://aclanthology.org/2025.naacl-long.323/) 的 [初稿](https://arxiv.org/abs/2412.05631) 是 2024-12-07；[PsyMem](https://aclanthology.org/2026.tacl-1.24/) 的 [初稿](https://arxiv.org/abs/2505.12814) 是 2025-05-19。年份索引和 PDF 路径采用首发年份。
2. **改题与作者变动。** [Character is Destiny](https://aclanthology.org/2025.findings-emnlp.813/) 的会议题名与 2024 预印本不同；[ChatAnime](https://aclanthology.org/2026.acl-long.2179/) 对应 2025 年初稿 *LLMs vs. Chinese Anime Enthusiasts*；[CharacterGLM](https://aclanthology.org/2024.emnlp-industry.107/) 正式版与 2023 年初稿的题名、作者和内容范围有差异。目录依正式版作者/标题，并保留双链接与两日期。
3. **起始集重复。** 2023 arXiv RoleLLM 与 2024 ACL RoleLLM 合并一条；[Generative Agents](https://arxiv.org/abs/2304.03442) 同时记录 ACM UIST 正式页与作者合法公开 PDF。
4. **异常须保留原始依据。** arXiv [2608.05170](https://arxiv.org/abs/2608.05170) 与 [2608.00023](https://arxiv.org/abs/2608.00023) 的版本历史日期早于编号月份；目录依页面显示的 v1 日期并在条目备注。RoleCDE 预印本与正式摘要的数据规模不一致；精读数字应以所引用 PDF 版本为准。
5. **原始页与 PDF 冲突。** [Character is Destiny](https://aclanthology.org/2025.findings-emnlp.813/) 的 ACL 书目标题是 *Can Persona-assigned Language Models Make Personal Choices?*，但正式 PDF 第一页印的是 *Can Role-Playing Language Agents Make Persona-Driven Decisions?*；书目页还将 PDF 的 `Xiaoqing Dong` 连写成 `Xiaoqingdong`。目录保留官方书目题名，并另存 PDF 首页题名与作者差异，分析引用 PDF 实际版本。
6. **撤回版本。** [MORTISE](https://arxiv.org/abs/2402.10618) 的 arXiv v2 于 2024-06-15 撤回，页面注明作者发现重大问题；普通 PDF 地址返回 404，仍可从 [arXiv v1 PDF](https://arxiv.org/pdf/2402.10618v1) 获取。其早期实验不作可靠效果证据，只保留为边界提问方法的历史线索。

## 覆盖与遗漏风险

按主题组合、预印本/正式版配对、综述参考文献、相关工作与部分后续引用做了至少两轮扩展。继续检索「技能上限、会尝试但失败、笨拙安慰」未产生可核实的直接新研究后停止。覆盖偏向 ACL、arXiv、机器学习会议与开放英文论文；中文期刊、HCI/游戏研究、未索引作者稿及闭源商业评测可能遗漏。不同角色和作品的原作授权与可读性会限制将来的人物级实验。对「现有论文尚缺直接证据」的判断只限本次检索范围。
