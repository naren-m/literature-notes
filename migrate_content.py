#!/usr/bin/env python3
"""
Migration script for Phase 3: Content Reorganization
Moves content to new hierarchical structure while preserving git history.
"""
import shutil
from pathlib import Path
import subprocess

BASE = Path(__file__).parent
CONTENT = BASE / "content"

# Content migration mapping: (source, destination)
CONTENT_MIGRATIONS = [
    # Computer Science domain
    ("CSE/Cryptography", "content/domains/computer-science/cryptography"),
    ("CSE/coding", "content/domains/computer-science/coding-practices"),
    ("CSE/design_patterns", "content/domains/computer-science/design-patterns"),
    ("Security", "content/domains/computer-science/security"),

    # Mathematics domain
    ("Statistics", "content/domains/mathematics/statistics"),
    ("math", "content/domains/mathematics/general"),

    # Humanities domain
    ("sanskrit-lit", "content/domains/humanities/sanskrit-literature"),
    ("india", "content/domains/humanities/history"),

    # Wellness domain
    ("books/ashtangahrydayam", "content/domains/wellness/ayurveda"),

    # Media content
    ("books", "content/media/books"),
    ("highlights/Books", "content/media/books/highlights"),
    ("highlights/Articles", "content/media/articles"),
    ("podcast", "content/media/podcasts"),
    ("video", "content/media/videos"),

    # Other content
    ("people", "content/people"),
    ("research", "content/research"),
    ("daily-notes", "content/journal"),
]


def git_mv(source: Path, dest: Path):
    """Move file/directory using git mv to preserve history."""
    try:
        subprocess.run(
            ["git", "mv", str(source), str(dest)],
            check=True,
            cwd=BASE,
            capture_output=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def migrate_directory(source_rel: str, dest_rel: str, use_git: bool = True):
    """Migrate a directory from source to destination."""
    source = BASE / source_rel
    dest = BASE / dest_rel

    if not source.exists():
        print(f"⚠️  Source not found: {source_rel}")
        return False

    if dest.exists():
        print(f"⚠️  Destination already exists: {dest_rel}")
        return False

    # Ensure parent directory exists
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Try git mv first if in a git repo
    if use_git and (BASE / ".git").exists():
        if git_mv(source, dest):
            print(f"✅ Git moved: {source_rel} → {dest_rel}")
            return True
        else:
            print(f"⚠️  Git mv failed for {source_rel}, using regular move")

    # Fall back to regular move
    shutil.move(str(source), str(dest))
    print(f"✅ Moved: {source_rel} → {dest_rel}")
    return True


def create_migration_plan():
    """Create and display migration plan without executing."""
    print("📋 Content Migration Plan\n")
    print("The following moves will be performed:\n")

    for source, dest in CONTENT_MIGRATIONS:
        source_path = BASE / source
        exists = "✓" if source_path.exists() else "✗"
        print(f"{exists} {source:50} → {dest}")

    print("\n" + "="*80)
    print("Total directories to migrate:", len(CONTENT_MIGRATIONS))
    existing = sum(1 for s, _ in CONTENT_MIGRATIONS if (BASE / s).exists())
    print(f"Existing directories: {existing}/{len(CONTENT_MIGRATIONS)}")


def execute_migration(dry_run: bool = True):
    """Execute the content migration."""
    if dry_run:
        print("\n🔍 DRY RUN MODE - No changes will be made\n")
        create_migration_plan()
        return

    print("🚀 Starting content migration (Phase 3)...\n")

    success_count = 0
    skip_count = 0

    for source_rel, dest_rel in CONTENT_MIGRATIONS:
        if migrate_directory(source_rel, dest_rel):
            success_count += 1
        else:
            skip_count += 1

    print(f"\n✅ Phase 3 content migration complete!")
    print(f"   Migrated: {success_count}")
    print(f"   Skipped: {skip_count}")
    print("\n📝 Next steps:")
    print("1. Update wikilinks in markdown files")
    print("2. Rebuild Zettelkasten database")
    print("3. Verify links are working")
    print("4. Test GitHub Pages build")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Migrate content to new structure")
    parser.add_argument("--execute", action="store_true",
                      help="Execute the migration (default is dry-run)")
    args = parser.parse_args()

    execute_migration(dry_run=not args.execute)


if __name__ == "__main__":
    main()
