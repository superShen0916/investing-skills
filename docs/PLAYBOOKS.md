# 从任务开始：九种研究入口与一个娱乐包

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

可用职业炒手框架补查风险判断是否真正落实到仓位与交易节奏。

**阶段产物：**竞争假设、事件表、行为时间线与暴露复盘。
只有收盘 K 线时不重建盘口；只给精选赢家时不估总体成功率。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee yangjia-market-regime beijing-first-board-review tuixue-trading-journal zhiye-chaoshou-exposure-tempo -a codex
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

## 5. 中国企业质量与逆向研究

**输入：**公司业务解释、竞争格局、价格与负面事实时间线、财报和现金分配资料。

**流程：**段永平框架检查是否懂生意 → 邱国鹭框架交叉审竞争与价格 →
若论点依赖大跌后恢复，用冯柳框架承认悲观解释并研究存续 → 张坤框架追现金到股东。

**阶段产物：**理解边界、正常化盈利、已呈现与未解除风险、股东现金桥。
不要求每个框架都同意；恢复能力不清时，不因低估值继续推出价格结论。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee duan-business-understanding qiu-competition-valuation fengliu-visible-risk zhangkun-shareholder-cash -a codex
```

```text
$investment-committee 这家公司跌了很多，我认为只是市场悲观。请先检查我是否懂它的生意，
再审竞争、估值和最强悲观解释，最后核查现金能否回到股东。保留价值陷阱的可能性。
```

## 6. 成长与趋势交叉检查

**输入：**增长故事、产品资料、已获授权使用的调查记录、长期投入、价格成交与事前候选。

**流程：**林奇框架拆增长 → 费雪框架设计交叉核实 → 张磊框架查投入是否创造价值 →
仅当问题涉及价格与交易时，用欧奈尔框架审查事前候选、价量与成交限制。
若核心疑问是产业方向，可改用但斌框架区分趋势、公司和价格三个命题。

**阶段产物：**可推翻的成长假设、材料角色图、投入结果链、价格证据与执行缺口。
设计调查不代表已经访谈；增长成立不代表适合追涨。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee lynch-business-evidence fisher-scuttlebutt zhanglei-value-creation oneil-growth-confirmation -a codex
```

```text
$investment-committee 请检查这家热门成长公司的论点：把增长故事转成假设，
核查不同角色的材料是否独立、长期投入是否兑现价值，再单独讨论价量证据。
缺事前候选与真实成交资料时，不声称已验证突破策略。
```

## 7. 社区人物

**输入：**自己的交易经历、事前计划和当时可知的市场资料。先选人物关注的问题，
再决定要补哪些研究步骤；不要求给所有社区人物逐个投票。

**可选流程：**养家看环境 → 北京炒家看首板事件 → 涅盘重升看依据怎样失效 →
职业炒手看暴露与节奏 → 退学炒股看计划偏离。

新增五个可选入口：赵老哥看回封多了什么信息，asking看为什么排除机会，
瑞鹤仙看卖飞与正常遗憾，龙飞虎看分仓滚动的盘中暴露，陈小群看事件与板块共振。
这五项和92科比目前均来源受限，引用时保留这一说明；不需要把11个人全部调用一遍。

```bash
npx skills add superShen0916/investing-skills --skill investment-committee yangjia-market-regime beijing-first-board-review niepan-decision-review zhiye-chaoshou-exposure-tempo tuixue-trading-journal kobe92-theme-rotation zhao-reseal-selection asking-opportunity-filter ruihexian-execution-regret longfeihu-rolling-exposure chenxiaoqun-theme-consensus -a codex
```

```text
$investment-committee 请按社区交易者框架复盘这份日志，只选与问题相关的两种方法。
先恢复当时环境，再看依据何时消失；引用转帖材料时不要冒充本人原文。
$zhao-reseal-selection 比较附件里首次封板、开板和回封时的已知信息，检查实际买得到吗。
$longfeihu-rolling-exposure 用这份成交记录列新老仓与可卖量，找出盘中暴露最高的时刻。
```

雪球的企业、基金与量化入口见下方第10节。
人物身份与补源方向见[社区地图](COMMUNITY_MAP.md)。

## 8. 交易流派

**输入：**证券、研究时点、价量／盘口、已有规则与实际成交。先声明想研究的流派。

| 流派 | 主技能 | 最关键的核查 |
| --- | --- | --- |
| 缠论 | chanlun-structure-review | 级别、规则版本、结构端点与实际确认时间 |
| 打板 | limit-up-execution-review | 触发、排队、实际成交与隔日退出 |
| 龙头战法 | leader-relay-review | 当时的完整候选梯队，是否事后才叫龙头 |
| 低吸 | pullback-rebound-review | 相对哪个参照算低，继续下跌怎么办 |
| 趋势突破 | trend-breakout-review | 盘中触及与收盘确认，最早可交易时刻 |
| 网格 | grid-path-review | 资金、库存与总资产，不能只看配对小赚 |

```bash
npx skills add superShen0916/investing-skills --skill investment-committee chanlun-structure-review limit-up-execution-review leader-relay-review pullback-rebound-review trend-breakout-review grid-path-review -a codex
```

```text
$chanlun-structure-review 按我附上的规则版本，复核这份截至某时刻的标注。
分别列端点时间和实际确认时间，不使用后来的K线。
$limit-up-execution-review 检查这份打板回测，把封板、成交、扣费盈利的分母分别列出。
$grid-path-review 检查这张网格交易表，分别核算配对利润、期末浮亏和总资产。
```

## 9. 梗股学（原创娱乐）

**输入：**用户明确要求玩梗、写搞笑文案或轻度吐槽；不需要强制提交研究资料。
孙宇晨用于热搜与价值的反差，峰哥用于清仓踏空追回的循环，户晨风用于品牌标签与估值的反差。
所有示例均为项目原创，不是本人语录或投资方法。

```bash
npx skills add superShen0916/investing-skills --skill justin-sun-headline-roast fengge-fomo-roast huchenfeng-brand-roast -a codex
```

```text
$fengge-fomo-roast 用这段虚构交易经历整两句活，再给一个可核查的问题。
```

见[三个原创演示](../examples/meme-clinic.md)。娱乐包有显式用途标记，不能混入研究包，
研究委员会也不把段子当支持意见或反向信号。

## 10. 雪球社区：财报、基金与量化

**输入：**按当前问题提供财报、基金资金流水、指数资料或策略回测记录，选一种主任务。

| 当前问题 | 可选入口 | 产物 |
| --- | --- | --- |
| 企业利润是否真实、可持续、需要再投入 | 唐朝 | 利润现金桥与估值前提；第三方问答整理，来源受限 |
| 基金涨了很多，我却没赚多少 | 望京博格 | 基金业绩、资金流与实际收益对照 |
| 量化曲线漂亮，是否调参过度 | 持有封基 | 数据时点、调参污染、未见样本与摩擦审查 |
| 指数便宜是否可据此投入 | 银行螺丝钉 | 估值口径与资金消耗 |
| 定投、分份、再平衡如何执行 | ETF拯救世界 | 现金边界与仓位路径 |

```bash
npx skills add superShen0916/investing-skills --skill investment-committee tangchao-profit-cash-check wangjing-investor-return chiyou-quant-validation luosiding-index-valuation etf-world-position-plan -a codex
```

```text
$tangchao-profit-cash-check 查附件财报：利润、经营现金、维持经营的再投入对得上吗？先列疑点。
$wangjing-investor-return 用我的申赎流水核对实际盈亏，再检查拿来比较的基金收益是否同口径。
$chiyou-quant-validation 这份策略在所谓样本外又调过两次参数，还能叫样本外吗？先审证据再谈收益。
```

这个包提供不同研究入口，不将人物的观点或收益相加为盈利概率。

## 使用与安装范围

这些命令按 Skills CLI 的多技能参数格式安装到项目范围，客户端可换为 `claude-code`。
见 [官方参数](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。
技能名不同不代表它们的判断相互独立；顺序也不构成固定投资策略。
首次使用可从 [研究输入模板](../templates/research-brief.md) 开始。

