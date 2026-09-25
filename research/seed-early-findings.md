# 2018–2024 起始集核验与扩展检索

检索日期：2026-09-25（Asia/Shanghai）。记录见 [`../catalog/seed-early.jsonl`](../catalog/seed-early.jsonl)。本批 36 条：用户起始集去重后 19 条，新增 17 条。年份按**首次公开日期**统计：2018 年 3、2019 年 1、2020 年 2、2021 年 0、2022 年 4、2023 年 10、2024 年 16。部分论文后来才正式发表，因此正式发表年份另见 `publication_date`。

## 检索与筛选过程

| 轮次 | 实际使用的检索入口与词组 | 结果和处理 |
|---|---|---|
| 起始核验 | ACL Anthology 的 14 个指定编号；arXiv 的 6 个指定编号；按论文标题分别检索对应 arXiv / ACL 正式页 | 官方页面逐条核对题名、作者、首次公开与正式发表日期、DOI、PDF。RoleLLM 的 arXiv / ACL 两版合并。补出早期论文与 2024 年 ACL 论文的先行预印本。 |
| 第一轮主题扩展 | Web 检索限定 `site:aclanthology.org` 或 `site:arxiv.org`：`role-playing character action world state`、`fictional character knowledge boundary timeline`、`role-playing social emotion benchmark`、`persona decision belief action`、`角色扮演 大语言模型 知识边界 时间线`、`虚构角色 场景 行动 目标 动机` | 纳入 [SocialBench](https://aclanthology.org/2024.findings-acl.125/)、[IBSEN](https://aclanthology.org/2024.acl-long.88/)、[OpenToM](https://aclanthology.org/2024.acl-long.466/)、[Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591/) 等；排除将“role playing”仅作为任务提示词、与原作人物无关的通用多智能体论文。 |
| 第二轮引文扩展 | 阅读 [TimeChara](https://aclanthology.org/2024.findings-acl.197.pdf) 附录的 concurrent benchmark 比较和 [Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591.pdf) 相关工作；以 `RoleEval`、`MORTISE`、`WikiRole`、`boundary-aware learning`、`roleplay-doh principles` 为词回查原始页；用较晚的 [CoSER](https://proceedings.mlr.press/v267/wang25dk.html) 与 [RoleMRC](https://aclanthology.org/2025.findings-acl.1082/) 参考文献作向前引用线索 | 纳入 [RoleEval](https://arxiv.org/abs/2312.16132)、[MORTISE](https://arxiv.org/abs/2402.10618)、[ERABAL](https://arxiv.org/abs/2409.14710)、[Ditto](https://aclanthology.org/2024.acl-long.423/)；沿 CharacterGLM 引文补 [Harry Potter Dialogue](https://aclanthology.org/2023.findings-emnlp.570/) 与 [DuLeMon](https://aclanthology.org/2022.findings-acl.207/)。向前引用中 2025–2026 新论文交由后续年份批次处理。 |
| 第三轮查漏 | 进一步搜 `fictional character action ability world state`、`character profiling fictional works`、`character-action interactions role-playing game`、`fictional character few utterances`，并追查 ACL 2018、2022、2024 正式页 | 纳入 [Deep Dungeons and Dragons](https://aclanthology.org/N18-2111/)、[Meet Your Favorite Character](https://aclanthology.org/2022.naacl-main.377/)、[CroSS](https://aclanthology.org/2024.emnlp-main.456/) 及关于信念关联的 [Beyond Demographics](https://aclanthology.org/2024.findings-emnlp.819/)；把“仅模仿台词”和“人物行动”区分为不同证据。 |
| 第四轮停止检查 | 限定 ACL/arXiv 2018–2024，搜 `fictional character skill cannot role-playing`、`socially awkward role play LLM`、`character capability boundary action`、`role-playing try fail ability` | 返回已纳入论文、后续年份论文和一般角色提示论文；本批未再得到可确认的高相关新论文，停止扩展。 |

数据库/站点：ACL Anthology、arXiv、OpenReview、ACM/官方 UIST、Google Research 作者公开版本；搜索引擎只用于发现，书目依据以原始页面为准。中文组合检索的主要结果是英文论文的转载或中文介绍；这些二手页未用来定稿元数据。下载合法开放原文的候选仅保留 ACL、arXiv、OpenReview、会议或作者公开 PDF。

纳入标准：直接研究既有人物或角色对话、人物心理/场景选择、角色知识与技能边界、行动与记忆架构，或能为这些问题提供具体可检验方法的相邻研究。`relevance=medium` 的 PersonaChat、Dialogue NLI、OpenToM 等主要作历史对照或诊断参考。未纳入通用人格提示、泛化情绪支持、仅用“角色扮演”给多代理分工的论文；例如 [LEGO](https://aclanthology.org/2023.findings-emnlp.613/) 属于因果解释多代理分工，不复现特定虚构人物。[ESC-Eval](https://aclanthology.org/2024.emnlp-main.883/) 研究一般情绪支持能力，并未衡量既有角色应有的社交能力上限。检索不是系统综述，不能声称覆盖所有论文。

## 起始集核验中的重要修正

1. [RoleLLM](https://arxiv.org/abs/2310.00746) 2023-10-01 首次公开，正式版为 [ACL Findings 2024](https://aclanthology.org/2024.findings-acl.878/)（2024-08）；在目录中只有一条。
2. [Character is Destiny](https://arxiv.org/abs/2404.12138) 2024-04-18 首次公开，正式版为 [EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.813/)（2025-11），标题改为 *Character is Destiny: Can Persona-assigned Language Models Make Personal Choices?*；正式版的 LIFECHOICE 数据规模也不同，不能混用预印本早期数值。
3. [From Persona to Personalization](https://arxiv.org/abs/2404.18231) 于 2024-04-28 首次公开；[TMLR 正式 PDF](https://openreview.net/pdf?id=xrO70E8UIZ) 标明 2024-10 发表。自动下载 OpenReview 可能遇到 403，目录使用合法 arXiv 作者版本 PDF，保留正式页。
4. [Generative Agents](https://arxiv.org/abs/2304.03442) 2023-04-07 首次公开；[ACM UIST 正式页](https://doi.org/10.1145/3586183.3606763) 给出 2023-10-29，PDF 选 [Google Research 公开的 UIST 版本](https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/374fbe430867bf8449a4138d2bc9e649829d7d08.pdf)。
5. [CharacterGLM 早期版](https://arxiv.org/abs/2311.16832) 与 [EMNLP Industry 2024 版](https://aclanthology.org/2024.emnlp-industry.107/) 同属 CharacterGLM 工作，但题名由“Chinese Conversational AI Characters”改为“Social Characters”，正式版作者增加、内容扩展；合并一条并以正式版书目为准。
6. [CharacterEval](https://arxiv.org/abs/2401.01275) 初稿与 [ACL 2024 正式版](https://aclanthology.org/2024.acl-long.638/) 的作者数和例数不同；目录采用 ACL 的作者表和正式 PDF，不沿用初稿摘要里的数字。[SocialBench](https://arxiv.org/abs/2403.13679) 初稿作者表也与 [ACL 正式版](https://aclanthology.org/2024.findings-acl.125/) 不同。
7. 指定的早期 ACL 论文均可追溯更早预印本：[P18-1205](https://arxiv.org/abs/1801.07243) 首发 2018-01-22；[P19-1363](https://arxiv.org/abs/1811.00671) 首发 2018-11-01；[D19-1062](https://arxiv.org/abs/1903.03094) 首发 2019-03-07；[2020.emnlp-main.65](https://arxiv.org/abs/2004.05816) 首发 2020-04-13；[2021.naacl-main.64](https://arxiv.org/abs/2010.00685) 首发 2020-10-01。所以“2021 NAACL”并不等于 2021 首次公开。
8. [InCharacter](https://arxiv.org/abs/2310.17976) 实为 2023-10-27 首发、2024-08 ACL 正式发表；[Capturing Minds](https://arxiv.org/abs/2406.18921) 正式版按 ACL 作者顺序入库。ACL 只给出发表月份时，目录保持 `YYYY-MM`，没有擅自补日。

## 新增论文与研究价值

| 论文 | 纳入理由及证据界限 |
|---|---|
| [I Cast Detect Thoughts](https://aclanthology.org/2023.acl-long.624/) | 玩家有各自 persona 与能力，Dungeon Master 显式建模意图和 Theory of Mind 并引导行动；适合参考“会做什么”评测，但并非原作人物复现。2022 年先行 [arXiv](https://arxiv.org/abs/2212.10060)。 |
| [Deep Dungeons and Dragons](https://aclanthology.org/N18-2111/) | 2018 年角色属性与行动序列关联的前 LLM 奠基工作，显示属性有助于预测行动；数据来自 RPG 玩家记录，不能证明虚构原作人物的长期一致性。 |
| [Meet Your Favorite Character](https://aclanthology.org/2022.naacl-main.377/) | 以少量原角色台词构造伪对话提示，是“只学话语风格”的明确历史对照；尚无能力边界或行动选择机制。 |
| [DuLeMon](https://aclanthology.org/2022.findings-acl.207/) | 动态更新用户与聊天机器人的长期 persona 记忆，可比较关系状态维护；角色是一般聊天 persona，不针对原作人物。 |
| [Harry Potter Dialogue](https://aclanthology.org/2023.findings-emnlp.570/) | 将场景、说话人、关系和属性随情节变化标注，最接近可追溯原作上下文的角色对话基准。论文可入库；含原作英文/中文台词及书籍内容的数据集不下载、不入 Git。2022 年 [arXiv 初稿](https://arxiv.org/abs/2211.06869) 的题名是 *What Would Harry Say?*。 |
| [CharacterChat](https://arxiv.org/abs/2308.10278) | 行为预设和动态记忆支持个性化社交支持；属于泛角色系统，不证明特定原作角色的笨拙反应。 |
| [NarrativePlay](https://aclanthology.org/2024.eacl-demo.10/) | 用户扮演小说人物并按叙事事件互动，适合作为第一人称叙事视角与关系状态的设计参考；系统 demo 的实验不能替代严格的角色一致性测试。2023 年先行 [arXiv](https://arxiv.org/abs/2310.01459)。 |
| [RoleEval](https://arxiv.org/abs/2312.16132) | 人物经历、关系和能力的双语知识选择题，可查模型知道的角色信息；答对能力描述不等于能在情境中表现出能力上限。 |
| [MORTISE](https://arxiv.org/abs/2402.10618) 与 [ERABAL](https://arxiv.org/abs/2409.14710) | 分别用对抗边界提问与边界感知训练测试角色偏离；其“boundary”主要是角色设定和知识/回答边界，不能直接当作社交技能或行动能力的证据。 |
| [SocialBench](https://aclanthology.org/2024.findings-acl.125/) | 分开评价个体与群体社交表现，发现个体高分不保证群体高分；适合多角色关系测试，但没有给每名原作人物建立独立的“应当不会”金标准。 |
| [Ditto](https://aclanthology.org/2024.acl-long.423/) | 自生成角色对话并做 self-alignment，作者分析模型内在知识对扮演的限制；这不是“训练后角色所有能力都被复制”的证据。 |
| [IBSEN](https://aclanthology.org/2024.acl-long.88/) | director/actor 结构明确处理剧情目标与参与者行动；输出主要是剧本生成，评测没有全面测试人物技能上限。 |
| [OpenToM](https://aclanthology.org/2024.acl-long.466/) | 人物偏好、错误信念、意图与行动的叙事测试，适合构造“想安慰但误解对方”等心理状态题；不是既有人物模拟研究。 |
| [CroSS 角色画像评测](https://aclanthology.org/2024.emnlp-main.456/) | 用文学专家画像与下游适用性评估自动抽取的人物简介，可作为从原作场景到设定卡的证据检查环节；画像质量不能替代新情境行为检验。 |
| [Beyond Demographics](https://aclanthology.org/2024.findings-emnlp.819/) | 实测“给一个信念”能改善相邻议题的意见分布一致性，但研究对象是人群信念模拟，测的是**表达的意见**，不是角色行动或稳定价值观。 |
| [Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591/) | 专家反馈变为条件化行为规则，实验证明可让模拟患者表现犹豫、少说、混乱等真实行为。直接启发将原作可追溯的局限写成条件规则；未验证虚构人物。 |

## Roleplay-doh 精读供后续笔记复核

原文：[ACL Anthology PDF](https://aclanthology.org/2024.emnlp-main.591.pdf)，以下页码为论文印刷页码。

- **问题与机制**：基础 GPT-4 对专家规则或对话惯例的违背为 55/276（20%；p.10573 §3.2）。专家与患者模型对话，对不真实回答给反馈，系统转换为自然语言原则。生成时先出候选，再把原则拆成 yes/no 问题、增补一般对话连贯性问题；判断条件是否适用（不适用返回 N/A），违背时重写候选（pp.10573–10574，图 2 与 §4）。
- **具体的有限/不完美行为**：25 名专家共写 123 条规则，中位 5 条/角色；14 人写“初始不信任或犹豫求助”，9 人写“对情绪和需要较少自知、表达较混乱”，也有“少说”和“接受鼓励后怀疑其意义”等条件行为（pp.10575–10576，§5.2/Table 2）。这些是患者个案规则，不能作为任意虚构人物的通用特质。
- **实验**：25 名咨询专家同一受试者内比较仅场景描述与场景加专家原则；创建者评分中真实性在 7 分制上增加 0.80，第三方评分增加 0.31；“stayed in role”未见显著改善。第三方 5 位咨询者对 25 个病例给出 125 对比较（p.10576，Table 1）。40 个选自原始错误的回合做消融，Full 流程的对话措辞错误 2.5%，无批评改写时为 15%（p.10577，§6）。这里的“awkward style”是**无意的语言不自然**，而研究目标中的角色社交笨拙是**有原作证据的行为特征**，不能混为一谈。
- **局限**：病例种类有限，严重精神疾病病例仅 1 个；用户研究中的对话因时间限制提前结束；系统不自动识别规则重叠或冲突；只测文字对话，缺少语气、表情、姿态（p.10578，Limitations）。研究没有测虚构人物、跨情境长期稳定性、真实世界行动或角色的技能天花板。

## 余下缺口与遗漏风险

- 2018–2024 工作多把“边界”落实为知识、时间线或答题范围；几乎没有直接以原作证据定义并评测人物**技能/社交能力上限**、会尝试但做得不好的动作、求助与能力性拒答。需用研究设想设计独立的技能边界题，不能把 TimeChara/RoleFact 的知识边界指标复用为技能指标。
- Roleplay-doh 给出可行的条件规则和人评方式，但还需验证如何从原作场景可靠提取规则、如何区别稳定缺陷与阶段性情绪、如何处理规则冲突，以及角色在新情境能否保持恰当的有限表现。
- 本批主要覆盖 ACL、arXiv、UIST、TMLR 的英文元数据和中文语境角色研究。中文本土期刊、游戏 AI/HCI 论文、商业产品实验以及未被索引的工作可能遗漏；中文搜索结果常是论文介绍而非原始出版，故未据此纳入。发现 2025–2026 后续引用文献已交由其他年份批次跟进。
