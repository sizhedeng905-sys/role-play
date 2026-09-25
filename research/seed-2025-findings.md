# 2025 起始集核验与扩展检索

检索日期：2026-09-25（中国标准时间）。范围是截至该日已经公开的论文。书目信息以 ACL Anthology、arXiv、PMLR、AAAI、COLM 官方页面及正式 PDF 为准；`catalog/seed-2025.jsonl` 保留同篇论文的正式版和预印本链接。这里的“首发”是**查到的最早原始来源日期**；若仅有正式页面按月标注，就只写到月份，不推测具体日子。未声称检出全部论文。

## 实际检索与筛选

| 轮次 | 来源与检索式（按原意记录） | 发现及处理 |
| --- | --- | --- |
| 起始核验 | 逐一打开用户给出的 12 个 2025 ACL 编号、PMLR `v267/wang25dk`、3 个 arXiv 编号；查 ACL 的 PDF、DOI、作者、月份与 arXiv v1 历史。 | 16 篇起始论文均有原始页面和公开 PDF；同篇预印本与正式版合并。起始集条目数 16，不把 `CoSER` 的 2026 arXiv 改题另算一篇。 |
| 第一轮扩展 | Web 检索并逐条转到原站：`site:aclanthology.org 2025 role playing agents social skills empathy awkward character behavior`、`site:aclanthology.org 2025 fictional character knowledge boundaries ability action decision role playing agents`、`site:arxiv.org 2025 role playing agents social competence imperfect behavior characters`、`角色扮演 社交 行为 情感 知识边界 2025`；另按标题检索 arXiv 版本。 | 纳入 [MIRAGE](https://aclanthology.org/2025.acl-short.2/)、[RAIDEN](https://aclanthology.org/2025.coling-main.735/)、[RoleBreak](https://aclanthology.org/2025.coling-main.494/)、[CharacterCraft](https://aclanthology.org/2025.findings-emnlp.323/)、[CharacterGPT](https://aclanthology.org/2025.naacl-industry.24/)；前两篇对复杂互动、多轮情境最直接。 |
| 第二轮扩展 | 回看 [RoleMRC 正式 PDF](https://aclanthology.org/2025.findings-acl.1082.pdf) 的相关工作与表 1、[CharacterBox 正式 PDF](https://aclanthology.org/2025.naacl-long.323.pdf) 的方法及引用；用 `RoleMRC skill`、`CharacterBox action`、`CharacterEval ability boundary`、`2025 role knowledge error`、`DMT-RoleBench` 做追踪；检索 2026 论文对 CharacterBox/RoleMRC 的后向使用。 | 纳入 [RoleKE-Bench](https://aclanthology.org/2025.emnlp-main.1689/) 和 [DMT-RoleBench](https://ojs.aaai.org/index.php/AAAI/article/view/34768)。RoleMRC 表 1 回溯到 CharacterLLM、RoleLLM、CharacterEval 等已在起始集的作品；[2026 RoleCDE](https://aclanthology.org/2026.findings-acl.106.pdf) 引用 CharacterBox，属向前追踪，已由 2026 检索组处理。第二轮在本组重点上未再产生新的高相关 2025 论文。 |

纳入标准：直接研究既有角色、角色知识与技能边界、心理或社交行为、场景动作、长期角色轨迹，或对这些目标有直接作用的评测与干预。间接方法保留 `medium` 关联程度并写明证据外推的边界。使用英文与中文关键词；中文论文或中文角色数据仍以原始出版页核查。

排除记录：[SweetieChat](https://aclanthology.org/2025.coling-main.312/) 虽把“角色扮演”用作情感支持对话生成策略，但目标是通用支持 Agent，没有既有角色的原作约束或“应当笨拙”评价；[KnowAgent](https://aclanthology.org/2025.findings-naacl.205/) 研究通用任务规划的动作知识库，缺少角色忠实度；[Learning to Play Like Humans](https://aclanthology.org/2025.findings-acl.531/) 是通用互动小说游戏策略，缺少固定人物角色证据；[OmniCharacter](https://aclanthology.org/2025.acl-long.1276/) 主要处理语音和语言人格交互，对当前文本角色能力边界较间接。它们可作未来外围参考，本批不纳入。

## 起始集逐一核验

| 起始编号 | 实际论文与版本结论 |
| --- | --- |
| [2025.findings-acl.1082](https://aclanthology.org/2025.findings-acl.1082/) | RoleMRC；[arXiv:2502.11387](https://arxiv.org/abs/2502.11387) 2025-02-17 首发，ACL 2025-07。 |
| [2025.findings-acl.311](https://aclanthology.org/2025.findings-acl.311/) | Tell Me What You Don't Know；[arXiv:2409.16913](https://arxiv.org/abs/2409.16913) 2024-09-25 首发，ACL 2025-07。正式版增列 Changze Lv。 |
| [2025.naacl-long.316](https://aclanthology.org/2025.naacl-long.316/) | EmoCharacter；核到 NAACL 2025-04，未核到更早公开的原始版本。 |
| [2025.naacl-long.323](https://aclanthology.org/2025.naacl-long.323/) | CharacterBox；[arXiv:2412.05631](https://arxiv.org/abs/2412.05631) 2024-12-07 首发，NAACL 2025-04。 |
| [2025.findings-acl.938](https://aclanthology.org/2025.findings-acl.938/) | RPA evaluation survey；[arXiv:2502.13012](https://arxiv.org/abs/2502.13012) 2025-02-18 首发，ACL 2025-07。预印本与正式版作者列表有差异，以正式版为准。 |
| [2025.findings-acl.1344](https://aclanthology.org/2025.findings-acl.1344/) | Persona-Aware Contrastive Learning；[arXiv:2503.17662](https://arxiv.org/abs/2503.17662) 2025-03-22 首发，ACL 2025-07。 |
| [2025.findings-acl.537](https://aclanthology.org/2025.findings-acl.537/) | Reasoning Does Not Necessarily Improve Role-Playing Ability；[arXiv:2502.16940](https://arxiv.org/abs/2502.16940) 2025-02-24 首发，ACL 2025-07。 |
| [2025.findings-emnlp.819](https://aclanthology.org/2025.findings-emnlp.819/) | ROLETHINK；[arXiv:2503.08193](https://arxiv.org/abs/2503.08193) 2025-03-11 首发，EMNLP 2025-11。 |
| [2025.emnlp-main.1372](https://aclanthology.org/2025.emnlp-main.1372/) | R-CHAR；核到 EMNLP 2025-11。 |
| [2025.findings-emnlp.18](https://aclanthology.org/2025.findings-emnlp.18/) | CPO / CharacterArena；[arXiv:2508.09074](https://arxiv.org/abs/2508.09074) 2025-08-12 首发，EMNLP 2025-11。预印本首作者 Xinge Ye，正式版 PDF 署名 Jing Ye。 |
| [2025.findings-emnlp.288](https://aclanthology.org/2025.findings-emnlp.288/) | TailorRPA；核到 EMNLP 2025-11。 |
| [2025.acl-long.603](https://aclanthology.org/2025.acl-long.603/) | RolePlot；核到 ACL 2025-07。 |
| [PMLR v267/wang25dk](https://proceedings.mlr.press/v267/wang25dk.html) | CoSER；[arXiv:2502.09082](https://arxiv.org/abs/2502.09082) 2025-02-13 首发，ICML 2025-07 正式版。arXiv 2026-01 修订改题，采用 ICML 正式题名。 |
| [arXiv:2507.21509](https://arxiv.org/abs/2507.21509) | Persona Vectors；2025-07-29 首发。单项特质控制与完整人物复现不等价。 |
| [arXiv:2507.02197](https://arxiv.org/abs/2507.02197) | Belief–Behavior Consistency in Human Trust；2025-07-02 首发。 |
| [arXiv:2508.10014](https://arxiv.org/abs/2508.10014) | PersonaEval；2025-08-06 首发，[COLM 2025 官方接收名单](https://colmweb.org/2025/AcceptedPapers.html) 确认正式会议发表，未核得精确出版日。 |

**编号结论：**起始集编号指向的论文均正确；错误主要是把 ACL 2025 条目误作首次公开 2025。Tell Me What You Don't Know 与 CharacterBox 实际首发 2024。另 2024 起始集的 [Character is Destiny](https://arxiv.org/abs/2404.12138) 有 [EMNLP 2025 正式版](https://aclanthology.org/2025.findings-emnlp.813/)，应与原记录合并，而非在 2025 另建一篇。新增的 RoleBreak、CharacterGPT、RoleKE-Bench 也首发于 2024，虽在 2025 正式发表，应按 2024 归档。

## 优先精读的论证边界

1. **能力边界：**[RoleMRC PDF §3.1 与附录](https://aclanthology.org/2025.findings-acl.1082.pdf) 将 `Specific Abilities and Skills` 与 `Ability and Knowledge Boundaries` 分成角色资料的不同字段，并生成“回答／拒答／尝试”任务。这证明可操作化区分，但角色资料来自通用 persona 扩展，不能凭结果证明某既有文学角色的原作技能上限。[DMT-RoleBench PDF Table 1](https://ojs.aaai.org/index.php/AAAI/article/download/34768/36923) 进一步将 Knowledge Boundary Eval、Professional Skill Eval、Game Interaction Eval 分开；其职业技能评价不能直接移植成虚构角色的“会不会”。
2. **场景行动：**[CharacterBox PDF §3.2–3.3](https://aclanthology.org/2025.naacl-long.323.pdf) 明确让角色在时间、地点和其他角色组成的环境里逐轮计划并执行动作，由 narrator 更新环境、身体位置和心理状态。这比台词相似度更接近研究目标；但状态由模拟框架生成，必须另设原作证据审查。[MIRAGE](https://aclanthology.org/2025.acl-short.2/) 则提供社交信任、调查与互动的任务信号。
3. **价值与行动：**[Belief–Behavior 论文](https://arxiv.org/abs/2507.02197) 的 Trust Game 表明先让 Agent 陈述信念，再比较行动是必要的；实验对象是合成社会角色，转到原作人物仍须新验证。[RolePlot](https://aclanthology.org/2025.acl-long.603/) 可研究推进情节的时机，但不能只奖励“推进”，否则可能惩罚本来会迟疑或退出的角色。
4. **情绪与社交上限：**[EmoCharacter](https://aclanthology.org/2025.naacl-long.316/) 衡量情绪忠实度；[R-CHAR](https://aclanthology.org/2025.emnlp-main.1372/) 与 [MIRAGE](https://aclanthology.org/2025.acl-short.2/) 衡量社交互动。这些论文多数默认更强的情绪表达或社交表现更好。尚没有可靠的直接证据证明评测能奖励某角色“想安慰却不知如何开口”的恰当失误；这应列为研究缺口，并用原作证据和未见情境设计角色特异测试。
5. **评审误差：**[PersonaEval](https://arxiv.org/abs/2508.10014) 发现 LLM 对人写场景的说话角色识别明显不及人类，提示不能只靠 LLM 裁判打分。[CPO 正式 PDF](https://aclanthology.org/2025.findings-emnlp.18.pdf) 讨论单样本奖励的不稳定并以多轮成对比较缓解，但比较胜负也不自动等于原作忠实度。

本次检索主要覆盖 ACL Anthology、arXiv、PMLR、AAAI、COLM 的可公开论文；受关键词、索引延迟和非英语资料收录范围限制，其他会议、期刊、独立网站仍可能有遗漏。尤其“保留社交笨拙”是细粒度角色特征，现有标题和摘要检索的召回率无法量化。
