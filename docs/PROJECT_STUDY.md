# 从热门 Skills 项目学什么

调研日期：2026-10-26。Star 来自当日 GitHub REST 仓库元数据快照，会继续变化。
这是按代表性选取的五个项目，不是排行榜，也不能由目录设计推断其获得 Star 的因果。
本库只借鉴组织方法，所有新增技能与文案独立编写，没有复制第三方技能正文。

| 项目与原始材料 | Star 快照 | 类型 | 可借鉴的设计 | 本库的落地 |
| --- | ---: | --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) · [README](https://github.com/obra/superpowers/blob/main/README.md) | 304,934 | 工作流框架 | 说明技能之间如何衔接，从用户任务走到交付物 | 企业、交易、组合、市场叙事四种工作流 |
| [anthropics/skills](https://github.com/anthropics/skills) · [README](https://github.com/anthropics/skills/blob/main/README.md) | 183,702 | 官方示例库 | 自包含技能、标准入口和按需参考资料，标明许可范围 | 保持单技能可安装，原文权利单独说明 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) · [README](https://github.com/msitarzewski/agency-agents/blob/main/README.md) | 163,938 | 角色与交付物库 | 用具体工作场景让读者理解用途 | README 的按任务入口和可复制提示；不模仿投资者人格 |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) · [质量标准](https://github.com/VoltAgent/awesome-agent-skills#skill-quality-standards) | 36,340 | 策展目录 | 分类清楚，描述说明触发条件，强调成熟使用与贡献质量 | 来源提案、使用反馈 Issue 表单和 PR 检查项 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · [发现索引](https://github.com/vercel-labs/agent-skills#discovery-index) | 32,999 | 工程技能库 | 明确使用场景、可发现的机器元数据与分发 | 由真实 frontmatter 生成 skills-index.json，并在 CI 检查漂移 |

Star 元数据原始接口示例：[GitHub REST](https://api.github.com/repos/obra/superpowers)。
其他项目的快照采用同一 `/repos/{owner}/{repo}` 端点，未把第三方排名当成原始来源。

## 明确不照搬的部分

角色库不一定使用标准 SKILL.md；本项目保留标准格式。
开发框架的强制步骤、自动委派或全局钩子不适合直接套在投资研究中。
维护者也不会为了被目录收录而自动向这些项目提交推广 PR 或发送消息。

我们的索引是本库的轻量元数据格式，不是 Vercel 的归档分发格式、官方 registry
或已被第三方收录的证明。CLI 的技能发现仍基于各目录中的 SKILL.md。

## 这轮落实的改进

- 新增四个有不同研究作用的框架：反向思考、价值陷阱、经营证据、反身性。
- [任务工作流](PLAYBOOKS.md)：可复制输入、框架顺序、阶段产物和停止条件。
- [输入与输出模板](../templates/research-brief.md)：降低第一次使用的材料准备成本。
- [机器索引](../skills-index.json)：供工具按任务或名称检索，来源由技能自己携带。
- 结构检查、索引同步检查与明确范围的安装检查，避免“文案很完整，使用入口不工作”。

传播上的判断是：清晰的首次体验、可信的来源和可见的交付物值得投入。
这些是产品设计假设，仍需后续真实使用和反馈验证，不能承诺项目因此获得多少 Star。

