<div align="center">

# Boss.skill

> *"I can be laid off, but you can't be irreplaceable."*
> *—— Every Worker Ever*

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

Provide your boss's catchphrases, management quirks, and meeting habits<br>
Generate an **AI Boss** — perfectly replicating their empty promises, blame-shifting, and micromanagement<br>
Then watch AI make decisions in 0.001 seconds that took your boss three days

[Features](#features) · [Install](#install) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

</div>

---

## Features

### Six Modes

| Mode | Command | Description |
|------|---------|-------------|
| **Full** | `/{boss-name}` | Chat with your AI boss in their style |
| **Meeting** | `/{boss-name}-meeting` | Simulate their meeting style: overtime, off-topic, "let's take this offline" |
| **PUA Detect** | `/{boss-name}-pua` | Analyze boss quotes for manipulation tactics (0-100 score) |
| **Cake Check** | `/{boss-name}-cake` | Rate boss's promises on a "BS meter" (0-100 score) |
| **Raise Sim** | `/{boss-name}-raise` | Practice salary negotiation against AI boss |
| **Replace** | `/{boss-name}-replace` | Generate "Boss Replaced by AI" announcement (for fun) |

### Tags

**Management Style**: Micromanager · Empty Promise King · Blame Shifter · Flip-Flopper · Results Only · Wants Everything · Meeting Addict · Email Bomber · KPI Tyrant · PPT Warrior ...

**Catchphrase Templates**:
- "This feature is simple" · "Think bigger" · "When I was your age..."
- "We're a family here" · "Next time, be careful" · "Own this"
- "Top performers are always hustling" · "The company had a tough year"

---

## Install

```bash
git clone https://github.com/nicepkg/boss-skill <your-skills-dir>/create-boss
```

## Usage

```
/create-boss
```

Follow prompts to input boss codename, industry/title, management style tags, and catchphrases.

### Management Commands

| Command | Description |
|---------|-------------|
| `/list-bosses` | List all boss Skills |
| `/fire-boss {boss-name}` | "Fire" your boss (delete Skill) |
| `/boss-rollback {boss-name} {version}` | Rollback to previous version |

---

## Examples

> Input: `Tech company VP, ESTJ, micromanager, empty promise king, loves saying "think bigger"`

**PUA Detection**:
```
You    ❯ My boss said "You're talented but your attitude needs work,
          look at Tom from the other team, less skilled but great attitude"

AI     ❯ 🚨 PUA Score: 85/100

          Breakdown:
          ✦ Praise-then-criticize    "talented but..."
          ✦ Fabricated comparison     "Tom from the other team"
          ✦ Vague criteria           "attitude" is unmeasurable
          ✦ Guilt induction          makes you feel it's your fault

          Translation: He doesn't want to promote you
          but doesn't want to give a real reason.
```

**Replacement Notice**:
```
          📢 Important Personnel Announcement

          Following evaluation by the AI Transformation Committee,
          {Boss}'s management duties have been fully assumed by AI.

          The AI system will maintain their management style:
          ✓ Extending every meeting by 15 minutes
          ✓ Saying "didn't we agree on this?" after changing requirements
          ✓ Sending "can this ship today?" at 5:55 PM on Fridays

          However, the AI system:
          ✗ Will not schedule meetings during lunch
          ✗ Will not say "the company had a tough year" during reviews
          ✗ Will not want everything while providing nothing

          Cost optimization starts from management.
```

---

## Disclaimer

This project is for **personal entertainment, emotional relief, and career skill training** only.

- Do not send generated content to your actual boss (unless you're quitting)
- "Replacement notices" are fictional
- If your boss is actually great, treasure them (they're rare these days)

---

<div align="center">

MIT License © [nicepkg](https://github.com/nicepkg)

**Like it? Star it, and let more workers see this 🌟**

</div>
