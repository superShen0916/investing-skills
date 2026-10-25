<p align="center"><img src="assets/cover.svg" alt="Investing Skills" width="100%"></p>

# Investing Skills

**Investment thinking, distilled into source-backed agent skills.**

[中文](README.md) · [Skill catalog](#skills) · [Examples](examples/README.md) · [Contribute](CONTRIBUTING.md)

Turn public investment ideas into repeatable research workflows for AI agents.
The library contains **12 skills, including 11 investor-inspired frameworks and 4 task playbooks**, covering business quality,
portfolio costs, cycles, diversification, and Chinese A-share trading review.
Skill instructions and examples are currently written in Chinese; an agent can respond in your preferred language.

Each workflow connects **inputs → evidence → reasoning → counterarguments → a reviewable output**.
Source notes distinguish the investor's public statements from the maintainer's operational interpretation.
The project is independently written and is not endorsed by the named investors or their organizations.

## Start with a task

| Task | Optional frameworks | Output |
| --- | --- | --- |
| Company diligence | Lynch → Buffett → Graham → Munger | Business evidence, valuation assumptions, failure paths |
| Trading review | Yangjia → Beijing → Tuixue | Market hypotheses, execution events, plan deviations |
| Portfolio review | Bogle → Dalio → Marks | Costs, common exposures, loss mechanisms |
| Market narrative | Soros → Marks → Yangjia | Feedback links, competing causes, breakpoints |

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

| Skill | Public framework | Task |
| --- | --- | --- |
| [investment-committee](skills/investment-committee/SKILL.md) | Maintainer-authored | Route questions, compare evidence, preserve disagreements |
| [buffett-business-quality](skills/buffett-business-quality/SKILL.md) | Warren Buffett | Business quality, cash generation, valuation assumptions |
| [bogle-cost-discipline](skills/bogle-cost-discipline/SKILL.md) | John C. Bogle | Costs, diversification, holding discipline |
| [marks-cycle-risk](skills/marks-cycle-risk/SKILL.md) | Howard Marks | Cycles, sentiment, permanent loss |
| [dalio-risk-budgeting](skills/dalio-risk-budgeting/SKILL.md) | Ray Dalio / Bridgewater | Risk concentration, growth and inflation scenarios |
| [tuixue-trading-journal](skills/tuixue-trading-journal/SKILL.md) | 退学炒股 | Trading impulses, plan deviations, review |
| [beijing-first-board-review](skills/beijing-first-board-review/SKILL.md) | 北京炒家 | First-limit-up candidates, execution assumptions, exits |
| [yangjia-market-regime](skills/yangjia-market-regime/SKILL.md) | 炒股养家 | Market-stage hypotheses, competing explanations |
| [munger-inversion](skills/munger-inversion/SKILL.md) | Charlie Munger | Inversion, incentives, failure paths |
| [graham-margin-of-safety](skills/graham-margin-of-safety/SKILL.md) | Benjamin Graham | Valuation room, asset quality, value traps |
| [lynch-business-evidence](skills/lynch-business-evidence/SKILL.md) | Peter Lynch | Turn product observations into business evidence |
| [soros-reflexivity](skills/soros-reflexivity/SKILL.md) | George Soros | Belief–behavior–fundamental feedback |

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
An authentic source does not validate an investment strategy. All current skills are research workflows
without verified investment performance. See the [methodology](docs/METHODOLOGY.md).

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

