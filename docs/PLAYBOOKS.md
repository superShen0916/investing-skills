# 从任务开始：四种研究工作流

每个包是一组可选技能，按当前问题加载必要部分，不要求每次全部运行。
不熟悉框架时先调用 investment-committee；没有数据时先得到缺口清单。

## 1. 企业研究

**输入：**公司身份、期限、财报、价格时点，以及自己看好或看空的理由。

**流程：**林奇把产品观察转成经营假设 → 巴菲特检查现金创造与生意质量 →
格雷厄姆审查价格余地与价值陷阱 → 芒格找失败路径。只选择当前问题需要的步骤。

**阶段产物：**经营假设表、企业备忘录、价值桥、反方清单。
缺财报时停在研究线索；缺合理估值输入时暂停价格结论。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee buffett-business-quality lynch-business-evidence graham-margin-of-safety munger-inversion -a codex
```

```text
$investment-committee 用附件研究这家公司，先判断增长故事需要什么经营证据，
再审查现金、价格与失败路径。资料不足时先给缺口，不补假数字。
```

## 2. A 股交易复盘

**输入：**市场、当时规则、候选全集、事前计划、实际成交和费用。

**流程：**养家框架比较市场阶段假设 → 北京炒家框架重建候选到退出的事件链 →
退学炒股框架分开评价判断、执行与结果。历史复盘始终冻结当时可知信息。

**阶段产物：**竞争假设、事件表、行为时间线。
只有收盘 K 线时不重建盘口；只给精选赢家时不估总体成功率。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee yangjia-market-regime beijing-first-board-review tuixue-trading-journal -a codex
```

```text
$investment-committee 复盘附件交易记录：先恢复当时环境和计划，再看成交与退出，
最后区分策略证据不足和执行偏离。不要用后来的涨跌替代当时依据。
```

## 3. 组合审查

**输入：**持仓名称、权重、币种、费用、研究日期及资金使用期限。

**流程：**博格检查可保留收益与成本 → 达利欧框架穿透共同风险 →
马克斯框架描述永久损失与被迫退出的路径。

**阶段产物：**成本账、风险暴露表、压力路径。
缺权重时只定性；缺适当历史数据时不计算相关性和风险贡献。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee bogle-cost-discipline dalio-risk-budgeting marks-cycle-risk -a codex
```

```text
$investment-committee 审查这份匿名组合，检查成本和隐藏的共同风险。
先比较现状与我提供的备选方案，不自动填入新的配置比例。
```

## 4. 市场叙事

**输入：**一个主题、截至时点、市场数据、融资或经营变化及消息原文。

**流程：**索罗斯框架核查反馈链 → 马克斯框架比较预期与价格风险 →
养家框架保留市场状态的竞争解释。

**阶段产物：**反馈链、损失机制和假设卡。
只有价格上涨时不证明泡沫或因果；确认机制也不等于确定转折日期。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee soros-reflexivity marks-cycle-risk yangjia-market-regime -a codex
```

```text
$investment-committee 检查这个主题的“价格—融资—经营—预期”链条。
逐条找证据，列出共同外因和断点，不推断确定的见顶日期。
```

## 使用与安装范围

这些命令按 Skills CLI 的多技能参数格式安装到项目范围，客户端可换为 `claude-code`。
见 [官方参数](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。
技能名不同不代表它们的判断相互独立；顺序也不构成固定投资策略。
首次使用可从 [研究输入模板](../templates/research-brief.md) 开始。

