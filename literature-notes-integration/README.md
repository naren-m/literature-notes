# Literature Notes Integration Suite

A comprehensive integration system that enhances your literature notes with smart search, knowledge synthesis, and LogSeq visualization capabilities.

## 🎯 Overview

This integration transforms your static literature notes into a dynamic, intelligent knowledge system with:

- **Smart Query System** - Natural language search with concept bridging
- **Knowledge Synthesis** - Automatic discovery of connections and insights  
- **LogSeq Integration** - Visual graph exploration and enhanced workflows
- **Daily Synthesis** - Automated knowledge discovery and reporting
- **Cross-Domain Analysis** - Find unexpected connections between different fields

## 📁 Directory Structure

```
literature-notes-integration/
├── scripts/           # Core integration scripts
├── web/              # Web interface components  
├── logseq/           # LogSeq plugins and templates
├── config/           # Configuration files
├── docker/           # Docker containerization
├── docs/             # Documentation and guides
└── README.md         # This file
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Start the integration server
./start_integration.sh

# Access web interface
open http://localhost:8080
```

### Option 2: Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run smart query
python scripts/smart_query.py "connections between sanskrit and programming"

# Generate daily synthesis
python scripts/generate_synthesis.py
```

## 🔧 Components

### Core Scripts (`scripts/`)
- `smart_query.py` - Natural language query processor
- `knowledge_synthesis.py` - Connection discovery and synthesis
- `logseq_integration.py` - LogSeq synchronization
- `generate_synthesis.py` - Daily insight generation

### Web Interface (`web/`)
- `smart-search.md` - Enhanced search interface
- Static assets and API endpoints

### LogSeq Integration (`logseq/`)
- `logseq_plugin_template.js` - Plugin for enhanced LogSeq features
- Custom queries and templates

## 📊 Features

### Smart Query System
- **Natural language queries**: "Show me connections between ayurveda and programming"
- **Concept expansion**: Automatically includes related terms
- **Cross-domain bridging**: Links ideas across different knowledge areas
- **Relevance scoring**: Ranks results by connection strength

### Knowledge Synthesis
- **Daily insights**: Automatic discovery of note connections
- **Domain analysis**: Deep-dive into specific knowledge areas
- **Cross-domain insights**: Find bridges between different fields
- **Pattern recognition**: Identify recurring themes and concepts

### LogSeq Integration
- **Visual graph**: See your knowledge as interconnected web
- **Custom queries**: Advanced exploration of your notes
- **Daily journal synthesis**: Insights appear in your daily notes
- **Plugin system**: Enhanced LogSeq workflows

## 🐳 Docker Deployment

The Docker setup provides:
- **Consistent environment** across machines
- **Isolated dependencies** 
- **Easy scaling** and deployment
- **API server** for web interface
- **Background synthesis** processing

### Docker Components
- **Web server** for smart search interface
- **API backend** for query processing
- **Database** for note indexing
- **Scheduled synthesis** jobs

## 🔗 API Endpoints

When running in Docker mode:

- `GET /` - Web interface
- `POST /api/smart-query` - Execute smart queries
- `POST /api/synthesis` - Generate knowledge synthesis
- `GET /api/graph` - Knowledge graph data
- `GET /api/domain/{domain}` - Domain analysis

## 📈 Usage Examples

### Smart Queries
```python
# Find connections between concepts
python scripts/smart_query.py "connections between meditation and programming"

# Find similar notes
python scripts/smart_query.py "similar to memory palace"

# Recent notes on topic
python scripts/smart_query.py "recent notes about cryptography"
```

### Knowledge Synthesis
```python
# Daily synthesis
python scripts/knowledge_synthesis.py daily

# Domain analysis
python scripts/knowledge_synthesis.py domain sanskrit

# Cross-domain insights
python scripts/knowledge_synthesis.py connect programming philosophy
```

### LogSeq Integration
```python
# Sync with LogSeq
python scripts/logseq_integration.py

# Generate LogSeq pages
python scripts/logseq_integration.py --create-pages

# Update knowledge graph
python scripts/logseq_integration.py --update-graph
```

## 🛠️ Configuration

### Environment Variables
```bash
NOTES_DB_PATH=/path/to/zettelkasten.db
LOGSEQ_DIR=/path/to/logseq
WEB_PORT=8080
API_HOST=0.0.0.0
DEBUG=false
```

### Config Files (`config/`)
- `smart_query_config.json` - Query processing settings
- `synthesis_config.json` - Synthesis parameters
- `logseq_config.json` - LogSeq integration settings

## 📚 Documentation

See the `docs/` directory for:
- **Setup guides** for different environments
- **Usage examples** and tutorials
- **API documentation** 
- **LogSeq integration** instructions
- **Troubleshooting** guides

## 🤝 Contributing

This integration system is designed to be:
- **Modular** - Easy to extend with new features
- **Configurable** - Adaptable to different workflows
- **Open** - Built with standard technologies

## 📄 License

MIT License - See LICENSE file for details

---

**Transform your literature notes into an intelligent knowledge discovery system!**