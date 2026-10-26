---
name: investment-committee
description: "按投资期限与研究问题选择合适的投资框架，比较证据、分歧和失效条件。用于多流派投资研究、持仓观点审查或不知道该用哪个 skill 的请求；不以人物投票生成买卖指令。"
---

# 投资研究委员会

这是维护者原创的研究编排流程。各人物 skill 依据公开材料整理，不扮演本人，
也不能据此推断其今天会买卖什么。先读 [来源与路由依据](references/sources.md)。

## 明确研究对象

确定市场、标的或组合、研究时点、持有期限、用户真正想回答的问题与现有材料。
缺少期限时，可以并列讨论长期与短期视角，但不可将两者合成一个交易结论。
只对影响当前判断的缺失项提问；其余部分先研究并标为待核实。
用户给出的“当前”日期与历史数据必须区分，不能把最新事实带回历史决策。

## 选择框架

先区分社区交易者、企业与组合投资者、交易流派的具体用途，不因人物都知名就视为同一类策略。
目录中 `kind: satire` 的技能仅供用户明确要求的娱乐，不能作为投研证据、反向信号或投票成员。
用户要同时看段子与研究时分别标明；段子中的原创情节不进入事实表。
`source-limited-workflow` 只代表转述材料启发的有限研究，引用时保留原始归属待核对的限制。

仅加载能回答当前问题的技能，通常先选一个主框架，再选一个反方框架。
下列技能若能被客户端发现，按名称调用；用户已授权读取本库时，也可按实际存在的路径
读取相应 SKILL.md 与按需参考资料，无需声称已安装。单独安装本技能时，不假定相邻文件存在；
缺少框架就说明对应目录，并独立输出研究问题与证据缺口。

| 问题 | 主框架 | 适合补充的反方视角 |
| --- | --- | --- |
| 一家公司值得长期研究吗 | buffett-business-quality | marks-cycle-risk：好公司是否已被高价反映 |
| 熟悉的产品能变成投资论点吗 | lynch-business-evidence | munger-inversion：观察偏差与失败路径 |
| 低估值是否是价值陷阱 | graham-margin-of-safety | buffett-business-quality：资产与经营是否在恶化 |
| 已有论点最可能错在哪里 | munger-inversion | 回到主框架验证反方，而非只列泛泛风险 |
| 热门叙事是否影响了基本面 | soros-reflexivity | marks-cycle-risk：价格与损失机制是否匹配 |
| 组合是否太贵、太复杂 | bogle-cost-discipline | dalio-risk-budgeting：成本低但风险是否集中 |
| 不同资产是否真的分散 | dalio-risk-budgeting | marks-cycle-risk：压力下相关性是否变化 |
| 是否受市场热度驱动 | marks-cycle-risk | tuixue-trading-journal：自身冲动与市场证据分开 |
| 首板交易复盘 | beijing-first-board-review | yangjia-market-regime：当时环境是否支持 |
| 下跌反弹如何研究 | yangjia-market-regime | tuixue-trading-journal：事前依据还是事后解释 |
| 交易为何反复偏离计划 | tuixue-trading-journal | 主策略的证据是否成立，而非全归因于心态 |
| 我真的懂这门生意吗 | duan-business-understanding | lilu-knowledge-boundary：结论能否独立重建 |
| 行业龙头便宜，还是价值陷阱 | qiu-competition-valuation | fengliu-visible-risk：承认悲观解释并核查存续 |
| 长期投入在创造价值吗 | zhanglei-value-creation | zhushaoxing-growth-governance：治理和每股价值是否兑现 |
| 产品刚需能转成利润吗 | linyuan-demand-substitution | fisher-scuttlebutt：替代与渠道材料是否独立 |
| 回购分红真的增加股东所得吗 | zhangkun-shareholder-cash | buffett-business-quality：现金持续性与资本需求 |
| 大产业趋势能支持这家公司吗 | danbin-secular-thesis | marks-cycle-risk：价格是否要求过度乐观 |
| 多份调研是否互相印证 | fisher-scuttlebutt | lilu-knowledge-boundary：共同来源与知识边界 |
| 跨市场的便宜是否可比 | templeton-global-comparison | dalio-risk-budgeting：是否存在共同暴露 |
| 质量和低价筛选是否可信 | greenblatt-quality-value-screen | graham-margin-of-safety：会计异常与价值陷阱 |
| 成长与突破证据是否一致 | oneil-growth-confirmation | lynch-business-evidence：经营假设是否真实 |
| 风险判断有没有落实到仓位 | zhiye-chaoshou-exposure-tempo | tuixue-trading-journal：规则不清还是执行偏离 |
| 已有交易依据什么时候消失 | niepan-decision-review | tuixue-trading-journal：事前记录与事后解释 |
| 题材延续、补涨还是切换 | kobe92-theme-rotation | yangjia-market-regime：保留竞争解释；前者来源受限 |
| 指数估值表能支持投入计划吗 | luosiding-index-valuation | etf-world-position-plan：资金边界与路径 |
| 缠论标注当时已经确认吗 | chanlun-structure-review | 检查规则版本、确认延迟与未来信息 |
| 打板是否买得到、能退出 | limit-up-execution-review | beijing-first-board-review：人物材料提供的有限主题 |
| 龙头是事前识别还是事后命名 | leader-relay-review | kobe92-theme-rotation：候选与阶段解释 |
| 低吸、反弹与反转有何区别 | pullback-rebound-review | marks-cycle-risk：继续恶化的路径 |
| 放量突破怎样验证 | trend-breakout-review | oneil-growth-confirmation：增长证据与价格证据分开 |
| 网格小赚但账户总亏为何发生 | grid-path-review | etf-world-position-plan：现金和仓位约束 |

## 取证与比较

1. 读取所选框架需要的材料；在线研究优先原始公告、财报、交易所、本人文章。
   记录数据时点、来源链接和缺失项。没有浏览或行情能力时只分析用户提供的数据。
2. 将每个关键判断写为“证据 → 推理 → 反证 → 尚缺资料”，区分事实、估计与假设。
   不输出未经校准的胜率、目标收益或人物拟真发言。
3. 分别写出各框架最强的支持意见和反对意见；不为了凑数强制所有框架表态。
4. 保留不同期限、目标和风险约束导致的分歧。企业经营质量、短线价格行为、
   个人执行纪律是不同问题，不把三项赞成汇总为置信度或买入票数。
5. 给出能使结论改变的可观察条件，说明未来应补什么证据。风控流程不能替代盈利验证。

## 输出

- 研究问题、时点、期限、使用的框架及选择原因。
- 一段可由证据支持的结论；证据不足时明确暂不能判断什么。
- 对照表：框架 / 核心判断 / 支持证据 / 最强反证 / 数据缺口。
- 分歧来自哪里、哪些问题可以补证解决、哪些属于不同投资目标。
- 后续核查清单及改变结论的条件。

如用户要求当前投资配置或买卖建议，进一步了解影响建议的期限、流动性与风险约束；
在没有这些信息时只提供条件化分析。研究输出不扩展为账户操作、资金托管或下单授权。

