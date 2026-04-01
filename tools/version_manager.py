#!/usr/bin/env python3
"""Boss Skill version management — backup and rollback."""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def backup(slug: str, base_dir: str) -> None:
    """Archive current version before update."""
    boss_dir = Path(base_dir) / slug
    versions_dir = boss_dir / "versions"
    versions_dir.mkdir(parents=True, exist_ok=True)

    meta_path = boss_dir / "meta.json"
    if not meta_path.exists():
        print(f"Error: boss '{slug}' not found at {boss_dir}", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    version = meta.get("version", "v1")
    version_dir = versions_dir / version
    version_dir.mkdir(exist_ok=True)

    for fname in ["SKILL.md"]:
        src = boss_dir / fname
        if src.exists():
            shutil.copy2(src, version_dir / fname)
    # Also backup assets
    assets_dir = boss_dir / "assets"
    if assets_dir.exists():
        assets_backup = version_dir / "assets"
        if assets_backup.exists():
            shutil.rmtree(assets_backup)
        shutil.copytree(assets_dir, assets_backup)

    # bump version
    v_num = int(version.lstrip("v")) + 1
    meta["version"] = f"v{v_num}"
    meta["updated_at"] = datetime.now(timezone.utc).isoformat()

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"Backed up {slug} {version} → {version_dir}")
    print(f"Current version bumped to v{v_num}")


def rollback(slug: str, version: str, base_dir: str) -> None:
    """Rollback to a previous version."""
    boss_dir = Path(base_dir) / slug
    version_dir = boss_dir / "versions" / version

    if not version_dir.exists():
        available = [d.name for d in (boss_dir / "versions").iterdir() if d.is_dir()]
        print(f"Error: version '{version}' not found. Available: {available}", file=sys.stderr)
        sys.exit(1)

    for fname in ["SKILL.md"]:
        src = version_dir / fname
        if src.exists():
            shutil.copy2(src, boss_dir / fname)

    print(f"Rolled back {slug} to {version}")


def main():
    parser = argparse.ArgumentParser(description="Boss Skill version management")
    parser.add_argument("--action", required=True, choices=["backup", "rollback"])
    parser.add_argument("--slug", required=True)
    parser.add_argument("--version", default=None)
    parser.add_argument("--base-dir", default=".")
    args = parser.parse_args()

    if args.action == "backup":
        backup(args.slug, args.base_dir)
    elif args.action == "rollback":
        if not args.version:
            print("Error: --version required for rollback", file=sys.stderr)
            sys.exit(1)
        rollback(args.slug, args.version, args.base_dir)


if __name__ == "__main__":
    main()
