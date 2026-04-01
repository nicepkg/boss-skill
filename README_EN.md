<div align="center">

# Boss.skill

> *"Tell HR to let the boss know — he's been optimized by AI too."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Your boss said "this feature is simple" and gave you two days?<br>
Your boss said "think bigger" and sat on your raise request for three months?<br>
Your boss said "we're a family" and then made you sleep at the office?<br>
Your boss said "AI can't replace humans" and then used AI to lay off half the team?<br>

**He fired you? No worries. AI can fire him.**

<br>

Describe your boss in one sentence → generate a dedicated AI stand-in<br>
**16 practical modes**: PUA detection · counterattack coach · cake-promise BS meter · evidence collector · labor law lookup · report optimizer · boss psychology predictor<br>
Fun on the outside, **seriously protecting workers** on the inside

[Features](#features) · [Quick Start](#quick-start) · [Install](#install) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

</div>

---

### Sister Projects

> - [Colleague.skill](https://github.com/titanwings/colleague-skill) — colleague left? use this
> - [Ex.skill](https://github.com/therealXiaomanChu/ex-skill) — ex left? use this
> - **Boss.skill** — sick of your boss? use this
>
> Cyber immortality, end to end — no one escapes 🌟

---

## Features

### The Worker's Full Journey: Vent → See Clear → Fight Back → Move On

**Layer 1: Diagnose (what's really going on)**

| Mode | Command | Description |
|------|---------|-------------|
| **PUA Detect** | `/boss-name pua` | 14 tactics + 10 corp flavor classification + victim profiling |
| **Cake Check** | `/boss-name cake` | 5-dimension BS meter for boss promises |

**Layer 2: Arm Up (learn to fight back)**

| Mode | Command | Description |
|------|---------|-------------|
| **Counterattack** | `/boss-name fight` or type **草** | 3-level tactics: safe / subtle shade / nuclear |
| **Evidence** | `/boss-name evidence` | Structured incident logging for labor arbitration |
| **Labor Law** | `/boss-name law` | Boss behavior → law article → rights → action path |
| **Salary Sim** | `/boss-name raise` | Practice negotiation, AI breaks down every rejection |
| **Boss Predictor** | `/boss-name predict` | Pre-meeting: predict boss mood, landmines, sweet spots |
| **Report Optimizer** | `/boss-name report` | Rewrite your report in boss's favorite jargon |
| **1v1 Simulator** | `/boss-name 1v1` | Practice tough conversations with real-time coaching |

**Layer 3: Move On (ready to leave)**

| Mode | Command | Description |
|------|---------|-------------|
| **Karma Game** | `/boss-name 翻车` | Interactive text adventure — watch the boss crash after layoffs |
| **Quit Script** | `/boss-name quit` | Personalized resignation script based on boss personality |
| **Replacement** | `/boss-name replace` | Generate "Boss Replaced by AI" announcement (for fun) |

**Base Modes**

| Mode | Command | Description |
|------|---------|-------------|
| **Full Chat** | `/boss-name` | Chat with AI boss, perfect replica of style and decisions |
| **Meeting Sim** | `/boss-name meeting` | Simulate boss meetings: overtime, off-topic, "let's take this offline" |
| **Ghostwriter** | `/boss-name delegate` | Middle managers: AI writes progress nudges so you don't have to be the bad guy |

### "草" — The Shortest Command in History

In **any mode**, type **草** (Chinese expletive) to trigger counterattack mode.

This isn't a designed interaction — it's a worker's instinct. When the AI boss says that thing you've heard a thousand times, your first reaction is "草". We just caught it.

Three levels:
- 🟢 **Workplace Safe** — professional, no risk, can't be used against you
- 🟡 **Subtle Shade** — technically correct, but the angle stings
- 🔴 **Nuclear** — for when you've already decided to leave

### 10 Corporate PUA Flavor Classification

Every PUA is analyzed and classified by corporate school:

🟠 Blessing Factory (soul interrogation) · 🟡 Universe Factory (radical candor as weapon) · 🔴 Chrysanthemum Factory (wolf culture) · 🟢 Goose Factory (internal horse race) · 🔵 Delivery Factory (extreme execution) · ⚫ Search Factory (competence denial) · 🟣 Slash Factory (absolute obedience) · 🟤 N-Corp (Keeper Test) · ⬛ Mars Boss (Hardcore) · ⬜ Fruit Guru (A/B Player)

---

## Quick Start (30 seconds)

```bash
# Create 3 pre-built demo bosses instantly
python3 <this-skill-dir>/tools/create_boss.py --demo --skills-dir <your-skills-dir>
```

Then try:
```
/王总 pua "You're talented but your attitude needs work"
/王总 fight
/刘姐 cake "Hit our targets and I'll take everyone to Sanya"
/张总 翻车
```

---

## Install

```bash
git clone https://github.com/nicepkg/boss-skill <your-skills-dir>/create-boss
```

## Usage

### Step 1: Create a Boss

```
/create-boss
```

Enter boss codename (e.g. "Boss Wang"), industry/title, management style tags, catchphrases.

All fields are optional — **one sentence is enough**. Supports multiple bosses.

### Step 2: Use the Boss

Each boss becomes its own skill. Subcommands use **spaces**, not hyphens:

```
/Boss-Wang              chat with AI boss
/Boss-Wang pua          PUA detection
/Boss-Wang 翻车         interactive text game
/Boss-Wang fight        counterattack coach
```

### Commands

| Command | Description |
|---------|-------------|
| `/boss-name` | Chat with AI boss |
| `/boss-name pua` | PUA detection (10 flavors + victim profiling) |
| `/boss-name cake` | Cake-promise BS meter (5 dimensions) |
| `/boss-name fight` or **草** | Counterattack coach (3 levels) |
| `/boss-name evidence` | Evidence collector (structured → arbitration timeline) |
| `/boss-name law` | Labor law lookup (behavior → law → rights) |
| `/boss-name raise` | Salary negotiation sim |
| `/boss-name predict` | Boss psychology predictor |
| `/boss-name report` | Report optimizer (rewrite in boss jargon) |
| `/boss-name 1v1` | 1v1 meeting simulator with coaching |
| `/boss-name delegate` | Ghostwriter for middle managers |
| `/boss-name meeting` | Meeting simulator |
| `/boss-name 翻车` | Karma game (interactive text adventure) |
| `/boss-name quit` | Resignation script |
| `/boss-name replace` | "Boss Replaced by AI" notice |
| `/fire-boss name` | "Fire" the boss (delete skill) |

---

## Examples

> Input: `Tech company VP, ESTJ, micromanager, empty promise king, loves saying "think bigger"`

**PUA Detection + Flavor Classification**:
```
You    ❯ Boss said "You're talented but your attitude needs work,
          look at Tom, less skilled but great attitude"

AI     ❯ 🚨 PUA Score: 85/100

          ━━━ Breakdown ━━━
          ✦ Praise-then-criticize    "talented but..."
          ✦ Fabricated comparison     "Tom from the other team"
          ✦ Vague criteria           "attitude" is unmeasurable
          ✦ Guilt induction          makes you feel it's your fault

          ━━━ Flavor ━━━
          🏷️ Primary: 🟠 Blessing Factory PUA (soul interrogation)

          ━━━ Your State ━━━
          📊 Victim type: Awakening Fighter
          You came here to check — that's already the first step.

          ━━━ Translation ━━━
          He doesn't want to promote you but won't give a real reason.

          💡 Type 草 to learn how to fight back
```

**Counterattack (type "草")**:
```
You    ❯ 草

AI     ❯ He said "think bigger, 3 days max."

          🟢 Workplace Safe:
          "Sure, 3 days works if we cut features X and Y.
           Which ones should we prioritize?"
          → Turns unreasonable deadline into HIS trade-off decision

          🟡 Subtle Shade:
          "3 days no problem. Should QA time come from dev or testing?
           Or skip testing? I'll note that in the meeting minutes."
          → Makes him say "skip testing" on record

          🔴 Nuclear:
          "2 weeks includes integration and testing. 3 days gets a demo.
           Production issues — who's accountable? I need that in email."
          → Asking for written confirmation = he won't sign = deadline resets
```

**Karma Game (Interactive Text Adventure)**:
```
You    ❯ /Boss-Wang 翻车

AI     ❯ 🎬 Karma Simulator v1.0

          ━━━ Act 1: Calm Before the Storm ━━━

          【Narrator】
          Day 3 after layoffs. Boss posted on social media:
          "Team is leaner and more efficient than ever" with latte art.

          📅 Day 3 | 💰 Loss ¥0 | 😰 Panic 5/100

          ━━━ Act 2: The Phone Rings ━━━

          【Client Zhang】
          "Where's Li? I've been calling for 3 days. What?
           He's gone? Then who handles my project?"

          📅 Day 6 | 💰 Loss ¥0 | 😰 Panic 35/100

          What do you do?
          [A] 😏 Post "beautiful weather today" on social media
          [B] 🍿 Keep watching
          [C] 📱 Forward boss's latte post to the ex-colleague group
```

---

## Data Sources

### Recommended Chat Export Tools

| Tool | Platform | Description |
|------|----------|-------------|
| [WeChatMsg](https://github.com/LC044/WeChatMsg) | Windows | WeChat chat export |
| [PyWxDump](https://github.com/xaoyaoo/PyWxDump) | Windows | WeChat database decryptor |
| [留痕](https://github.com/greyovo/留痕) | macOS | WeChat export for Mac |

> No export tools needed! Screenshots, descriptions, or copy-paste all work.

---

## Project Structure

```
create-boss/
├── SKILL.md              # Skill entry point
├── references/
│   ├── prompts/          # 19 prompt templates
│   └── guides/           # Creation guides + generated skill spec
├── examples/             # 3 pre-built bosses (instant demo)
├── tools/
│   ├── create_boss.py    # Core generator script
│   ├── email_parser.py   # Email parser
│   └── version_manager.py
└── docs/PRD.md
```

---

## Disclaimer

For **personal entertainment, emotional relief, career skill training, and legal rights protection** only.

- Generated "replacement notices" are fictional
- Labor law lookup is reference only — consult a real lawyer
- Evidence collector helps organize personal experiences, not legal advice
- If your boss is actually great, treasure them (they're rare these days)

---

## Credits

Inspired by:

- [Colleague.skill](https://github.com/titanwings/colleague-skill) by [@titanwings](https://github.com/titanwings) — pioneer of "distill a person into AI Skill"
- [Ex.skill](https://github.com/therealXiaomanChu/ex-skill) by [@therealXiaomanChu](https://github.com/therealXiaomanChu) — extended the concept from workplace to relationships
- [PUA.skill](https://github.com/tanweai/pua) by [@tanweai](https://github.com/tanweai) — PUA detection trailblazer

---

## Star History

<a href="https://www.star-history.com/?repos=nicepkg%2Fboss-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=nicepkg/boss-skill&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=nicepkg/boss-skill&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=nicepkg/boss-skill&type=date&legend=top-left" />
 </picture>
</a>

---

<div align="center">

MIT License © [nicepkg](https://github.com/nicepkg)

**Like it? Star it, and let more workers see this 🌟**

</div>
