# 🌳 Knowledge Forest System - Quick Start Guide

## What is a Knowledge Forest?

A Knowledge Forest is an interconnected network of your notes that creates semantic pathways between related concepts. It allows you to:

- **Navigate organically** through related concepts
- **Discover unexpected connections** between different topics
- **Follow thematic trails** through your knowledge
- **Visualize knowledge clusters** and relationships

## 🚀 Quick Start

### 1. Generate Your Knowledge Forest

```bash
# Build forest from your entire notes collection
python simple_forest_builder.py --directory . --output my_forest.json --sample

# Or build from a specific directory
python simple_forest_builder.py --directory sanskrit-lit --output sanskrit_forest.json --sample
```

This will:
- Scan all `.md` files in the directory
- Extract titles, tags, and wiki-links (`[[Note Name]]`)
- Build semantic connections based on content similarity
- Create clusters of related notes
- Generate visualization data

### 2. Explore Your Forest

Open `knowledge_forest_navigator.html` in your web browser to:

- **Browse notes** in the left sidebar
- **See connections** in the main visualization
- **Follow pathways** by clicking on nodes
- **Get recommendations** in the right panel
- **Search** for specific notes or concepts

## 🌲 How It Works

### Connection Types

The system creates connections based on:

1. **Tag Overlap** (30% weight) - Notes with similar tags
2. **Content Similarity** (40% weight) - Notes with similar key terms  
3. **Wiki-Links** (30% weight) - Explicit `[[Note Name]]` connections

### Node Types

Notes are automatically classified as:

- **🔵 Concept** - Ideas, theories, explanations
- **🟢 Practice** - Techniques, exercises, methods
- **🟠 Reference** - Sources, links, bibliography
- **🟣 Synthesis** - Summaries, overviews, integrations

### Clustering

Related notes are grouped into semantic clusters based on strong connections, helping you discover thematic areas in your knowledge.

## 🧭 Navigation Patterns

### Following Trails

1. Start with any note that interests you
2. Click "🧭 Explore From Here" to see connected notes
3. Follow the strongest connections (thicker lines)
4. Use breadcrumbs to track your path

### Discovery Methods

- **Cluster Browsing** - Explore nodes in the same semantic cluster
- **Type Filtering** - Focus on concepts vs practices
- **Recommendation Following** - Use the AI-generated suggestions
- **Search & Connect** - Find specific notes and see their connections

## 📊 Understanding Your Forest

### Forest Stats Show:
- **Total Notes** - Size of your knowledge base
- **Connections** - How interconnected your notes are
- **Clusters** - Thematic areas in your knowledge
- **Node Types** - Distribution of different content types

### Most Connected Notes
These are often:
- Central concepts in your thinking
- Integration points between different topics
- Key references you cite frequently

## 🔧 Customization

### Improving Connections

1. **Add Tags** - Use consistent tagging for better clustering
2. **Use Wiki-Links** - Add `[[Note Name]]` connections between related notes  
3. **Include Key Terms** - Make sure important concepts appear in content
4. **Write Summaries** - Synthesis notes help connect disparate ideas

### Directory Structure

The system works best with organized directories:
```
notes/
├── concepts/
├── practices/  
├── people/
├── books/
└── projects/
```

## 🌟 Advanced Usage

### Generate Different Views

```bash
# Focus on specific topic areas
python simple_forest_builder.py --directory books --output books_forest.json --sample

# Combine with your existing tools
python simple_forest_builder.py --directory . --output full_forest.json
# Then use full_forest.json with your existing knowledge graph tools
```

### Integration with Existing Tools

The generated `forest_data.json` contains:
- **Nodes** with metadata (type, tags, connections, etc.)
- **Edges** with connection strengths
- **Clusters** with semantic groupings
- **Metadata** with summary statistics

This can be imported into other visualization tools like Obsidian, Roam Research, or custom D3.js visualizations.

## 🎯 Best Practices

### For Better Connections:
1. **Consistent Tagging** - Use the same tags for related concepts
2. **Cross-References** - Add `[[links]]` between related notes
3. **Clear Titles** - Use descriptive, searchable titles
4. **Key Terms** - Include important terms in your content

### For Better Navigation:
1. **Start Broad** - Begin with high-level concepts
2. **Follow Strength** - Stronger connections (thicker lines) are usually more meaningful
3. **Use Clusters** - Explore entire semantic clusters for comprehensive understanding
4. **Track Paths** - Use breadcrumbs to understand how concepts connect

## 🐛 Troubleshooting

### No Connections Showing?
- Check if notes have common tags or terms
- Add more `[[wiki-links]]` between related notes
- Ensure notes have substantial content (>100 words works better)

### Visualization Not Loading?
- Make sure you ran with `--sample` flag
- Check that `sample_forest_data.js` exists
- Open browser developer tools to see any JavaScript errors

### Poor Clustering?
- Add more descriptive tags to your notes
- Use consistent terminology across related notes
- Consider splitting very long notes into focused topics

---

**Happy Exploring! 🌳✨**

Your knowledge forest grows more valuable as you add more connections and spend time navigating the pathways between your ideas.