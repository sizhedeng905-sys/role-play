# 这些论文与 AI、原作人物扮演的关系

复核日期：2026-09-25。这里的「AI 相关」指论文研究或评测机器学习、NLP、对话系统、语言模型或 Agent；「原作人物直接范围」另看**主要研究数据或任务**是否包含已有作品中的虚构人物。这两件事不能混为一谈。按书目、原始论文页及可下载 PDF 的研究对象复核，**87/87 篇属于 AI/NLP/机器学习研究**；其中 **48 篇**在宽口径下把已有虚构人物作为主要研究对象或任务来源，另外 **39 篇**是相邻方法与早期基础工作。三类互斥，合计 87 篇。

| 范围 | 篇数 | 阅读时怎样使用 |
| --- | ---: | --- |
| 已有虚构人物进入语言模型相关研究 | 48 | 可找原作人物数据、任务或角色一致性结果；仍须逐篇核对实际测试的是知识、台词、行动还是心理。 |
| 相邻 AI/LLM 方法与评测 | 30 | 可借鉴机制或测量方法，不能把结果直接写成「已证明某原作人物扮演忠实」。 |
| 早期 AI/NLP 基础工作 | 9 | 提供 persona 对话、RPG 行动、目标驱动代理等历史基线，部分早于当代 LLM。 |

上述 48 篇是**研究对象范围**的宽口径计数，不是「48 篇验证了角色技能上限」或「48 篇都有可靠的行动层实验」。其中 47 篇有本地 PDF，Act-LLM 仅有出版页摘要。例如 [TimeChara](https://aclanthology.org/2024.findings-acl.197/) 主要测原作时点知识，[Character is Destiny](https://aclanthology.org/2025.findings-emnlp.813/) 测已发生的原作选择，[Codified Decision Trees](https://aclanthology.org/2026.acl-long.568/) 才进一步尝试可执行决策规则。它们不能互相代替。

## 容易误认为「直接证据」的例子

| 论文 | 实际研究对象或任务 | 对本项目的价值与限制 |
| --- | --- | --- |
| [PersonaChat](https://aclanthology.org/P18-1205/) | 2018 年的 persona 对话模型与数据 | 是 AI/NLP 历史起点；不测试已有原作人物的行动。 |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | 通用模拟社会代理 | 记忆、反思和计划架构可迁移；无原作人物金标准。 |
| [Character-LLM](https://aclanthology.org/2023.emnlp-main.814/) | 论文实验角色主要是贝多芬、埃及艳后、凯撒等历史真人 | 研究 LLM 角色扮演，但不能把真人实验写成虚构角色的原作忠实性证据。 |
| [STSS](https://aclanthology.org/2024.findings-acl.526/) | 语言代理的社会行动结果 | 能启发行动层评测；不是具体原作人物测试。 |
| [Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591/) | LLM 模拟病人 | 条件行为规则可借鉴；论文没有验证原作角色。 |
| [AgentSense](https://aclanthology.org/2025.naacl-long.257/) | 通用互动社会场景 | 可借鉴社交结果评测；不定义某人物应有的社交能力上限。 |
| [ThinkPersona](https://aclanthology.org/2026.acl-long.449/) | 主要用真人访谈构建个体 persona，另在 InCharacter 作泛化测试 | 图式与推理方法可迁移；主实验不是以原作虚构人物为数据来源。 |
| [RoleCDE](https://aclanthology.org/2026.findings-acl.106/) | 从 PersonaHub 的一句话人口/职业描述扩展合成角色困境 | 研究价值与助手对齐的冲突；数据不是来自原作人物。 |
| [RoleBreak](https://aclanthology.org/2025.coling-main.494/) | 使用 WikiRoleEval 的角色资料，正文未交代所测角色的虚构人物构成 | 是 LLM 角色知识安全研究；不能核实其结果对应哪些原作人物。 |
| [Understanding Generalization](https://aclanthology.org/2026.findings-acl.87/) | RPGBench 角色主要由 LLM 生成，所谓文学虚构角色样本也未给出可追溯作品 | 研究角色扮演泛化，但不能当作已有原作人物的实证。 |
| [AdaMARP](https://aclanthology.org/2026.findings-acl.1563/) | 主要训练材料含 81 部书的角色；主要报告的 AdaptiveBench 场景由模型合成 | 归入原作人物数据范围，但其主要分数不能当作原作忠实度。 |

## 互斥分类的完整非直接清单

下列 ID 可在[书目目录](../catalog/papers.jsonl)中检索；**其余 48 条**归入上表第一类。原 `relevance=direct/high/medium` 表示与本项目问题的用途强弱，**不是**「有无原作人物实验」的标记。

**相邻 AI/LLM 方法与评测（30）：** `arxiv-2304.03442`、`arxiv-2308.10278`、`2023.emnlp-main.814`、`2024.emnlp-industry.107`、`arxiv-2312.16132`、`2024.acl-long.466`、`2024.findings-acl.526`、`arxiv-2404.18231`、`2024.findings-emnlp.819`、`2024.acl-long.88`、`2024.emnlp-main.591`、`arxiv-2407.11484`、`2025.coling-main.494`、`2025.naacl-long.257`、`2025.acl-short.2`、`2025.findings-acl.1082`、`2025.findings-acl.938`、`arxiv-2507.02197`、`arxiv-2507.21509`、`arxiv-2508.10014`、`arxiv-2601.10122`、`arxiv-2602.15669`、`2026.acl-long.1491`、`2026.findings-acl.471`、`2026.findings-acl.106`、`2026.acl-long.1336`、`2026.acl-long.449`、`2026.findings-acl.87`、`arxiv-2608.00023`、`arxiv-2607.27816`。

**早期 AI/NLP 基础工作（9）：** `P18-1205`、`N18-2111`、`P19-1363`、`D19-1062`、`2020.emnlp-main.65`、`2021.naacl-main.64`、`2022.findings-acl.207`、`2023.acl-long.624`、`2023.emnlp-main.110`。

## 证据限制

- [Act-LLM](https://www.sciencedirect.com/science/article/pii/S0957417425026417) 的出版页摘要提到虚构角色，归入宽口径第一类；本机 PDF 下载返回 HTTP 403，因此其具体实验结论**仅能依据摘要**，不能当作已精读全文。
- [MORTISE](https://arxiv.org/abs/2402.10618) 的本地 v1 涵盖虚构及真人角色，但 v2 因重大问题撤回；它保留为历史线索，**不作为可靠效果证据**。
- 有些论文混合真人、虚构人物与自定义 persona；即使属于第一类，也必须在引用数字时确认被评测的角色子集。多数工作测对话、知识或人格问答，没有直接测「想做但做不到」的技能与社交能力上限。
