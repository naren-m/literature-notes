#!/usr/bin/env python3
"""
Daily Synthesis Generator
Creates daily knowledge synthesis reports automatically
"""

import json
import sqlite3
import random
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from knowledge_synthesis import KnowledgeSynthesizer, generate_synthesis_report

def create_daily_synthesis_page():
    """Create a daily synthesis page and update the website"""
    
    # Generate synthesis
    synthesizer = KnowledgeSynthesizer()
    synthesis = synthesizer.generate_daily_synthesis(num_notes=8)
    
    # Create markdown content
    date_str = datetime.now().strftime('%Y-%m-%d')
    synthesis_content = f"""---
layout: default
title: Daily Synthesis - {date_str}
tags: [synthesis, daily, auto-generated]
---

# Daily Knowledge Synthesis
*Auto-generated on {datetime.now().strftime('%B %d, %Y')}*

Welcome to your personalized knowledge synthesis! This page highlights interesting connections and patterns in your notes.

## 🔗 Discovered Connections

"""
    
    for i, group in enumerate(synthesis['groups'], 1):
        synthesis_content += f"### {i}. {group['theme']}\n\n"
        
        # Add note list
        synthesis_content += "**Connected Notes:**\n"
        for note in group['notes']:
            # Create clean title and path
            title = note['title']
            # Convert path to URL-friendly format
            url_path = note['path'].replace('.md', '').replace(' ', '-').lower()
            synthesis_content += f"- [{title}](/{url_path}/)\n"
        
        # Add connections if any
        if group['connections']:
            synthesis_content += "\n**Knowledge Flows:**\n"
            for conn in group['connections']:
                synthesis_content += f"- {conn['from']} → {conn['to']}\n"
        
        synthesis_content += "\n"
    
    # Add insights section
    if synthesis.get('insights'):
        synthesis_content += "## 💡 Insights\n\n"
        for insight in synthesis['insights']:
            synthesis_content += f"- {insight}\n"
        synthesis_content += "\n"
    
    # Add exploration suggestions
    if synthesis.get('suggested_explorations'):
        synthesis_content += "## 🎯 Suggested Explorations\n\n"
        for suggestion in synthesis['suggested_explorations']:
            synthesis_content += f"- {suggestion}\n"
        synthesis_content += "\n"
    
    # Add quick concept summary
    synthesis_content += """## 🗺️ Quick Actions

- **[Smart Search](/smart-search/)** - Use natural language to explore your knowledge
- **[Knowledge Graph](/graph/)** - Visualize connections between your notes  
- **[Browse by Tags](/tags/)** - Explore your knowledge by categories

## 📊 Synthesis Stats

"""
    
    total_notes = sum(len(group['notes']) for group in synthesis['groups'])
    total_connections = sum(len(group['connections']) for group in synthesis['groups'])
    
    synthesis_content += f"- **Notes analyzed:** {total_notes}\n"
    synthesis_content += f"- **Connections found:** {total_connections}\n"
    synthesis_content += f"- **Knowledge clusters:** {len(synthesis['groups'])}\n"
    
    # Add footer
    synthesis_content += f"""
---

*This synthesis was automatically generated from your literature notes. It highlights patterns and connections that might not be immediately obvious when browsing individual notes.*

**Next synthesis:** Tomorrow at the same time  
**Previous synthesis:** [Browse synthesis archive](/synthesis-archive/)
"""
    
    # Save the synthesis page
    filename = f"daily-synthesis.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(synthesis_content)
    
    # Also create an archive entry
    archive_filename = f"synthesis-archive/{date_str}.md"
    import os
    os.makedirs('synthesis-archive', exist_ok=True)
    
    archive_content = synthesis_content.replace('title: Daily Synthesis', f'title: Synthesis Archive - {date_str}')
    with open(archive_filename, 'w', encoding='utf-8') as f:
        f.write(archive_content)
    
    return filename, archive_filename

def create_synthesis_index():
    """Create an index page for all synthesis reports"""
    
    index_content = """---
layout: default
title: Knowledge Synthesis Archive
---

# Knowledge Synthesis Archive

This archive contains daily synthesis reports that automatically discover connections and patterns in your literature notes.

## Latest Synthesis

- **[Today's Synthesis](/daily-synthesis/)** - Fresh insights from your knowledge base

## What is Knowledge Synthesis?

Knowledge synthesis automatically analyzes your notes to:

- **Find hidden connections** between different topics and domains
- **Identify knowledge clusters** where multiple notes relate to the same theme  
- **Suggest exploration paths** for expanding your understanding
- **Highlight cross-domain insights** linking diverse areas of knowledge

## Archive

"""
    
    # List archived synthesis reports (if any exist)
    import os
    import glob
    
    if os.path.exists('synthesis-archive'):
        archive_files = sorted(glob.glob('synthesis-archive/*.md'), reverse=True)
        
        for archive_file in archive_files[:30]:  # Show last 30 days
            date_part = os.path.basename(archive_file).replace('.md', '')
            try:
                date_obj = datetime.strptime(date_part, '%Y-%m-%d')
                readable_date = date_obj.strftime('%B %d, %Y')
                index_content += f"- [{readable_date}](/synthesis-archive/{date_part}/)\n"
            except ValueError:
                continue
    else:
        index_content += "*No archived synthesis reports yet. Run the synthesis generator to create your first report.*\n"
    
    # Add instructions
    index_content += """

## How to Generate Synthesis

To generate a new synthesis report:

```bash
python generate_synthesis.py
```

This will analyze your current notes and create a fresh synthesis highlighting new connections and insights.

## Automation

You can automate daily synthesis by adding this to your cron jobs:

```bash
# Run daily synthesis at 9 AM
0 9 * * * cd /path/to/literature-notes && python generate_synthesis.py
```

---

*Knowledge synthesis helps you see the forest, not just the trees. By surfacing connections between your notes, it transforms your collection from a static archive into a dynamic thinking tool.*
"""
    
    with open('synthesis-archive.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    # Also create the directory index
    os.makedirs('synthesis-archive', exist_ok=True)
    with open('synthesis-archive/index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

def update_main_navigation():
    """Update the main site to include synthesis links"""
    
    # Check if index.md exists and add synthesis link
    try:
        with open('index.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add synthesis section if not already present
        if 'Daily Synthesis' not in content and 'Knowledge Synthesis' not in content:
            synthesis_section = """
## 🧠 Knowledge Synthesis

- **[Today's Synthesis](/daily-synthesis/)** - Discover connections in your knowledge
- **[Smart Search](/smart-search/)** - Advanced search with natural language
- **[Synthesis Archive](/synthesis-archive/)** - Browse past insights

"""
            
            # Insert after the first heading or at the end
            if '\n##' in content:
                # Insert before the first section
                parts = content.split('\n##', 1)
                content = parts[0] + synthesis_section + '\n##' + parts[1]
            else:
                content += synthesis_section
            
            with open('index.md', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Updated main navigation with synthesis links")
    
    except FileNotFoundError:
        print("ℹ️  Main index.md not found, skipping navigation update")

def main():
    """Main function to generate daily synthesis"""
    print("🧠 Generating daily knowledge synthesis...")
    
    try:
        # Create synthesis pages
        main_file, archive_file = create_daily_synthesis_page()
        print(f"✅ Created daily synthesis: {main_file}")
        print(f"✅ Archived synthesis: {archive_file}")
        
        # Create synthesis archive index
        create_synthesis_index()
        print("✅ Updated synthesis archive index")
        
        # Update main navigation
        update_main_navigation()
        
        # Generate some stats
        synthesizer = KnowledgeSynthesizer()
        
        print("\n📊 Synthesis Statistics:")
        
        # Quick domain analysis
        domains = ['ayurveda', 'programming', 'sanskrit', 'cryptography', 'leadership']
        for domain in domains:
            try:
                summary = synthesizer.generate_domain_summary(domain, max_notes=5)
                if summary['note_count'] > 0:
                    print(f"  • {domain.capitalize()}: {summary['note_count']} notes, {summary['total_words']} words")
            except:
                continue
        
        print(f"\n🎉 Daily synthesis complete! View at: /daily-synthesis/")
        print(f"💡 Try the enhanced search at: /smart-search/")
        
    except Exception as e:
        print(f"❌ Error generating synthesis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()