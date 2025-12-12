#!/usr/bin/env python3
"""
Create backward-compatible wrapper scripts that point to the new tool locations.
This ensures existing workflows and documentation continue to work.
"""
from pathlib import Path

BASE = Path(__file__).parent
TOOLS_SCRIPTS = BASE / "tools" / "scripts"

# Map old script names to new CLI scripts
COMPATIBILITY_MAP = {
    "zettelkasten.py": "tools/scripts/build_database.py",
    "smart_query.py": "tools/scripts/search_notes.py",
    "build_forest.py": "tools/scripts/build_forest.py",
    "analyze_links.py": "tools/scripts/analyze_links.py",
    "github_pages_generator.py": "tools/scripts/generate_site.py",
}


def create_wrapper(old_name: str, new_path: str):
    """Create a compatibility wrapper script."""
    wrapper_path = BASE / old_name

    # Create a simple Python wrapper that calls the new script
    wrapper_content = f'''#!/usr/bin/env python3
"""
Backward-compatibility wrapper for {old_name}
This script redirects to the new location: {new_path}
"""
import sys
import subprocess
from pathlib import Path

# Get the new script path
new_script = Path(__file__).parent / "{new_path}"

# Execute the new script with all arguments
result = subprocess.run([sys.executable, str(new_script)] + sys.argv[1:])
sys.exit(result.returncode)
'''

    # Only create if the old script isn't being actively used
    if wrapper_path.exists() and wrapper_path.is_file():
        # Backup the old file
        backup_path = BASE / f"{old_name}.backup"
        wrapper_path.rename(backup_path)
        print(f"📦 Backed up {old_name} → {old_name}.backup")

    # Write the wrapper
    wrapper_path.write_text(wrapper_content)
    wrapper_path.chmod(0o755)
    print(f"✅ Created compatibility wrapper: {old_name} → {new_path}")


def main():
    print("🔗 Creating backward-compatibility wrappers...\n")

    for old_name, new_path in COMPATIBILITY_MAP.items():
        create_wrapper(old_name, new_path)

    print("\n✅ Compatibility wrappers created!")
    print("\n📝 Note: Old scripts now redirect to new tools/scripts/ location")
    print("   You can safely delete .backup files after verifying everything works")


if __name__ == "__main__":
    main()
