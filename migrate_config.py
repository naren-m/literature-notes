#!/usr/bin/env python3
"""
Migration script for Phase 4: Configuration and Artifacts
Moves tool configurations and generated artifacts to proper locations.
"""
import shutil
from pathlib import Path
import subprocess

BASE = Path(__file__).parent

# Configuration migrations
CONFIG_MIGRATIONS = [
    (".obsidian", "config/note-tools/obsidian"),
    (".foam", "config/note-tools/foam"),
    ("logseq", "config/note-tools/logseq"),
    ("templates", "config/templates"),
]

# Artifact migrations
ARTIFACT_MIGRATIONS = [
    ("zettelkasten.db", "build/database/zettelkasten.db"),
    ("artifacts/data/my_forest.json", "build/graphs/my_forest.json"),
    ("artifacts/data/improved_forest.json", "build/graphs/improved_forest.json"),
    ("artifacts/data/full_forest.json", "build/graphs/full_forest.json"),
    ("artifacts/data/missing_links.json", "build/graphs/missing_links.json"),
    ("artifacts/data/link_changes.json", "build/graphs/link_changes.json"),
    ("assets/search-index.json", "build/indices/search-index.json"),
    ("assets/search-suggestions.json", "build/indices/search-suggestions.json"),
]


def migrate_item(source_rel: str, dest_rel: str, item_type: str = "file"):
    """Migrate a file or directory."""
    source = BASE / source_rel
    dest = BASE / dest_rel

    if not source.exists():
        print(f"⚠️  Source not found: {source_rel}")
        return False

    # Ensure parent directory exists
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Move the item
    if dest.exists():
        print(f"⚠️  Destination exists, skipping: {dest_rel}")
        return False

    shutil.move(str(source), str(dest))
    print(f"✅ Moved {item_type}: {source_rel} → {dest_rel}")
    return True


def create_migration_plan():
    """Display migration plan."""
    print("📋 Configuration & Artifacts Migration Plan\n")

    print("CONFIGURATIONS:")
    for source, dest in CONFIG_MIGRATIONS:
        source_path = BASE / source
        exists = "✓" if source_path.exists() else "✗"
        print(f"  {exists} {source:40} → {dest}")

    print("\nARTIFACTS:")
    for source, dest in ARTIFACT_MIGRATIONS:
        source_path = BASE / source
        exists = "✓" if source_path.exists() else "✗"
        print(f"  {exists} {source:40} → {dest}")


def execute_migration(dry_run: bool = True):
    """Execute configuration and artifacts migration."""
    if dry_run:
        print("\n🔍 DRY RUN MODE - No changes will be made\n")
        create_migration_plan()
        return

    print("🚀 Starting Phase 4: Configuration & Artifacts migration...\n")

    print("📁 Migrating configurations...")
    config_count = 0
    for source, dest in CONFIG_MIGRATIONS:
        if migrate_item(source, dest, "config"):
            config_count += 1

    print("\n📦 Migrating artifacts...")
    artifact_count = 0
    for source, dest in ARTIFACT_MIGRATIONS:
        if migrate_item(source, dest, "artifact"):
            artifact_count += 1

    print(f"\n✅ Phase 4 migration complete!")
    print(f"   Configurations migrated: {config_count}/{len(CONFIG_MIGRATIONS)}")
    print(f"   Artifacts migrated: {artifact_count}/{len(ARTIFACT_MIGRATIONS)}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Migrate configs and artifacts")
    parser.add_argument("--execute", action="store_true",
                      help="Execute the migration (default is dry-run)")
    args = parser.parse_args()

    execute_migration(dry_run=not args.execute)


if __name__ == "__main__":
    main()
