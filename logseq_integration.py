#!/usr/bin/env python3
"""
LogSeq Integration for Literature Notes
Syncs knowledge synthesis and smart queries with LogSeq's graph visualization
"""

import json
import sqlite3
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple
import re
from knowledge_synthesis import KnowledgeSynthesizer

class LogSeqIntegrator:
    """Integrates literature notes with LogSeq for enhanced visualization and workflow"""
    
    def __init__(self, 
                 notes_db_path: str = "zettelkasten.db",
                 logseq_dir: str = "logseq"):
        self.db_path = notes_db_path
        self.logseq_dir = Path(logseq_dir)
        self.pages_dir = self.logseq_dir / "pages"
        self.journals_dir = self.logseq_dir / "journals"
        
        # Ensure directories exist
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        self.journals_dir.mkdir(parents=True, exist_ok=True)
        
        self.synthesizer = KnowledgeSynthesizer()
    
    def sync_knowledge_graph(self):
        """Sync the knowledge graph to LogSeq format for visualization"""
        
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # Create knowledge graph page
        graph_content = """# Knowledge Graph
#graph #meta #visualization

This page provides an overview of knowledge connections discovered through synthesis.

## Graph Overview
- **Total Notes**: {total_notes}
- **Total Connections**: {total_connections} 
- **Knowledge Clusters**: {clusters}
- **Last Updated**: {timestamp}

## Cross-Domain Bridges
{bridges}

## Knowledge Clusters
{clusters_detail}

## Query Insights
Use these LogSeq queries to explore your knowledge:

```clojure
{{{{query (and [[programming]] [[philosophy]])}}}}
```

```clojure
{{{{query (page-tags #sanskrit #ayurveda)}}}}
```

```clojure
{{{{query (and (page-property :type "synthesis") (between [[7d ago]] [[today]]))}}}}
```

## Smart Search Integration
- Use `/smart-query` command to trigger enhanced search
- Daily synthesis appears in journal pages
- Cross-references maintained automatically
"""
        
        # Get statistics
        cursor = conn.execute("SELECT COUNT(*) as count FROM notes")
        total_notes = cursor.fetchone()['count']
        
        cursor = conn.execute("SELECT COUNT(*) as count FROM links")
        total_connections = cursor.fetchone()['count']
        
        # Generate cross-domain insights
        domains = ['programming', 'sanskrit', 'ayurveda', 'cryptography', 'leadership']
        bridges_text = []
        
        for i, domain1 in enumerate(domains):
            for domain2 in domains[i+1:]:
                try:
                    insights = self.synthesizer.find_cross_domain_insights(domain1, domain2)
                    if insights['bridge_notes']:
                        bridges_text.append(f"### [[{domain1}]] ↔ [[{domain2}]]")
                        bridges_text.append(f"- **Bridge Notes**: {len(insights['bridge_notes'])}")
                        for note in insights['bridge_notes'][:3]:
                            bridges_text.append(f"  - [[{note['title']}]]")
                        bridges_text.append("")
                except:
                    continue
        
        # Format the content
        formatted_content = graph_content.format(
            total_notes=total_notes,
            total_connections=total_connections,
            clusters="Auto-discovered",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
            bridges="\n".join(bridges_text) if bridges_text else "No cross-domain bridges found yet.",
            clusters_detail="Generated dynamically from daily synthesis"
        )
        
        # Write to LogSeq
        graph_page = self.pages_dir / "Knowledge Graph.md"
        with open(graph_page, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        conn.close()
        return str(graph_page)
    
    def create_synthesis_journal_entry(self, synthesis: Dict = None):
        """Create a LogSeq journal entry with daily synthesis"""
        
        if not synthesis:
            synthesis = self.synthesizer.generate_daily_synthesis()
        
        today = datetime.now()
        journal_file = self.journals_dir / f"{today.strftime('%Y_%m_%d')}.md"
        
        # Create journal entry content
        journal_content = f"""# {today.strftime('%B %d, %Y')}
#daily #synthesis #auto-generated

## 🧠 Knowledge Synthesis
*Auto-generated connections and insights*

"""
        
        for i, group in enumerate(synthesis['groups'], 1):
            journal_content += f"### Cluster {i}: {group['theme']}\n"
            journal_content += "- **Connected Notes**:\n"
            for note in group['notes']:
                # Convert to LogSeq page reference
                page_ref = self._convert_to_logseq_page_ref(note['title'])
                journal_content += f"  - [[{page_ref}]]\n"
            
            if group['connections']:
                journal_content += "- **Knowledge Flow**:\n"
                for conn in group['connections']:
                    from_ref = self._convert_to_logseq_page_ref(conn['from'])
                    to_ref = self._convert_to_logseq_page_ref(conn['to'])
                    journal_content += f"  - [[{from_ref}]] → [[{to_ref}]]\n"
            journal_content += "\n"
        
        # Add insights
        if synthesis.get('insights'):
            journal_content += "## 💡 Insights\n"
            for insight in synthesis['insights']:
                journal_content += f"- {insight}\n"
            journal_content += "\n"
        
        # Add explorations
        if synthesis.get('suggested_explorations'):
            journal_content += "## 🎯 Explore Next\n"
            for suggestion in synthesis['suggested_explorations']:
                journal_content += f"- {suggestion}\n"
            journal_content += "\n"
        
        # Add properties for LogSeq
        journal_content += """
## Properties
type:: synthesis
generated:: auto
source:: literature-notes
clusters:: """ + str(len(synthesis['groups'])) + """

## Smart Queries
Try these in LogSeq query box:
- `{{query (and [[programming]] [[sanskrit]])}}` - Find connections between programming and Sanskrit
- `{{query (page-tags #synthesis)}}` - All synthesis entries
- `{{query (page-property :type "synthesis")}}` - Auto-generated insights
"""
        
        # Write journal entry
        with open(journal_file, 'w', encoding='utf-8') as f:
            f.write(journal_content)
        
        return str(journal_file)
    
    def create_smart_query_page(self, query: str, results: List[Dict]):
        """Create a LogSeq page for smart query results"""
        
        # Create page name from query
        page_name = f"Query - {query[:50]}"
        safe_name = re.sub(r'[^\w\s-]', '', page_name).strip()
        
        page_content = f"""# {page_name}
#query #search #auto-generated

**Query**: `{query}`
**Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Results**: {len(results)} notes found

## Results

"""
        
        for i, result in enumerate(results, 1):
            page_ref = self._convert_to_logseq_page_ref(result['title'])
            page_content += f"### {i}. [[{page_ref}]]\n"
            
            # Add metadata
            if result.get('tags'):
                tags = result['tags'] if isinstance(result['tags'], list) else json.loads(result['tags'])
                page_content += f"**Tags**: {', '.join(f'#{tag}' for tag in tags)}\n"
            
            if result.get('relevance_score'):
                page_content += f"**Relevance**: {result['relevance_score']}\n"
            
            if result.get('connection_strength'):
                page_content += f"**Connection Strength**: {result['connection_strength']}\n"
            
            # Add content preview
            content_preview = result.get('content', '')[:200] + "..." if len(result.get('content', '')) > 200 else result.get('content', '')
            page_content += f"**Preview**: {content_preview}\n\n"
        
        # Add related queries
        page_content += """## Related Queries
- `{{query (page-tags #programming)}}` - All programming notes
- `{{query (page-tags #sanskrit)}}` - All Sanskrit notes  
- `{{query (page-tags #synthesis)}}` - All synthesis results
"""
        
        # Write page
        page_file = self.pages_dir / f"{safe_name}.md"
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        return str(page_file)
    
    def sync_note_as_logseq_page(self, note_path: str):
        """Convert a literature note to LogSeq page format"""
        
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.execute("SELECT * FROM notes WHERE path = ?", (note_path,))
        note = cursor.fetchone()
        
        if not note:
            conn.close()
            return None
        
        # Convert to LogSeq format
        page_name = self._convert_to_logseq_page_ref(note['title'])
        
        # Process content to add LogSeq enhancements
        content = note['content']
        
        # Convert [[wikilinks]] to LogSeq format (they're already compatible)
        # Add block references and enhance with LogSeq features
        
        logseq_content = f"""# {note['title']}

{content}

## Metadata
- **Source**: literature-notes
- **Word Count**: {note.get('word_count', 0)}
- **Created**: {note.get('created', 'Unknown')}
- **Modified**: {note.get('modified', 'Unknown')}

## Connections
"""
        
        # Add backlinks
        if note['backlinks']:
            backlinks = json.loads(note['backlinks']) if isinstance(note['backlinks'], str) else note['backlinks']
            logseq_content += "### Backlinks\n"
            for backlink in backlinks:
                ref = self._convert_to_logseq_page_ref(backlink)
                logseq_content += f"- [[{ref}]]\n"
        
        # Add forward links
        if note['wikilinks']:
            wikilinks = json.loads(note['wikilinks']) if isinstance(note['wikilinks'], str) else note['wikilinks']
            logseq_content += "### Links to\n"
            for link in wikilinks:
                ref = self._convert_to_logseq_page_ref(link)
                logseq_content += f"- [[{ref}]]\n"
        
        # Add tags
        if note['tags']:
            tags = json.loads(note['tags']) if isinstance(note['tags'], str) else note['tags']
            logseq_content += f"\n**Tags**: {', '.join(f'#{tag}' for tag in tags)}\n"
        
        # Write to LogSeq pages
        page_file = self.pages_dir / f"{page_name}.md"
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(logseq_content)
        
        conn.close()
        return str(page_file)
    
    def create_custom_logseq_queries(self):
        """Create custom LogSeq queries for enhanced knowledge discovery"""
        
        queries_content = """# Custom Queries
#queries #meta #knowledge-discovery

## Knowledge Discovery Queries

### Cross-Domain Connections
```clojure
{:title "Programming + Sanskrit Connections"
 :query [:find (pull ?p [*])
         :where
         [?p :page/tags ?t1]
         [?p :page/tags ?t2]
         [(= ?t1 "programming")]
         [(= ?t2 "sanskrit")]]
 :result-transform (fn [result]
                     (sort-by :page/created-at result))
 :collapsed? false}
```

### Recent Synthesis
```clojure
{:title "Recent Knowledge Synthesis"
 :query [:find (pull ?p [*])
         :where
         [?p :page/properties ?props]
         [(get ?props :type) ?type]
         [(= ?type "synthesis")]
         [?p :page/journal-day ?d]
         [(> ?d 20231201)]]
 :result-transform (fn [result]
                     (sort-by :page/journal-day > result))
 :collapsed? false}
```

### High-Connection Notes
```clojure
{:title "Knowledge Hubs (Highly Connected)"
 :query [:find (pull ?p [*]) (count ?b)
         :where
         [?b :block/refs ?p]
         [?p :page/name]]
 :result-transform (fn [result]
                     (->> result
                          (sort-by second >)
                          (take 20)))
 :collapsed? false}
```

### Domain Clusters
```clojure
{:title "Ayurveda Knowledge Cluster"
 :query [:find (pull ?p [*])
         :where
         (or [?p :page/tags "ayurveda"]
             [?p :page/tags "health"]
             [?p :page/tags "wellness"]
             [?p :page/name "Ayurveda"])]
 :result-transform (fn [result]
                     (sort-by :page/name result))
 :collapsed? false}
```

### Smart Search Integration
```clojure
{:title "Auto-Generated Content"
 :query [:find (pull ?p [*])
         :where
         [?p :page/tags "auto-generated"]]
 :result-transform (fn [result]
                     (sort-by :page/created-at > result))
 :collapsed? false}
```

## Usage Instructions

1. **Copy queries to LogSeq**: Paste these in your LogSeq queries page
2. **Customize parameters**: Modify tags and dates as needed  
3. **Create shortcuts**: Use LogSeq's slash commands to trigger queries
4. **Graph exploration**: Use results to explore the knowledge graph

## Advanced Queries

### Concept Evolution
Track how your understanding of concepts evolves over time:

```clojure
{:title "Concept Evolution: Memory"
 :query [:find (pull ?p [*])
         :where
         (or [?p :page/name "Memory Palace"]
             [?p :page/name "Memory"]
             [?p :page/tags "memory"])]
 :result-transform (fn [result]
                     (sort-by :page/created-at result))
 :collapsed? false}
```

### Cross-Cultural Insights
Find connections between Eastern and Western concepts:

```clojure
{:title "East-West Knowledge Bridges"
 :query [:find (pull ?p [*])
         :where
         [?p :page/tags ?eastern]
         [?p :page/tags ?western]
         [(contains? #{"sanskrit" "ayurveda" "yoga" "vedanta"} ?eastern)]
         [(contains? #{"programming" "science" "philosophy" "psychology"} ?western)]]
 :collapsed? false}
```
"""
        
        # Write queries page
        queries_file = self.pages_dir / "Custom Queries.md"
        with open(queries_file, 'w', encoding='utf-8') as f:
            f.write(queries_content)
        
        return str(queries_file)
    
    def _convert_to_logseq_page_ref(self, title: str) -> str:
        """Convert a note title to LogSeq page reference format"""
        # LogSeq is flexible with page names, but clean them up
        return title.replace('.md', '').strip()
    
    def create_logseq_plugin_config(self):
        """Create configuration for LogSeq integration"""
        
        plugin_config = {
            "smartQuery": {
                "enabled": True,
                "apiEndpoint": "http://localhost:8000/smart-query",
                "autoSync": True,
                "dailySynthesis": True
            },
            "knowledgeGraph": {
                "showClusters": True,
                "highlightBridges": True,
                "autoUpdate": "daily"
            },
            "customCommands": [
                {
                    "name": "smart-query",
                    "description": "Run smart query on literature notes",
                    "shortcut": "/sq"
                },
                {
                    "name": "daily-synthesis", 
                    "description": "Generate daily knowledge synthesis",
                    "shortcut": "/ds"
                }
            ]
        }
        
        config_file = self.logseq_dir / "plugins" / "literature-notes-integration.json"
        config_file.parent.mkdir(exist_ok=True)
        
        with open(config_file, 'w') as f:
            json.dump(plugin_config, f, indent=2)
        
        return str(config_file)


def main():
    """Main integration function"""
    print("🔗 Integrating Literature Notes with LogSeq...")
    
    integrator = LogSeqIntegrator()
    
    try:
        # Sync knowledge graph
        graph_file = integrator.sync_knowledge_graph()
        print(f"✅ Knowledge graph synced: {graph_file}")
        
        # Create daily synthesis
        synthesis_file = integrator.create_synthesis_journal_entry()
        print(f"✅ Daily synthesis created: {synthesis_file}")
        
        # Create custom queries
        queries_file = integrator.create_custom_logseq_queries()
        print(f"✅ Custom queries created: {queries_file}")
        
        # Create plugin config
        plugin_file = integrator.create_logseq_plugin_config()
        print(f"✅ Plugin config created: {plugin_file}")
        
        print("\n🎉 LogSeq integration complete!")
        print("\n📋 Next Steps:")
        print("1. Open LogSeq and check the new pages")
        print("2. Use the custom queries to explore connections") 
        print("3. Check today's journal for synthesis insights")
        print("4. Explore the Knowledge Graph page")
        print("5. Use `/sq` command for smart queries (when plugin is available)")
        
        # Show some sample queries
        print("\n🔍 Try these LogSeq queries:")
        print("- {{query (page-tags #programming #sanskrit)}}")
        print("- {{query (page-property :type 'synthesis')}}")
        print("- {{query (and [[Knowledge Graph]] (page-tags #visualization))}}")
        
    except Exception as e:
        print(f"❌ Error during integration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()