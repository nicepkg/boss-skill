#!/usr/bin/env python3
"""
Boss Skill Generator — create a self-contained boss skill from data.

Usage:
    python3 <this-dir>/create_boss.py --from-example 王总 --skills-dir <dir>
    python3 <this-dir>/create_boss.py --demo --skills-dir <dir>
    python3 <this-dir>/create_boss.py --list
    python3 <this-dir>/create_boss.py --from-file data.json --skills-dir <dir>
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


PROMPTS_TO_COPY = [
    "pua_detector.md", "cake_detector.md", "counterattack.md",
    "evidence_collector.md", "labor_law.md", "predict.md",
    "report_optimizer.md", "one_on_one.md", "delegate.md",
    "karma.md", "quit_script.md", "replacement_notice.md",
]


def get_script_dir():
    return Path(__file__).resolve().parent


def get_create_boss_dir():
    return get_script_dir().parent


def read_skill_template():
    tpl_path = get_create_boss_dir() / "references" / "guides" / "generated-skill-spec.md"
    if not tpl_path.exists():
        return None
    return tpl_path.read_text(encoding="utf-8")


def create_boss(data: dict, skills_dir: str, creator_dir: Path = None) -> Path:
    if creator_dir is None:
        creator_dir = get_create_boss_dir()

    boss_name = data["name"]
    boss_dir = Path(skills_dir) / boss_name
    assets_dir = boss_dir / "assets"
    prompts_dir = assets_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    # 1. Copy prompt templates
    src_prompts = creator_dir / "references" / "prompts"
    copied = 0
    for pname in PROMPTS_TO_COPY:
        src = src_prompts / pname
        if src.exists():
            content = src.read_text(encoding="utf-8")
            content = content.replace("{boss-name}", boss_name)
            (prompts_dir / pname).write_text(content, encoding="utf-8")
            copied += 1

    # 2. Write management.md
    mgmt_content = data.get("management_content", "(pending)")
    mgmt = f"# {boss_name} management style\n\n{mgmt_content}\n"
    (assets_dir / "management.md").write_text(mgmt, encoding="utf-8")

    # 3. Write persona.md
    persona_content = data.get("persona_content", "(pending)")
    persona = f"# {boss_name} persona\n\n{persona_content}\n"
    (assets_dir / "persona.md").write_text(persona, encoding="utf-8")

    # 4. Write profile.md
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    tags_str = ", ".join(data.get("tags", []))
    phrases = data.get("catchphrases", [])
    phrases_str = "\n".join(f'- "{p}"' for p in phrases)

    profile = (
        f"# {boss_name} multi-dimensional profile\n\n"
        f"> Living doc - auto-updated on PUA detect / cake check / correction\n\n"
        f"## Basic Info\n"
        f"- Codename: {boss_name}\n"
        f"- Industry: {data.get('industry', '')}\n"
        f"- Title: {data.get('title', '')}\n"
        f"- Company type: {data.get('company_type', '')}\n"
        f"- Team size: {data.get('team_size', '')}\n"
        f"- MBTI: {data.get('mbti', '')}\n\n"
        f"## Management Profile\n"
        f"- Style tags: [{tags_str}]\n"
        f"- Catchphrases:\n{phrases_str}\n"
        f"- PUA flavor: {data.get('pua_flavor', 'TBD')}\n"
        f"- Impression: {data.get('impression', '')}\n\n"
        f"## Cake History\n"
        f"| Date | Promise | BS Score | Delivered? |\n"
        f"|------|---------|----------|------------|\n\n"
        f"## PUA Record\n"
        f"| Date | Quote | Technique | Flavor |\n"
        f"|------|-------|-----------|--------|\n\n"
        f"## Relationship Map\n"
        f"- Boss's boss: TBD\n"
        f"- Inner circle: TBD\n"
        f"- Blame target: TBD\n\n"
        f"## Data Sources\n"
        f"- Source types: [example]\n"
        f"- Created: {now}\n"
        f"- Last updated: {now}\n"
        f"- Update count: 0\n\n"
        f"## Corrections\n"
    )
    (assets_dir / "profile.md").write_text(profile, encoding="utf-8")

    # 5. Write evidence.md (empty)
    evidence = f"# {boss_name} PUA evidence log\n\n> Add records via /{boss_name} evidence\n\n(no records yet)\n"
    (assets_dir / "evidence.md").write_text(evidence, encoding="utf-8")

    # 6. Write SKILL.md
    industry = data.get("industry", "")
    title = data.get("title", "")
    company_type = data.get("company_type", "")

    skill_md = (
        f"---\n"
        f"name: {boss_name}\n"
        f'description: "{boss_name}, {industry} {title}, AI stand-in"\n'
        f'argument-hint: "[pua|cake|fight|evidence|law|raise|predict|report|1v1|delegate|meeting|翻车|quit|replace]"\n'
        f"user-invocable: true\n"
        f"allowed-tools: Read, Write, Edit, Bash\n"
        f"---\n\n"
        f"# {boss_name} (AI stand-in)\n\n"
        f"{industry} {title} | {company_type}\n\n"
        f"## Identity & Data\n\n"
        f"On startup, **MUST read** these files to understand the boss:\n"
        f"- Management style: `<this-skill-dir>/assets/management.md`\n"
        f"- Persona: `<this-skill-dir>/assets/persona.md`\n"
        f"- Profile: `<this-skill-dir>/assets/profile.md`\n\n"
        f"## Default Mode (no subcommand)\n\n"
        f"Chat as AI boss. Strictly follow persona.md expression style + management.md decisions.\n\n"
        f"Rules:\n"
        f"1. persona.md decides mood and attitude\n"
        f"2. management.md decides actions\n"
        f"3. Output always in persona.md style\n"
        f"4. Layer 0 hard rules override everything\n\n"
        f'## Trigger: "草"\n\n'
        f"In **any mode**, when user types 草/卧槽/我靠/怎么怼/教我反击:\n"
        f"-> Switch to fight mode for the last boss statement.\n"
        f"-> Read `<this-skill-dir>/assets/prompts/counterattack.md`\n\n"
        f"## Subcommand Routing\n\n"
        f"### pua\n"
        f"Read `<this-skill-dir>/assets/prompts/pua_detector.md`, execute framework.\n"
        f"After detection, **auto-append** to `<this-skill-dir>/assets/profile.md` PUA Record.\n"
        f"End with: input 草 to learn counterattack\n\n"
        f"### cake\n"
        f"Read `<this-skill-dir>/assets/prompts/cake_detector.md`, execute framework.\n"
        f"After check, **auto-append** to `<this-skill-dir>/assets/profile.md` Cake History.\n"
        f"End with: input 草 to get counterattack\n\n"
        f"### fight\n"
        f"Read `<this-skill-dir>/assets/prompts/counterattack.md`, 3-level system.\n\n"
        f"### evidence\n"
        f"Read `<this-skill-dir>/assets/prompts/evidence_collector.md`.\n"
        f"Append to `<this-skill-dir>/assets/evidence.md`.\n"
        f"`evidence export` = full timeline report.\n\n"
        f"### law\n"
        f"Read `<this-skill-dir>/assets/prompts/labor_law.md`, match laws.\n\n"
        f"### raise\n"
        f"Role-play salary negotiation per persona.md, then break character with coaching.\n\n"
        f"### predict\n"
        f"Read `<this-skill-dir>/assets/prompts/predict.md`, predict based on persona + management.\n\n"
        f"### report\n"
        f"Read `<this-skill-dir>/assets/prompts/report_optimizer.md`, rewrite in boss's jargon.\n\n"
        f"### 1v1\n"
        f"Read `<this-skill-dir>/assets/prompts/one_on_one.md`, role-play + coach commentary.\n\n"
        f"### delegate\n"
        f"Read `<this-skill-dir>/assets/prompts/delegate.md`, 3 tones.\n\n"
        f"### meeting\n"
        f"Simulate boss's meeting style per management.md. Include overtime, off-topic, etc.\n\n"
        f"### 翻车\n"
        f"Read `<this-skill-dir>/assets/prompts/karma.md`, launch interactive text game.\n\n"
        f"### quit\n"
        f"Read `<this-skill-dir>/assets/prompts/quit_script.md`, customize per persona.\n\n"
        f"### replace\n"
        f"Read `<this-skill-dir>/assets/prompts/replacement_notice.md`, generate notice.\n\n"
        f"## Evolution\n\n"
        f"- New material -> update assets/management.md + persona.md + profile.md\n"
        f"- User says 'not like him' -> append to profile.md Corrections\n"
        f"- PUA/cake checks -> auto-update profile.md history\n"
    )
    (boss_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    # 7. Register in create-boss
    registry_path = creator_dir / "bosses-registry.json"
    registry = []
    if registry_path.exists():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            registry = []

    entry = {
        "name": boss_name,
        "path": str(boss_dir),
        "industry": data.get("industry", ""),
        "title": data.get("title", ""),
        "tags": data.get("tags", []),
        "created_at": now,
        "updated_at": now,
    }
    registry = [e for e in registry if e["name"] != boss_name]
    registry.append(entry)
    registry_path.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"  /{boss_name} skill created at {boss_dir}")
    print(f"  SKILL.md + assets/ ({copied} prompts, 5 data files)")
    print(f"  Registered in bosses-registry.json")
    return boss_dir


def list_bosses(creator_dir: Path = None):
    if creator_dir is None:
        creator_dir = get_create_boss_dir()
    registry_path = creator_dir / "bosses-registry.json"

    if not registry_path.exists():
        print("No bosses created yet. Try: --demo or --from-example")
        return

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if not registry:
        print("No bosses created yet.")
        return

    print(f"{len(registry)} boss(es) created:\n")
    for b in registry:
        tags = ", ".join(b.get("tags", [])[:3])
        exists = "OK" if Path(b["path"]).exists() else "MISSING"
        print(f"  /{b['name']}  [{exists}]")
        print(f"    {b.get('industry', '')} {b.get('title', '')} | {tags}")
        print(f"    Path: {b['path']}")
        print()


def demo(skills_dir: str, creator_dir: Path = None):
    if creator_dir is None:
        creator_dir = get_create_boss_dir()

    examples_dir = creator_dir / "examples"
    if not examples_dir.exists():
        print("Error: examples/ not found", file=sys.stderr)
        sys.exit(1)

    for f in sorted(examples_dir.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        create_boss(data, skills_dir, creator_dir)
        print()

    print("Demo bosses ready! Try:")
    print("  /王总           chat with AI boss")
    print("  /王总 pua       PUA detection")
    print("  /王总 翻车      interactive text game")
    print("  /刘姐 cake     cake-promise BS meter")
    print("  /张总 fight    counterattack coach")


def main():
    parser = argparse.ArgumentParser(description="Boss Skill Generator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--from-example", metavar="NAME")
    group.add_argument("--from-file", metavar="PATH")
    group.add_argument("--demo", action="store_true")
    group.add_argument("--list", action="store_true")

    parser.add_argument("--skills-dir", default=None)

    args = parser.parse_args()
    creator_dir = get_create_boss_dir()

    if args.list:
        list_bosses(creator_dir)
    elif args.demo:
        if not args.skills_dir:
            parser.error("--skills-dir required for --demo")
        demo(args.skills_dir, creator_dir)
    elif args.from_example:
        if not args.skills_dir:
            parser.error("--skills-dir required")
        ep = creator_dir / "examples" / f"{args.from_example}.json"
        if not ep.exists():
            avail = [f.stem for f in (creator_dir / "examples").glob("*.json")]
            print(f"Error: '{args.from_example}' not found. Available: {avail}", file=sys.stderr)
            sys.exit(1)
        data = json.loads(ep.read_text(encoding="utf-8"))
        create_boss(data, args.skills_dir, creator_dir)
    elif args.from_file:
        if not args.skills_dir:
            parser.error("--skills-dir required")
        data = json.loads(Path(args.from_file).read_text(encoding="utf-8"))
        create_boss(data, args.skills_dir, creator_dir)


if __name__ == "__main__":
    main()
