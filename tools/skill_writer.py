#!/usr/bin/env python3
"""Boss Skill file management utility."""

import argparse
import json
import os
import sys
from pathlib import Path


def list_bosses(base_dir: str) -> None:
    """List all generated boss skills."""
    base = Path(base_dir)
    if not base.exists():
        print("No bosses created yet.")
        return

    bosses = []
    for d in sorted(base.iterdir()):
        meta_path = d / "meta.json"
        if d.is_dir() and meta_path.exists():
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            bosses.append(meta)

    if not bosses:
        print("No bosses created yet.")
        return

    print(f"Found {len(bosses)} boss(es):\n")
    for b in bosses:
        profile = b.get("profile", {})
        tags = b.get("tags", {})
        mgmt_tags = ", ".join(tags.get("management", [])[:3])
        print(f"  /{b['slug']}")
        print(f"    Name: {b['name']}")
        print(f"    Industry: {profile.get('industry', 'N/A')} | Title: {profile.get('title', 'N/A')}")
        print(f"    Style: {mgmt_tags or 'N/A'}")
        print(f"    Version: {b.get('version', 'v1')} | Updated: {b.get('updated_at', 'N/A')}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Boss Skill file management")
    parser.add_argument("--action", required=True, choices=["list"])
    parser.add_argument("--base-dir", default=".")
    args = parser.parse_args()

    if args.action == "list":
        list_bosses(args.base_dir)


if __name__ == "__main__":
    main()
