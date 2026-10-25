# 一起把投资经验变成可复用的研究流程

欢迎新增框架、补原始出处、纠正归属，或提交 skill 在真实研究任务中的失败案例。
优先做深已有框架，尤其是让抽象词汇变成可核查问题。

## 新增技能

在 `skills/<name>/` 创建 `SKILL.md` 与 `references/sources.md`，并在 `catalog.json`
登记。`name` 使用与目录一致的小写英文和连字符；`description` 用一句话说明做什么、
何时使用。前置字段 `name` 和 `description` 在本库约定为单行 YAML 字符串。

正文应让另一个 agent 能完成一项明确任务：需要什么输入、如何取证、如何推理、
遇到资料不足怎么办、最后交付什么，以及什么情况会推翻判断。只在有实际用途时添加脚本。

来源文件应包含：

- 本人或原机构的直接 URL，原文标题、日期与可定位段落；原页无日期时如实说明。
- 来源等级，及它具体支持哪些观点。
- 原始观点与维护者操作化解释的区别。
- 核查日期（`YYYY-MM-DD`）、访问失败或身份不确定等限制。

请用自己的语言归纳。不要上传付费课程、整本书、原文抓取全集或未获授权的媒体。
人物名称只用于识别思想来源，不能写成官方合作或授权。

## 提交前检查

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build_index.py
.venv/bin/python scripts/build_index.py --check
.venv/bin/python -m unittest discover -s tests -v
```

新增或改名时同步 `catalog.json`，再生成 `skills-index.json`；修改描述也需重新生成索引。
校验不会联网，也不验证策略业绩。PR 说明应写明改动、来源和验证范围。
若声称改善了实际行为，请提供任务输入和输出，说明模型、日期和浏览条件。
可从 [行为评估题](evals/README.md) 选相关案例；不能以关键词匹配代替推理质量检查。
不要把模拟示例写成实测结果，不提交私人账户、身份信息或访问令牌。

## 可以认领的方向

- Livermore 等趋势与风险框架，优先补可靠的一手材料。
- 更好的失效案例、历史时点复盘、缺资料时的表现评估。
- 英文版 skill、客户端安装实测、来源链接维护。

路线图表示可贡献方向；在完成来源核查和行为评估前，不视为已支持。

新框架可使用 [来源提案](https://github.com/superShen0916/investing-skills/issues/new?template=source-proposal.yml)，
遇到实际使用问题可使用 [使用反馈](https://github.com/superShen0916/investing-skills/issues/new?template=skill-feedback.yml)。
也欢迎直接发 PR；本库不会自动替贡献者向外部项目投稿。

