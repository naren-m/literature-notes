#!/usr/bin/env python3
"""
Migration script to reorganize Python codebase into proper package structure.
Phase 2: Code Migration
"""
import shutil
from pathlib import Path

# Base paths
BASE = Path(__file__).parent
TOOLS_SRC = BASE / "tools" / "src"
TOOLS_SCRIPTS = BASE / "tools" / "scripts"

# Script migration mapping: (source_file, target_module_path, target_script_name)
MIGRATIONS = [
    # Core Zettelkasten functionality
    ("zettelkasten.py", TOOLS_SRC / "zettelkasten" / "core.py", "build_database.py"),
    ("smart_query.py", TOOLS_SRC / "zettelkasten" / "search.py", "search_notes.py"),

    # Knowledge graph functionality
    ("knowledge_forest.py", TOOLS_SRC / "knowledge_graph" / "forest.py", None),
    ("build_forest.py", TOOLS_SRC / "knowledge_graph" / "forest_builder.py", "build_forest.py"),
    ("clean_forest_builder.py", TOOLS_SRC / "knowledge_graph" / "clean_builder.py", None),
    ("simple_forest_builder.py", TOOLS_SRC / "knowledge_graph" / "simple_builder.py", None),
    ("analyze_links.py", TOOLS_SRC / "knowledge_graph" / "link_analyzer.py", "analyze_links.py"),
    ("apply_links.py", TOOLS_SRC / "knowledge_graph" / "link_applier.py", None),

    # Generators
    ("generate_synthesis.py", TOOLS_SRC / "generators" / "synthesis.py", None),
    ("knowledge_synthesis.py", TOOLS_SRC / "generators" / "knowledge_synthesis.py", None),
    ("github_pages_generator.py", TOOLS_SRC / "generators" / "github_pages.py", "generate_site.py"),
    ("search_generator.py", TOOLS_SRC / "generators" / "search_index.py", None),
    ("generate_readmes.py", TOOLS_SRC / "generators" / "readmes.py", None),

    # Integrations
    ("logseq_integration.py", TOOLS_SRC / "integrations" / "logseq.py", None),

    # API
    ("minimal_api.py", TOOLS_SRC / "api" / "minimal.py", None),
    ("simple_api_start.py", TOOLS_SRC / "api" / "simple_start.py", None),
    ("debug_api.py", TOOLS_SRC / "api" / "debug.py", None),
    ("integrate_api_with_docs.py", TOOLS_SRC / "api" / "docs_integration.py", "run_api.py"),

    # Visualization
    ("visualize.py", TOOLS_SRC / "visualization" / "graphs.py", None),
    ("copy_graph_to_pages.py", TOOLS_SRC / "visualization" / "copy_to_pages.py", None),

    # Utilities (can stay at root level for now or move to tools/utils/)
    ("fix_content.py", TOOLS_SRC / "utils" / "fix_content.py", None),
    ("test_integration.py", BASE / "tools" / "tests" / "test_integration.py", None),
]


def create_cli_wrapper(script_name: str, module_path: str, function_name: str = "main"):
    """Create a CLI wrapper script."""
    return f'''#!/usr/bin/env python3
"""
CLI entry point for {script_name}
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from {module_path} import {function_name}

if __name__ == "__main__":
    {function_name}()
'''


def migrate_file(source: Path, target_module: Path, cli_script: str = None):
    """Migrate a single file."""
    if not source.exists():
        print(f"⚠️  Source not found: {source}")
        return

    # Ensure target directory exists
    target_module.parent.mkdir(parents=True, exist_ok=True)

    # Copy to target module location
    shutil.copy2(source, target_module)
    print(f"✅ Copied {source.name} → {target_module.relative_to(BASE)}")

    # Create CLI wrapper if specified
    if cli_script:
        # Determine module path from target
        rel_path = target_module.relative_to(TOOLS_SRC)
        module_path = str(rel_path.with_suffix('')).replace('/', '.')

        cli_path = TOOLS_SCRIPTS / cli_script
        cli_content = create_cli_wrapper(cli_script, module_path)

        cli_path.write_text(cli_content)
        cli_path.chmod(0o755)
        print(f"✅ Created CLI wrapper: {cli_path.relative_to(BASE)}")


def create_utils_dir():
    """Create utils directory if needed."""
    utils_dir = TOOLS_SRC / "utils"
    utils_dir.mkdir(exist_ok=True)
    (utils_dir / "__init__.py").touch()


def main():
    print("🚀 Starting code migration (Phase 2)...\n")

    # Create utils directory
    create_utils_dir()

    # Migrate all files
    for source_file, target_module, cli_script in MIGRATIONS:
        source = BASE / source_file
        migrate_file(source, target_module, cli_script)

    print("\n✅ Phase 2 migration complete!")
    print("\n📝 Next steps:")
    print("1. Test the new CLI scripts in tools/scripts/")
    print("2. Update import paths if needed")
    print("3. Create symlinks for backward compatibility (optional)")
    print("4. Update documentation")


if __name__ == "__main__":
    main()
