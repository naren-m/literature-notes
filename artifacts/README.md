# Artifacts Directory

This directory contains generated files and visualizations that are not committed to the repository.

## Subdirectories

- **data/** - Generated JSON files (forest data, link changes, etc.)
- **visualizations/** - HTML visualization files
- **temp/** - Temporary files (canvas, etc.)

## Contents

All files in this directory are gitignored except this README. These are generated artifacts from:

- `zettelkasten.py` - Note database and analysis
- `knowledge_forest.py` - Forest structure generation
- `analyze_links.py` - Link analysis and suggestions
- Obsidian/LogSeq temporary files

## Regenerating

To regenerate these files, run:

```bash
python zettelkasten.py build
python knowledge_forest.py build
```

See the `docs/` directory for setup guides and troubleshooting.
