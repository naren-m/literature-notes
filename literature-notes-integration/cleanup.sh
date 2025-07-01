#!/bin/bash

# Literature Notes Integration - Cleanup Script
# Removes scattered integration files and consolidates everything in Docker

echo "🧹 Cleaning up scattered integration files..."
echo "=============================================="

# Set script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PARENT_DIR"

echo "📁 Current directory: $(pwd)"

# List of files to remove (scattered integration files)
FILES_TO_REMOVE=(
    "debug_api.py"
    "fix_api.sh"
    "generate_synthesis.py"
    "integrate_api_with_docs.py"
    "logseq_integration.py"
    "simple_api_start.py"
    "smart_query.py"
    "knowledge_synthesis.py"
    "install_requirements.sh"
    "setup_integration.sh"
    "start_docs_with_api.sh"
    "start_integration.sh"
    "stop_integration.sh"
    "run_docker.sh"
    "test_integration.py"
    "api-search.md"
    "smart-search.md"
    "markdown-viewer.html"
    "API_TROUBLESHOOTING.md"
    "DOCKER_SETUP_GUIDE.md"
    "SMART_SEARCH_SETUP.md"
    "demo_logseq_output.md"
    "logseq_plugin_template.js"
    "logseq_setup_guide.md"
)

# Directories to remove
DIRS_TO_REMOVE=(
    "assets/js"
    "api"
)

echo "🗑️ Removing scattered integration files..."

# Remove files
for file in "${FILES_TO_REMOVE[@]}"; do
    if [ -f "$file" ]; then
        echo "   Removing: $file"
        rm "$file"
    fi
done

# Remove directories
for dir in "${DIRS_TO_REMOVE[@]}"; do
    if [ -d "$dir" ]; then
        echo "   Removing directory: $dir"
        rm -rf "$dir"
    fi
done

# Move important files to Docker if not already there
echo ""
echo "📦 Ensuring important files are in Docker setup..."

# Copy database if it exists and not already in Docker data
if [ -f "zettelkasten.db" ] && [ ! -f "literature-notes-integration/data/zettelkasten.db" ]; then
    echo "   Copying database to Docker data directory"
    mkdir -p literature-notes-integration/data
    cp zettelkasten.db literature-notes-integration/data/
fi

# Create final README for Docker setup
cat > literature-notes-integration/README.md << 'EOF'
# Literature Notes Integration - Docker Setup

This directory contains the complete Literature Notes integration system in a clean, containerized setup.

## 🚀 Quick Start

1. **Start the integration:**
   ```bash
   ./start.sh
   ```

2. **Access the interfaces:**
   - Smart Search: http://localhost:4000/smart-search.html
   - Markdown Viewer: http://localhost:4000/markdown-viewer.html
   - API Health: http://localhost:8083/health

3. **Install LogSeq Extension:**
   - Copy `logseq/logseq-literature-notes-extension/` to your LogSeq plugins directory
   - Restart LogSeq and enable the plugin

## 📁 Directory Structure

```
literature-notes-integration/
├── docker/
│   ├── Dockerfile              # Container definition
│   ├── docker-compose.yml      # Service orchestration
│   └── entrypoint.sh           # Container startup script
├── scripts/
│   └── minimal_api.py          # Zero-dependency API server
├── web/
│   ├── smart-search.html       # Smart search interface
│   └── markdown-viewer.html    # Markdown note viewer
├── logseq/
│   └── logseq-literature-notes-extension/  # LogSeq plugin
├── data/                       # Database and data files
├── start.sh                    # Main startup script
└── cleanup.sh                  # Cleanup scattered files
```

## 🔧 Management Commands

```bash
# Start all services
./start.sh

# View logs
cd docker && docker-compose logs -f

# Stop services
cd docker && docker-compose stop

# Stop and remove containers
cd docker && docker-compose down

# Rebuild containers
cd docker && docker-compose up --build
```

## 🧩 LogSeq Integration

1. Copy the extension to LogSeq:
   ```bash
   cp -r logseq/logseq-literature-notes-extension ~/.logseq/plugins/
   ```

2. Restart LogSeq

3. Enable "Literature Notes Integration" in Settings → Plugins

4. Use `/Smart Search` command or toolbar button 📚

## 🧪 Testing

```bash
# Test API health
curl http://localhost:8083/health

# Test smart search
curl -X POST http://localhost:8083/smart-query \
  -H "Content-Type: application/json" \
  -d '{"query":"philosophy"}'

# View statistics
curl http://localhost:8083/stats
```

## 🛠️ Customization

- **API Port**: Edit `docker/docker-compose.yml` to change port 8083
- **Web Port**: Edit `docker/docker-compose.yml` to change port 4000
- **Database**: Mount your existing `zettelkasten.db` in docker-compose.yml
- **LogSeq Settings**: Configure API URL in LogSeq plugin settings

## 📊 Features

### Smart Search System
- Natural language query processing
- Cross-domain knowledge discovery
- Relevance scoring and ranking
- Real-time search suggestions

### LogSeq Integration
- Seamless search within LogSeq
- Insert literature notes directly
- Toolbar integration
- Slash commands

### Web Interface
- GitHub-style markdown rendering
- Interactive note viewer
- Smart search with filters
- API statistics dashboard

All integration files are now properly organized in this Docker setup!
EOF

echo ""
echo "✅ Cleanup completed!"
echo "===================="
echo ""
echo "📦 All integration files are now organized in:"
echo "   literature-notes-integration/"
echo ""
echo "🚀 To start the integration:"
echo "   cd literature-notes-integration"
echo "   ./start.sh"
echo ""
echo "🧩 To install LogSeq extension:"
echo "   cp -r literature-notes-integration/logseq/logseq-literature-notes-extension ~/.logseq/plugins/"
echo ""
echo "🧹 Scattered files have been removed from the main directory"