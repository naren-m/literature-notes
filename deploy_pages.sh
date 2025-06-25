#!/bin/bash
# Deploy script for GitHub Pages

echo "🚀 Deploying Literature Notes to GitHub Pages..."

# Step 1: Index notes
echo "📝 Indexing notes..."
python3 zettelkasten.py index

# Step 2: Generate visualization
echo "🕸️ Generating knowledge graph..."
python3 visualize.py --type html

# Step 3: Generate GitHub Pages
echo "📄 Generating GitHub Pages..."
python3 github_pages_generator.py --clean

# Step 4: Add search functionality
echo "🔍 Adding search functionality..."
python3 search_generator.py

# Step 5: Copy interactive graph
echo "📊 Copying interactive graph..."
python3 copy_graph_to_pages.py

echo "✅ Deployment ready!"
echo ""
echo "📋 Next steps:"
echo "1. git add docs/"
echo "2. git commit -m 'Deploy GitHub Pages'"
echo "3. git push"
echo "4. Enable GitHub Pages in repository settings"
echo "5. Choose 'Deploy from branch' and select 'docs' folder"
echo ""
echo "Your site structure:"
echo "├── Home page with overview and statistics"
echo "├── /topics/ - Browse by subject areas"
echo "├── /tags/ - Browse by tags"
echo "├── /search/ - Full-text search"
echo "└── /graph/ - Interactive knowledge graph"