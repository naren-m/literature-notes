# Literature Notes - Zettelkasten System

A comprehensive knowledge management system for organizing, searching, and visualizing interconnected notes.

## 🧠 Features

- **Smart Indexing**: Automatically scans and catalogs all markdown files
- **Link Discovery**: Finds connections between notes via wikilinks `[[note]]`
- **Tag System**: Extracts and organizes tags for easy categorization
- **Full-Text Search**: Search across all note content, titles, and tags
- **Interactive Visualization**: Generate beautiful knowledge graphs
- **Backlink Generation**: Automatically creates bidirectional relationships
- **CLI Interface**: Easy-to-use command line tools
- **GitHub Pages**: Deploy as a searchable website with navigation

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
Use `[[note title]]` to create links between notes:
```markdown
This concept relates to [[Machine Learning]] and [[Statistics]].
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

## 🌐 GitHub Pages Deployment

Deploy your knowledge base as a beautiful, searchable website:

```bash
# One-command deployment
./deploy_pages.sh

# Or step by step:
python3 zettelkasten.py index                    # Index notes
python3 visualize.py --type html                 # Generate graph
python3 github_pages_generator.py --clean        # Create pages
python3 search_generator.py                      # Add search
python3 copy_graph_to_pages.py                   # Copy graph
```

### GitHub Pages Features
- **Responsive Design**: Works on desktop and mobile
- **Client-side Search**: Fast search using Lunr.js
- **Topic Organization**: Browse by subject areas
- **Tag Navigation**: Filter by tags and themes
- **Interactive Graph**: Embedded knowledge visualization
- **Breadcrumb Navigation**: Easy wayfinding
- **Backlink Display**: See what references each note

### Setup GitHub Pages
1. Push the generated `docs/` folder to your GitHub repository
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch"
4. Select `main` branch and `/docs` folder
5. Your site will be live at `https://username.github.io/repository-name/`

## 🎯 Example Workflows

### Research Mode
1. `./zettel search "topic"` - Find relevant notes
2. `./zettel links "note.md"` - Explore connections  
3. Open interactive graph to visualize relationships
4. Browse website at `/topics/subject/` for organized view

### Writing Mode
1. Create new note with wikilinks to existing concepts
2. `./zettel index` - Update the knowledge graph
3. `./zettel tags --tag newtag` - Find related tagged content
4. `./deploy_pages.sh` - Update website

### Discovery Mode
1. Visit your GitHub Pages site
2. Use search to find specific content
3. Browse topics and tags for exploration
4. View interactive graph for connection insights

### Sharing Mode
1. Deploy to GitHub Pages for public access
2. Share specific note URLs
3. Reference topics and tag collections
4. Embed interactive graph in presentations

---

**Note**: This system works with any collection of markdown files and preserves your existing file structure while adding powerful search, visualization, and web publishing capabilities.

[[Agni]]