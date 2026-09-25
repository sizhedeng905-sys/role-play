# 2026 起始集与扩展检索记录

检索截止：**2026-09-25**。本文件是 `catalog/seed-2026.jsonl` 的核验日志；年份以**首次公开**为准，正式发表时间另记。检索对象是论文，而非网页转载、技术博客或自动生成的论文摘要。

## 检索入口与词组

- 原始来源：ACL Anthology 论文页及正式 PDF、arXiv 摘要页及版本历史、ICLR 2026 正式 proceedings、Elsevier 期刊页、作者在 SSRN 公开的预印本页。2026-09-25 执行核验；使用网页检索定位候选后，回到上述原始来源核对。
- 英文词组：`role-playing agent character action decision tree`、`role-playing ability boundary skill limit`、`perspective bounded memory fictional character`、`awkward emotional support role play`、`dynamic persona social interaction benchmark`、`role playing executable state machine`、`role playing storyline memory`、`anonymous character evaluation`、`villain role playing alignment`。
- 中文词组：`角色扮演 能力边界 技能上限`、`角色 安慰 笨拙 社交反应 大模型`、`虚构人物 场景动作 状态转移`、`角色扮演 匿名评测 情绪变化`。中文词组主要用于寻找可能的中文论文；高相关结果最终仍以原始论文页核验。未发现直接实验“特定角色想安慰人但因社交技能不足而笨拙行动”的已核实论文。
- 纳入原则：角色或 persona 的知识、动机、心理、场景行动、状态变化、评测或可执行约束与研究目标有直接方法联系，且能找到原始论文页。对只研究一般情绪支持、泛化多智能体交互或纯图像游戏动作的结果，只有能够提供明确对照方法时才纳入。

## 起始集逐项核验

15 个指定入口均可解析：10 个 ACL/TACL/SIGDIAL 编号、4 个 arXiv 编号和 1 篇 ICLR PERSONA。另纳入 10 个扩展候选，目录共 25 条，其中 4 条首次公开于 2025 年。正式 ACL 文献主要发表于 2026-07；SIGDIAL 是 2026-08；TACL 的 [正式 PDF](https://aclanthology.org/2026.tacl-1.24.pdf) 载明 2026-04 发表。ACL 页只给到月份时未伪造具体日期。

| 起始入口 | 核验结果与主要价值 |
| --- | --- |
| [2026.acl-long.568](https://aclanthology.org/2026.acl-long.568/) | **Deriving Character Logic from Storyline as Codified Decision Trees**；[arXiv 2601.10080](https://arxiv.org/abs/2601.10080) 首发 2026-01-15。把故事场景与行动归纳为可执行条件树。 |
| [2026.acl-long.449](https://aclanthology.org/2026.acl-long.449/) | **ThinkPersona: Thinking with Persona Graphs for Faithful Individualized Role-Playing**；真人访谈 persona 图，不应直接当作虚构角色原作忠实性的证据。 |
| [2026.acl-long.1336](https://aclanthology.org/2026.acl-long.1336/) | **Beyond Static Persona Consistency: Dynamic Persona Coherence in LLM Role-Playing**；区分稳定身份与随经历变化的心理状态。 |
| [2026.acl-long.1491](https://aclanthology.org/2026.acl-long.1491/) | **StratMem-Bench: Evaluating Strategic Memory Use in Virtual Character Conversation Beyond Factual Recall**；[arXiv 2604.26243](https://arxiv.org/abs/2604.26243) 首发 2026-04-29。 |
| [2026.acl-long.2179](https://aclanthology.org/2026.acl-long.2179/) | **ChatAnime: Towards User-Centered Emotional Support in LLM-based Virtual Character Chat**；与 [arXiv 2508.06388](https://arxiv.org/abs/2508.06388) 同一 ChatAnime 数据与实验，首发 **2025-08-08**，按 2025 年归档。 |
| [2026.tacl-1.24](https://aclanthology.org/2026.tacl-1.24/) | **PsyMem: Fine-grained Psychological Alignment and Explicit Memory Control for Advanced Role-Playing LLMs**；[arXiv 2505.12814](https://arxiv.org/abs/2505.12814) 首发 **2025-05-19**，正式版 2026-04。 |
| [2026.findings-acl.1283](https://aclanthology.org/2026.findings-acl.1283/) | **HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing**；[arXiv 2601.21459](https://arxiv.org/abs/2601.21459) 首发 2026-01-29。 |
| [2026.findings-acl.106](https://aclanthology.org/2026.findings-acl.106/) | **RoleCDE: Benchmarking and Mitigating Role–Alignment Trade-offs in Role-Playing Agents**；[arXiv 2606.01552](https://arxiv.org/abs/2606.01552) 首发 2026-06-01，研究价值冲突中的角色决策。 |
| [2026.findings-acl.1175](https://aclanthology.org/2026.findings-acl.1175/) | **Memory-Driven Role-Playing: Evaluation and Enhancement of Persona Knowledge Utilization in LLMs**；[arXiv 2603.19313](https://arxiv.org/abs/2603.19313) 首发 2026-03-14，分阶段评测记忆的锚定、选择、边界与演绎。 |
| [2026.sigdial-1.15](https://aclanthology.org/2026.sigdial-1.15/) | **Rethinking Role-Playing Evaluation: Anonymous Benchmarking and A Systematic Study of Personality Effects**；[arXiv 2603.03915](https://arxiv.org/abs/2603.03915) 首发 2026-03-04。 |
| [arXiv 2606.25632](https://arxiv.org/abs/2606.25632) | **Staying In Character: Perspective-Bounded Memory For Book-Based Role-Playing Agents**；2026-06-24，测试角色视角内知识，不等同于技能上限。 |
| [arXiv 2608.05170](https://arxiv.org/abs/2608.05170) | **DREAM: LLM-based Dynamic Role-playing via Event-Aware Memory Graph**；页面版本历史写 2026-05-27，见下方异常说明。 |
| [arXiv 2608.00023](https://arxiv.org/abs/2608.00023) | **Role Steering of Language Models for Social Simulations**；页面版本历史写 v1 为 2026-07-09，见下方异常说明。 |
| [arXiv 2601.10122](https://arxiv.org/abs/2601.10122) | **Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends**；综述作为追踪参考文献入口，不充当方法有效性原始实验。 |
| [ICLR PERSONA](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f66ce276436c4cd151535b03841ac713-Abstract-Conference.html) | **PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra**；[arXiv 2602.15669](https://arxiv.org/abs/2602.15669) 首发 2026-02-17。Big Five 的激活向量控制不等于完整原作角色复现。 |

## 两轮扩展与引用追踪

**第一轮，按缺口扩展。** 用“角色行动、社会场景、非完美心理反应、能力边界、匿名评测”等词组搜索 ACL 2026、arXiv 和 ICLR 原始页，纳入 [AdaMARP](https://aclanthology.org/2026.findings-acl.1563/)（显式 Thought/Action/Environment/Speech 和场景管理）、[PersonaArena](https://aclanthology.org/2026.findings-acl.471/)（多轮社会情境）、[PersonaForge](https://aclanthology.org/2026.findings-acl.386/)（防御机制与长对话心理一致性）、[Too Good to be Bad](https://aclanthology.org/2026.findings-acl.282/)（反派特质保真度）、[Understanding Generalization in Role-Playing Models](https://aclanthology.org/2026.findings-acl.87/)（人物、用户和对话分布漂移）、[PALATE](https://arxiv.org/abs/2607.27816)（个体用户与角色的自由多轮交互评测）。反派论文的 [arXiv 2511.04962](https://arxiv.org/abs/2511.04962) 首发 2025-11-07。

**第二轮，顺着论文参考文献、作者论文页和新论文相关工作追踪。** [CDT 正式 PDF](https://aclanthology.org/2026.acl-long.568.pdf) 的可执行角色逻辑线索指向 [ICLR Codified Finite-state Machines](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a862f5788fd09bb6843c694d8120d50c-Abstract-Conference.html)，其 [arXiv 2602.05905](https://arxiv.org/abs/2602.05905) 首发 2026-02-05。作者公开论文列表与 arXiv 原始页指向 [BOOKMARKS](https://arxiv.org/abs/2605.14169)，首发 2026-05-13，按故事时间点维护状态、行为、概念问答。能力边界线索指向 [Act-LLM 期刊页](https://www.sciencedirect.com/science/article/pii/S0957417425026417) 与 [SSRN 作者预印本](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5230378)：预印本 2025-04-25，期刊卷期日期 2026-01-15。SSRN 声称有 33 页合法开放版本，但本机访问其 PDF 返回 HTTP 403；须将实际下载结果记为失败或不可获取，不可凭摘要标记已读全文。

从 [CFSM 正式 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a862f5788fd09bb6843c694d8120d50c-Paper-Conference.pdf)、[ChatAnime 正式 PDF](https://aclanthology.org/2026.acl-long.2179.pdf) 和 CDT 的参考文献回溯了前期角色/记忆工作；2025 年新增高相关候选已另行报告：AAAI DMT-RoleBench 的 professional skill 与 knowledge boundary 分项、ACL RoleKE-Bench 的已知/未知错误检测。继续用“笨拙社交反应、角色技能上限”中英文组合检索，未得到直接实验该缺口的新高相关 2026 论文，故停止本支扩展。覆盖范围以 ACL、arXiv、ICLR 与目标线索为主；可能遗漏未被上述数据库收录、未开放摘要或未被搜索引擎索引的工作，不能声称穷尽。

**截止日期补充筛选。** [CHARM: Character Hallucination for Multicultural Role Play Benchmark](https://arxiv.org/abs/2609.01352) 的 arXiv 版本历史给出 **2026-09-01**，早于截止日；[合法 PDF](https://arxiv.org/pdf/2609.01352) 可直接访问并核对标题页。论文覆盖 5 个文化语言区域的 40 名真人与虚构角色，区分知识边界的识别（Boundary-Awareness）与回答时遵守边界（Boundary-Compliance）；研究对象与时间均符合范围，已纳入。arXiv 页只写“被 Findings of EMNLP 2026 接收”，截至本次核验未找到正式 Anthology 条目，故正式发表日期留空。其结论只针对**知识**边界，不代表角色的技能或社交能力上限。

### 编号、版本与元数据异常

1. [DREAM arXiv 页](https://arxiv.org/abs/2608.05170) 的编号看似 2026-08，但版本历史明示 v1 为 **2026-05-27**；[role steering arXiv 页](https://arxiv.org/abs/2608.00023) 同样编号看似 2026-08，版本历史明示 v1 为 **2026-07-09**。目录保留原始页面日期并标记冲突；不按编号推算首次公开日。
2. [RoleCDE arXiv 摘要](https://arxiv.org/abs/2606.01552) 说约 **24k** 困境实例，[ACL 落地页摘要](https://aclanthology.org/2026.findings-acl.106/) 误写近 **240k**；但 [ACL 正式 PDF 第 1、4 页](https://aclanthology.org/2026.findings-acl.106.pdf) 写 **24k**，第 4 页给出确数 **23,871**（7,957 个角色场景对 × 3 难度）。ACL 网站说明 PDF 才是权威版本；目录与笔记采用 PDF 数字，记录页面摘要十倍错误。
3. [Memory-Driven 预印本](https://arxiv.org/abs/2603.19313) 将一个 MREval 阶段写作 **Recalling**，而 [ACL 正式摘要](https://aclanthology.org/2026.findings-acl.1175/) 写作 **Selecting**。目录摘要用正式版名称，保留差异。
4. ChatAnime 2025 [预印本](https://arxiv.org/abs/2508.06388) 标题为 *LLMs vs. Chinese Anime Enthusiasts...*、作者 4 人；2026 [ACL 正式版](https://aclanthology.org/2026.acl-long.2179/) 改题并列作者 5 人。相同数据规模与结论支持同一工作合并；作者栏依正式版。
5. [反派角色论文预印本](https://arxiv.org/abs/2511.04962) 的早期作者列表末位是 **Linus**，而 [ACL 正式版](https://aclanthology.org/2026.findings-acl.282/) 末位是 **Liefeng Bo**。目录依正式版作者，并保留版本差异说明。
6. `PersonaForge` 一词还指另一篇 [arXiv 2608.28378](https://arxiv.org/abs/2608.28378) 用户模拟论文；它与此处 ACL 2026 心理架构论文不是同一论文，未合并。

## 候选精读与研究判断

- **CDT：场景 → 行动的可执行规则。** 正式 PDF 把人物故事中的场景与行动对归纳为带条件检查的决策树，测试跨故事后半段的行动预测；其 [Limitations](https://aclanthology.org/2026.acl-long.568.pdf) 明说目前只用故事行动数据、离线建树且不追踪新增剧情。研究设想：让每个条件叶子保留原作场景证据及置信度，并让未见场景走“可推断但未证实”路径，不把树叶当作原作明示事实。
- **CFSM：状态转移与技能获得。** [ICLR 正式 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a862f5788fd09bb6843c694d8120d50c-Paper-Conference.pdf) 用人物档案生成状态集合及可执行转移逻辑，再比较合成转移任务与原作人物情境。作者在局限中明确：状态集合固定，无法自然表现角色**获得新技能**；一步 Markov 转移也无法表示过去失败后不愿重试或技能冷却。这正是能力随经历变化的未解细节。
- **AdaMARP：场景动作与世界变化。** [正式 PDF](https://aclanthology.org/2026.findings-acl.1563.pdf) 把思想、动作、环境、对白写成可交错的消息，并由 Scene Manager 决定选发言者、切换场景、加入人物、结束。它可用于动作轨迹结构和环境更新的对照，但多角色叙事流畅度不能证明特定原作人物是否真的会做某项动作。
- **ChatAnime：情感支持与角色真实性可能冲突。** [正式 PDF](https://aclanthology.org/2026.acl-long.2179.pdf) 的 20 个动漫角色、60 个真实生活情绪问题，分别评估角色性、情感支持和回答多样性。作者仅用两轮互动，且主要面向中文用户；其“顶尖模型比人类粉丝更会安慰”的结果不能推出“原作中社交笨拙的角色也应该安慰得熟练”。研究设想：对每名角色另外标注原作可见的安慰方式、迟疑、回避与求助行为，避免把通用高情商设为唯一正确答案。
- **REVERIEMEM、PsyMem、BOOKMARKS：三种记忆边界。** [REVERIEMEM](https://arxiv.org/abs/2606.25632) 使用第一人称情节记忆和可见性标记解决越界知识；[PsyMem](https://aclanthology.org/2026.tacl-1.24/) 训练模型显式对齐记忆和心理指标；[BOOKMARKS](https://arxiv.org/abs/2605.14169) 按故事时间点更新可复用问答。三者共同提示“人物知道什么”必须带时间与视角；它们均未直接证明“人物会不会安慰、能否修理、能否战斗”等技能上限。
- **CHARM：知道边界与遵守边界分开测。** [原文 PDF](https://arxiv.org/pdf/2609.01352) 采用跨时间、跨作品宇宙的题目，并把直接询问是否知道与隐含边界的具体问答配对；一些模型能正确识别越界，却仍用自身参数知识作答。它提供知识边界诊断方法，但问题形式是带弃答项的选择题，不能评价“尝试但做不好”的行动能力。
- **RoleCDE 与反派评测：价值冲突和标准助手偏差。** [RoleCDE](https://aclanthology.org/2026.findings-acl.106/) 的角色价值和对齐偏好困境、[Too Good to be Bad](https://aclanthology.org/2026.findings-acl.282/) 的反派角色保真度下降，显示通用助手倾向会遮蔽人物动机。研究设想：评测时分别记录安全约束符合度与有证据支持的角色偏好，避免把两者混为一个总分。
- **匿名与多轮评测。** [SIGDIAL 匿名评测](https://aclanthology.org/2026.sigdial-1.15/) 说明知名角色名称可提供隐含线索；[PALATE](https://arxiv.org/abs/2607.27816) 说明固定对话前缀和统一 rubric 会掩盖个体用户、多轮轨迹差异。适用于“去角色名但给原作证据”与“有角色名”配对实验，并记录多轮环境和情绪状态。PALATE 以用户体验为目标，仍需额外原作证据评分。

## 目前仍无直接证据的能力上限问题

现有 2026 论文把“boundary”主要操作化为**知识可见性**、**记忆选择**或**价值冲突**。CHARM 精细区分知识边界的识别与遵守，但仍不能替代“知道步骤但手不熟”“想帮忙但社交表达笨拙”“技能失败后如何复盘或求助”的能力与行动实验。即便 CFSM 指出“获得新技能”是其固定状态模型的局限，仍未给出可追溯原作证据、覆盖成功/尝试/失败/求助/拒绝的分层标注法。后续研究需要把知识、技能、社交执行力分别标注，且每条标注附原作场景、故事时间和推断等级。
