# 角色行为建模路线比较

本文件比较文献中的**研究途径**，不表示本仓库已训练模型。目标是在新情境中同时限制角色可知事实、可执行技能、社会表现和状态变化。效果只归因于各论文实际评测的范围；下面的组合方案均标作**研究设想**。

| 途径 | 具体机制及文献证据 | 可提供的证据 | 尚不能证明 |
| --- | --- | --- | --- |
| 角色提示词与检索 | 将角色简介、原作时点和相关片段放入上下文；[TimeChara](https://aclanthology.org/2024.findings-acl.197/) 专门测试叙事时点知识，[TailorRPA](https://aclanthology.org/2025.findings-emnlp.288/) 报告以细粒度记忆与保护性查询改善一般领域角色对话。 | 可测试时点检索和事实隔离是否减少越界回答。 | 检索到事实并不等于角色会运用技能、会采取符合习惯的动作；模型仍可从自身预训练知识泄漏后续剧情。 |
| 台词语料和角色微调 | [Character-LLM](https://aclanthology.org/2023.emnlp-main.814/) 及 [RoleLLM](https://aclanthology.org/2024.findings-acl.878/) 从角色语料构造训练及评测；[Thinking Before Speaking](https://arxiv.org/abs/2409.13752) 进一步加入推测的心态与越界知识样本。 | 可比较对话口吻、事实记忆、作者评测中的人设一致性；TBS 消融显示其评分对心态和越界样本敏感。 | 台词分数无法单独验证未见场景动作、真实心理机制或技能上限；合成心态不自动成为原作事实。 |
| 受约束的记忆与世界状态 | [Generative Agents](https://arxiv.org/abs/2304.03442) 用记忆、反思、计划模拟长期互动；[PsyMem](https://aclanthology.org/2026.tacl-1.24/) 研究心理对齐与显式记忆控制；[BOOKMARKS](https://arxiv.org/abs/2605.14169) 与 [perspective-bounded memory](https://arxiv.org/abs/2606.25632) 针对情节记忆及视角边界。 | 可逐回合审计「角色见到什么、何时知道、关系如何变化」，避免跨时点记忆混用。 | 记忆机制本身不限制说话能力或行动成功率，写入错误推断还可能固化幻觉。 |
| 可执行行为规则 | [Roleplay-doh](https://aclanthology.org/2024.emnlp-main.591/) 从专家批评提炼条件规则，再检查适用性和遵循情况；[Codified Decision Trees](https://aclanthology.org/2026.acl-long.568/) 探索从故事线提炼决策逻辑。 | 可以显式测试「何种情境触发犹豫、求助、拒绝或某类行动」，并追踪每条规则的证据来源。 | 针对模拟病人的专家规则及角色决策树不能直接证明任意虚构人物的长期真实性；规则冲突、例外和隐性行为仍需人工处理。 |
| 表示编辑与 activation steering | [Tell Me What You Don’t Know](https://aclanthology.org/2025.findings-acl.311/) 研究角色未知知识的拒答表示编辑；[Persona Vectors](https://arxiv.org/abs/2507.21509) 与 [Role Steering](https://arxiv.org/abs/2608.00023) 探索特质/角色相关的激活干预。 | 可针对某一特质或知识边界做受控消融，观察副作用。 | 调节一个向量或拒答倾向，不足以证明已复现完整人物、技能谱、经历或行动政策。 |
| 偏好优化与强化学习 | [CPO / CharacterArena](https://aclanthology.org/2025.findings-emnlp.18/) 用多轮轨迹比较减少主观奖励的歧义；[HER](https://aclanthology.org/2026.findings-acl.1283/) 研究角色内在推理与强化学习。 | 可检验一组明确偏好标签是否改善轨迹级角色表现。 | 偏好信号若把「更会安慰、更有效率」一律奖励，可能抹平原作角色的笨拙与失败；奖励模型不能代替原作证据。 |
| 行动层环境与状态机 | [STSS](https://aclanthology.org/2024.findings-acl.526/) 发现对话表现与沙盒行动达成有落差；[RolePlot](https://aclanthology.org/2025.acl-long.603/) 关注推进剧情；[AdaMARP](https://aclanthology.org/2026.findings-acl.1563/) 显式组织思想、行动、环境和发言。 | 可记录动作是否执行、世界是否响应、角色是否遵循因果与剧情约束。 | 环境中更高的通用成功率不等于对某角色更忠实；模拟器与其他代理会影响结果。 |

## 候选组合：证据先行的行为约束（研究设想）

1. 为每个角色建立带时间、视角、来源场景的证据卡。分别记录事实、技能、价值目标、关系、情绪和行为习惯；每项标明「原文明示 / 研究者推断 / 未知」。不要存储整本原作。
2. 情境状态由当前时点、角色可见环境、互动对象和前序动作组成。检索只返回此视角可知的证据卡；缺乏证据时保留不确定性。
3. 先选**动作意图**：尝试、回避、求助、拒绝、拖延或其他可执行动作。规则层约束技能上限和条件触发；世界状态层决定执行结果；最后生成符合口吻的表达。
4. 将记忆分为原作固定背景与本次互动增量。每次更新记录来源和有效时间；关系及情绪状态可以变化，既有原作事实不因一次模型输出而自动改写。
5. 用 [TimeChara](https://aclanthology.org/2024.findings-acl.197/) 类时点题、[DMT-RoleBench](https://ojs.aaai.org/index.php/AAAI/article/view/34768) 的知识/技能分项、[STSS](https://aclanthology.org/2024.findings-acl.526/) 类行动结果和匿名人评做独立消融。尚无证据表明这种组合优于单一方案，需要实验。

## 选择原则

优先把「不知道」与「不会做」设成不同变量。未知事实可以触发询问或承认不知道；技能不足可以触发尝试后失败、调整策略或求助；社交能力不足可以体现为迟疑、误解、表达笨拙。每一种反应都须来自原作证据或明确的推断，不能把通用礼貌、万能共情当作所有角色的默认设定。
