#!/bin/bash

# Literature Notes Integration Setup Script
# Creates organized directory structure and moves integration files

echo "🚀 Setting up Literature Notes Integration..."

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p literature-notes-integration/{scripts,config,docs,docker,web,logseq}

# Move integration scripts
echo "📦 Moving integration scripts..."
mv smart_query.py literature-notes-integration/scripts/
mv knowledge_synthesis.py literature-notes-integration/scripts/
mv logseq_integration.py literature-notes-integration/scripts/
mv generate_synthesis.py literature-notes-integration/scripts/

# Move web components
echo "🌐 Moving web components..."
mv smart-search.md literature-notes-integration/web/

# Move LogSeq components  
echo "🧠 Moving LogSeq components..."
mv logseq_plugin_template.js literature-notes-integration/logseq/
mv logseq_setup_guide.md literature-notes-integration/docs/
mv demo_logseq_output.md literature-notes-integration/docs/

echo "✅ Integration files organized!"
echo "📍 Location: ./literature-notes-integration/"