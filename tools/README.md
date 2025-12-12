# Literature Notes Tools

Python tooling for managing a Zettelkasten-based knowledge management system.

## Installation

```bash
# Development installation
cd tools
pip install -e ".[dev]"
```

## CLI Tools

After installation, the following commands are available:

- `zk-build` - Build Zettelkasten database from markdown files
- `zk-search` - Search notes with natural language queries
- `zk-forest` - Build knowledge forest structure
- `zk-links` - Analyze and apply link suggestions
- `zk-generate` - Generate GitHub Pages site
- `zk-api` - Run the knowledge API server

## Architecture

```
tools/
├── src/                          # Source code
│   ├── zettelkasten/            # Core Zettelkasten functionality
│   ├── knowledge_graph/         # Knowledge graph and forest building
│   ├── generators/              # Site and content generators
│   ├── integrations/            # External tool integrations
│   ├── api/                     # API server
│   └── visualization/           # Visualization tools
├── scripts/                     # CLI entry points
└── tests/                       # Test suite
```

## Development

```bash
# Run tests
pytest

# Format code
black src/ scripts/ tests/

# Lint code
ruff check src/ scripts/ tests/
```

## Module Overview

### zettelkasten
Core functionality for managing the Zettelkasten database, searching notes, and managing wikilinks.

### knowledge_graph
Build and manage the knowledge forest structure with semantic pathways and clusters.

### generators
Generate various outputs including GitHub Pages content, search indices, and synthesis documents.

### integrations
Integration with external tools like LogSeq, Obsidian, and Foam.

### api
REST API server for querying the knowledge base.

### visualization
Generate visualizations of the knowledge graph and connections.
