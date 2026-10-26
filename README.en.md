<p align="center"><img src="assets/cover.svg" alt="Investing Skills" width="100%"></p>

# Investing Skills

**Investment thinking, distilled into source-backed agent skills.**

[中文](README.md) · [Skill catalog](#skills) · [Examples](examples/README.md) · [Contribute](CONTRIBUTING.md)

Turn public investment ideas into repeatable research workflows for AI agents.
The library contains **39 skills: 29 investor frameworks, 6 trading schools, 3 original entertainment modes, and 1 research router**, covering business quality,
portfolio costs, cycles, diversification, Chinese business research, and A-share trading review.
The research catalog includes 17 frameworks associated with Chinese markets and Chinese investors, and 12 international frameworks.
Community trading, index investing, trading schools and opt-in humor have separate discovery tracks.
Skill instructions and examples are currently written in Chinese; an agent can respond in your preferred language.

Each workflow connects **inputs → evidence → reasoning → counterarguments → a reviewable output**.
Source notes distinguish the investor's public statements from the maintainer's operational interpretation.
The project is independently written and is not endorsed by the named investors or their organizations.

Try the [community map](docs/COMMUNITY_MAP.md), the [six trading schools](docs/PLAYBOOKS.md#8-交易流派), or the [original meme clinic](examples/meme-clinic.md). Humor is not treated as investment evidence.

## Start with a task

| Task | Optional frameworks | Output |
| --- | --- | --- |
| Company diligence | Lynch → Buffett → Graham → Munger | Business evidence, valuation assumptions, failure paths |
| Trading review | Yangjia → Beijing → Tuixue | Market hypotheses, execution events, plan deviations |
| Portfolio review | Bogle → Dalio → Marks | Costs, common exposures, loss mechanisms |
| Market narrative | Soros → Marks → Yangjia | Feedback links, competing causes, breakpoints |
| Chinese business / contrarian research | Duan → Qiu → Feng → Zhang Kun | Knowledge boundaries, value traps, shareholder cash |
| Growth cross-check | Lynch → Fisher → Zhang Lei → O’Neil | Growth mechanisms, evidence conflicts, execution limits |

Use only the stages relevant to your question. The [playbooks](docs/PLAYBOOKS.md) include installation
commands and prompts. Start with the [research brief](templates/research-brief.md) when preparing inputs.

## Quick start

Using the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add superShen0916/investing-skills
npx skills add superShen0916/investing-skills --skill buffett-business-quality -a codex
npx skills add superShen0916/investing-skills --list
```

Or copy a complete skill directory, including its references, into:

| Client | Project scope | User scope |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

See [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills),
[Claude Code docs](https://code.claude.com/docs/en/skills), and the [Agent Skills specification](https://agentskills.io/specification).
CLI project installation for Codex and Claude Code was checked in isolated directories. Full runtime behavior has not been tested across every client.

In Codex:

```text
$buffett-business-quality Review this annual report for cash generation and capital allocation.
$tuixue-trading-journal Separate execution mistakes from strategy problems in this journal.
$investment-committee Compare long-term business quality with the short-term trading thesis.
```

Claude Code uses `/skill-name`. Install the relevant specialist skills alongside the committee skill.
Browsing, data access, and calculation tools come from the host agent. Offline review works with supplied materials.

## Skills

**39 skills: 29 investor frameworks, 6 trading schools, 3 original entertainment modes, and 1 router.**

The Kobe92 framework is source-limited. Entertainment is explicitly typed and excluded from research packs.
See the [community map](docs/COMMUNITY_MAP.md), [playbooks](docs/PLAYBOOKS.md), [humor demos](examples/meme-clinic.md), and [source coverage](docs/SOURCE_COVERAGE.md).

### TGB and short-term trading communities

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [tuixue-trading-journal](skills/tuixue-trading-journal/SKILL.md) | 退学炒股 | Trading impulses, plan deviations, review |
| [beijing-first-board-review](skills/beijing-first-board-review/SKILL.md) | 北京炒家 | First-limit-up candidates, execution assumptions, exits |
| [yangjia-market-regime](skills/yangjia-market-regime/SKILL.md) | 炒股养家 | Market-stage hypotheses, competing explanations |
| [zhiye-chaoshou-exposure-tempo](skills/zhiye-chaoshou-exposure-tempo/SKILL.md) | 职业炒手 (Zhiye Chaoshou) | Exposure, trading tempo and drawdown review |
| [niepan-decision-review](skills/niepan-decision-review/SKILL.md) | 涅盘重升 (Niepan) | Decision and exit review |
| [kobe92-theme-rotation](skills/kobe92-theme-rotation/SKILL.md) | 92科比 (Kobe92), secondary sources | Theme rotation; source-limited |

### Xueqiu and index-investing communities

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [luosiding-index-valuation](skills/luosiding-index-valuation/SKILL.md) | 银行螺丝钉 (Luosiding) | Index valuation and implementation |
| [etf-world-position-plan](skills/etf-world-position-plan/SKILL.md) | ETF拯救世界 (E Da) | Capital planning and rebalancing |

### Trading schools

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [chanlun-structure-review](skills/chanlun-structure-review/SKILL.md) | Chan theory | Structures, levels and confirmation time |
| [limit-up-execution-review](skills/limit-up-execution-review/SKILL.md) | Limit-up trading | Board events, queueing and executable exits |
| [leader-relay-review](skills/leader-relay-review/SKILL.md) | Leader and relay trading | Ex-ante leadership and failed relays |
| [pullback-rebound-review](skills/pullback-rebound-review/SKILL.md) | Pullbacks and rebounds | Reference levels and downside budgets |
| [trend-breakout-review](skills/trend-breakout-review/SKILL.md) | Trend breakouts | Signal timing, volume and execution |
| [grid-path-review](skills/grid-path-review/SKILL.md) | Grid trading | Inventory, cash and total-account outcomes |

### Meme clinic: original entertainment

Opt-in only. Jokes are original, not quotations or impersonations. “Sunge” refers to Justin Sun here.

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [fengge-fomo-roast](skills/fengge-fomo-roast/SKILL.md) | Fengge-inspired humor | Original FOMO-cycle jokes |
| [huchenfeng-brand-roast](skills/huchenfeng-brand-roast/SKILL.md) | Huchenfeng-inspired humor | Original brand-versus-valuation jokes |
| [justin-sun-headline-roast](skills/justin-sun-headline-roast/SKILL.md) | Justin Sun-inspired humor | Original headline-versus-value jokes |

### Business, value and institutional frameworks

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [duan-business-understanding](skills/duan-business-understanding/SKILL.md) | Duan Yongping | Business understanding and culture |
| [lilu-knowledge-boundary](skills/lilu-knowledge-boundary/SKILL.md) | Li Lu | Knowledge boundaries and independent judgment |
| [zhanglei-value-creation](skills/zhanglei-value-creation/SKILL.md) | Zhang Lei | Long-term investment and value creation |
| [qiu-competition-valuation](skills/qiu-competition-valuation/SKILL.md) | Qiu Guolu | Competition, quality and valuation |
| [fengliu-visible-risk](skills/fengliu-visible-risk/SKILL.md) | Feng Liu | Visible risks and contrarian research |
| [linyuan-demand-substitution](skills/linyuan-demand-substitution/SKILL.md) | Lin Yuan | Demand persistence and substitution |
| [danbin-secular-thesis](skills/danbin-secular-thesis/SKILL.md) | Dan Bin | Secular trends and shareholder returns |
| [zhangkun-shareholder-cash](skills/zhangkun-shareholder-cash/SKILL.md) | Zhang Kun / E Fund disclosures | Cash generation, distributions and dilution |
| [zhushaoxing-growth-governance](skills/zhushaoxing-growth-governance/SKILL.md) | Zhu Shaoxing / Fullgoal disclosures | Growth quality, governance and price |

### International investor frameworks

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [buffett-business-quality](skills/buffett-business-quality/SKILL.md) | Warren Buffett | Business quality, cash generation, valuation assumptions |
| [bogle-cost-discipline](skills/bogle-cost-discipline/SKILL.md) | John C. Bogle | Costs, diversification, holding discipline |
| [marks-cycle-risk](skills/marks-cycle-risk/SKILL.md) | Howard Marks | Cycles, sentiment, permanent loss |
| [dalio-risk-budgeting](skills/dalio-risk-budgeting/SKILL.md) | Ray Dalio / Bridgewater | Risk concentration, growth and inflation scenarios |
| [munger-inversion](skills/munger-inversion/SKILL.md) | Charlie Munger | Inversion, incentives, failure paths |
| [graham-margin-of-safety](skills/graham-margin-of-safety/SKILL.md) | Benjamin Graham | Valuation room, asset quality, value traps |
| [lynch-business-evidence](skills/lynch-business-evidence/SKILL.md) | Peter Lynch | Turn product observations into business evidence |
| [soros-reflexivity](skills/soros-reflexivity/SKILL.md) | George Soros | Belief–behavior–fundamental feedback |
| [fisher-scuttlebutt](skills/fisher-scuttlebutt/SKILL.md) | Philip A. Fisher | Multi-source business research |
| [templeton-global-comparison](skills/templeton-global-comparison/SKILL.md) | John Templeton | Global value comparisons and real returns |
| [greenblatt-quality-value-screen](skills/greenblatt-quality-value-screen/SKILL.md) | Joel Greenblatt | Quality/value screening and data integrity |
| [oneil-growth-confirmation](skills/oneil-growth-confirmation/SKILL.md) | William J. O’Neil | Growth and price/volume confirmation |

### Research routing

| Skill | Public framework / type | Task |
| --- | --- | --- |
| [investment-committee](skills/investment-committee/SKILL.md) | Maintainer-authored | Route questions, compare evidence, preserve disagreements |

Community identities and professional roles can overlap. Grouping is for discovery, not ranking or endorsement.

Tools can read [skills-index.json](skills-index.json), generated from the catalog and actual skill metadata.
It is this repository's lightweight index, not proof of third-party registry inclusion.

## Examples and evidence

Read the [multi-framework review](examples/multi-framework-review.md) and
[trading-journal review](examples/trading-journal-review.md).
These are fictional, manually authored demonstrations, not model evaluations or investment results.

A [single independent offline agent execution](docs/evaluations/2026-10-26-committee.md) is also recorded.
It documents one behavior observation, not repeated reliability or investment performance.

[Six reproducible behavior cases](evals/README.md) cover value traps, causal claims, historical cutoffs,
and disagreement. These are prompts and rubrics, not executed pass-rate results.

Every skill includes `references/sources.md` with original URLs, dates, and attribution limits.
An authentic source does not validate an investment strategy. Research workflows have no verified investment performance;
entertainment modes are original creative content, not strategies. See the [methodology](docs/METHODOLOGY.md).

## Validate and contribute

The skills themselves have no code-runtime dependency. Maintainer checks require Python 3.10+:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build_index.py --check
.venv/bin/python -m unittest discover -s tests -v
```

Checks cover manifests, catalog consistency, source records, and local links. They do not verify
external URL availability, client-runtime compatibility, or investment performance.

Contributions are welcome: original sources, counterexamples, observed failures, translations,
and new frameworks. See [CONTRIBUTING](CONTRIBUTING.md).

Related projects: [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund),
[Buffett Skills](https://github.com/agi-now/buffett-skills),
[Claude Trading Skills](https://github.com/tradermonty/claude-trading-skills).

## Scope and license

This is a research-workflow preview. It does not accept funds, manage accounts, execute transactions,
guarantee returns, or reproduce an investor's private decision-making ability.

Original repository content is [MIT licensed](LICENSE). Linked third-party works retain their original rights;
see [NOTICE](NOTICE.md).

