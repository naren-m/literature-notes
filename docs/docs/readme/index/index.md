---
layout: "default"
title: "Literature Notes - Zettelkasten System"
tags:
  - python
  - cryptography
  - india
  - science
  - philosophy
  - programming
  - tag
  - algorithms
word_count: 583
created: "2025-06-25T14:36:45.423088"
modified: "2025-06-25T14:36:45.423088"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Readme"
    url: "/topics/docs/readme//"
---
---
layout: "default"
title: "Literature Notes - Zettelkasten System"
tags:
  - india
  - cryptography
  - science
  - python
  - tag
  - programming
  - algorithms
  - philosophy
word_count: 548
created: "2025-06-25T14:26:07.974480"
modified: "2025-06-25T14:26:07.974480"
---
# Literature Notes - Zettelkasten System

A comprehensive knowledge management system for organizing, searching, and visualizing interconnected notes.

## 🧠 Features

- **Smart Indexing**: Automatically scans and catalogs all markdown files
- **Link Discovery**: Finds connections between notes via wikilinks `*note*`
- **Tag System**: Extracts and organizes tags for easy categorization
- **Full-Text Search**: Search across all note content, titles, and tags
- **Interactive Visualization**: Generate beautiful knowledge graphs
- **Backlink Generation**: Automatically creates bidirectional relationships
- **CLI Interface**: Easy-to-use command line tools

## 🚀 Quick Start

### 1. Index Your Notes
```bash
# Index all markdown files in current directory
./zettel index

# Or specify a different root directory
python3 zettelkasten.py --root /path/to/notes index
```

### 2. Search Your Knowledge Base
```bash
# Search for notes containing "cryptography"
./zettel search cryptography

# Limit results to 5
./zettel search "machine learning" --limit 5
```

### 3. Explore Tags
```bash
# List all tags with counts
./zettel tags

# Show all notes with a specific tag
./zettel tags --tag programming
```

### 4. Visualize Connections
```bash
# Generate interactive HTML graph
python3 visualize.py --type html

# Generate static network graph (requires networkx/matplotlib)
python3 visualize.py --type network

# Generate all visualizations
python3 visualize.py --type all
```

### 5. View Note Relationships
```bash
# Show links and backlinks for a specific note
./zettel links "CSE/Cryptography/Encryption.md"
```

### 6. System Statistics
```bash
# View system overview
./zettel stats
```

## 📁 File Structure

```
literature-notes/
├── zettelkasten.py      # Main indexing and search script
├── visualize.py         # Visualization tools
├── zettel              # CLI wrapper script
├── requirements.txt     # Python dependencies
├── zettelkasten.db     # SQLite database (auto-created)
└── knowledge_graph.html # Interactive visualization (auto-generated)
```

## 💡 Usage Tips

### Wikilinks
Use `*note title*` to create links between notes:
```markdown
This concept relates to *Machine Learning* and *Statistics*.
```

### Tags
Use `#tag` format for categorization:
```markdown
This is about #programming #python #algorithms
```

### Note Organization
- Use descriptive titles for better search results
- Include relevant tags for categorization
- Create wikilinks to connect related concepts
- Keep notes atomic (one concept per note)

## 🔧 Advanced Usage

### Custom Database Location
```bash
python3 zettelkasten.py --db /path/to/custom.db index
```

### Filtering Visualizations
The HTML visualization includes interactive filters:
- Search by note content or title
- Filter by specific tags
- Set minimum connection thresholds
- Reset view to show all notes

### Database Schema
The system uses SQLite with tables for:
- `notes`: Complete note metadata and content
- `links`: Relationships between notes
- `tags`: Tag associations

## 🛠 Installation

1. Clone or download the scripts
2. Install optional dependencies for static graphs:
   ```bash
   pip install -r requirements.txt
   ```
3. Make the CLI script executable:
   ```bash
   chmod +x zettel
   ```

## 📊 System Statistics Example

```
📊 Zettelkasten Statistics

Total notes: 342
Total links: 1,247
Total tags: 89
Average links per note: 3.6

🏷️  Top tags:
  #programming (45)
  #philosophy (32)
  #science (28)
  #cryptography (23)
  #india (19)

🔗 Most linked notes:
  Machine Learning (12 links)
  Cryptography (8 links)
  Sanskrit Literature (7 links)
```

## 🎯 Example Workflows

### Research Mode
1. `./zettel search "topic"` - Find relevant notes
2. `./zettel links "note.md"` - Explore connections  
3. Open interactive graph to visualize relationships

### Writing Mode
1. Create new note with wikilinks to existing concepts
2. `./zettel index` - Update the knowledge graph
3. `./zettel tags --tag newtag` - Find related tagged content

### Discovery Mode
1. `python3 visualize.py` - Generate knowledge graph
2. Open HTML file in browser
3. Use filters to explore clusters and connections

---

**Note**: This system works with any collection of markdown files and preserves your existing file structure while adding powerful search and visualization capabilities.

[Agni](sanskrit-lit/agni/)