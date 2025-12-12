#!/usr/bin/env python3
"""
Build Knowledge Forest
Processes existing notes and builds the knowledge forest structure.
Integrates with existing zettelkasten.py infrastructure.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from knowledge_forest import KnowledgeForest
from zettelkasten import ZettelkastenDB

def build_knowledge_forest(notes_dir: str = ".", db_path: str = "zettelkasten.db", output_file: str = "forest_data.json"):
    """Build knowledge forest from existing notes"""
    
    print("🌱 Building Knowledge Forest...")
    
    # Step 1: Update the zettelkasten database
    print("📚 Updating notes database...")
    try:
        # Import and use existing zettelkasten indexing
        db = ZettelkastenDB(db_path)
        
        # Index all markdown files
        indexed_count = 0
        for md_file in Path(notes_dir).rglob("*.md"):
            if md_file.name != "README.md" and "/.git/" not in str(md_file):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract title from first heading or filename
                    title = extract_title(content, md_file.name)
                    
                    # Extract tags and wikilinks
                    tags = extract_tags(content)
                    wikilinks = extract_wikilinks(content)
                    
                    # Update database
                    db.add_note(
                        path=str(md_file),
                        title=title,
                        content=content,
                        tags=tags,
                        wikilinks=wikilinks
                    )
                    indexed_count += 1
                    
                except Exception as e:
                    print(f"⚠️ Error processing {md_file}: {e}")
        
        print(f"✅ Indexed {indexed_count} notes")
        
    except Exception as e:
        print(f"❌ Error updating database: {e}")
        sys.exit(1)
    
    # Step 2: Build the knowledge forest
    print("🌳 Building knowledge forest...")
    try:
        forest = KnowledgeForest(db_path)
        print(f"✅ Created forest with {len(forest.nodes)} nodes and {len(forest.pathways)} pathways")
        
    except Exception as e:
        print(f"❌ Error building forest: {e}")
        sys.exit(1)
    
    # Step 3: Generate summary
    print("📊 Generating forest summary...")
    summary = forest.generate_forest_summary()
    
    print("\n🌟 Knowledge Forest Summary:")
    print(f"   📝 Total Notes: {summary['total_nodes']}")
    print(f"   🔗 Total Connections: {summary['total_pathways']}")
    print(f"   🎯 Clusters: {summary['total_clusters']}")
    print(f"   📊 Node Types: {summary['node_types']}")
    print(f"   🔢 Avg Connections/Note: {summary['avg_connections_per_node']}")
    
    if summary['most_connected_nodes']:
        print("\n🏆 Most Connected Notes:")
        for i, node in enumerate(summary['most_connected_nodes'][:3], 1):
            print(f"   {i}. {node['title']} ({node['connections']} connections)")
    
    # Step 4: Export forest data
    print(f"\n💾 Exporting forest data to {output_file}...")
    forest_data = forest.export_forest_data()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(forest_data, f, indent=2, default=str)
    
    print("✅ Forest data exported successfully!")
    
    # Step 5: Generate sample pathways
    print("\n🛤️ Sample Pathways:")
    sample_nodes = list(forest.nodes.keys())[:3]
    for node_id in sample_nodes:
        node = forest.nodes[node_id]
        pathways = forest.find_pathways(node_id, max_depth=2)
        
        print(f"\n   From '{node.title}':")
        for i, pathway in enumerate(pathways[:2], 1):
            path_titles = [n.title for n in pathway['nodes']]
            print(f"     {i}. {' → '.join(path_titles)} (strength: {pathway['strength']:.2f})")
    
    return forest_data

def extract_title(content: str, filename: str) -> str:
    """Extract title from content or filename"""
    lines = content.split('\n')
    
    # Look for first heading
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    
    # Fallback to filename without extension
    return Path(filename).stem.replace('-', ' ').replace('_', ' ').title()

def extract_tags(content: str) -> list:
    """Extract tags from content"""
    tags = []
    
    # Look for hashtags
    import re
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, content)
    tags.extend(hashtags)
    
    # Look for yaml frontmatter tags
    if content.startswith('---'):
        try:
            parts = content.split('---', 2)
            if len(parts) >= 2:
                frontmatter = parts[1]
                # Simple tag extraction from YAML
                for line in frontmatter.split('\n'):
                    if line.strip().startswith('tags:'):
                        tag_line = line.split(':', 1)[1].strip()
                        if tag_line.startswith('[') and tag_line.endswith(']'):
                            # Parse as list
                            tag_line = tag_line[1:-1]
                            yaml_tags = [t.strip().strip('"\'') for t in tag_line.split(',')]
                            tags.extend(yaml_tags)
        except:
            pass
    
    return list(set(tags))  # Remove duplicates

def extract_wikilinks(content: str) -> list:
    """Extract wikilinks from content"""
    import re
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    return matches

def create_sample_web_data(forest_data: dict, output_file: str = "sample_forest_data.js"):
    """Create a sample data file for the web interface"""
    
    # Convert to JavaScript format for the web interface
    js_content = f"""
// Sample Knowledge Forest Data
// Generated from your literature notes
const FOREST_DATA = {json.dumps(forest_data, indent=2, default=str)};

// Function to load data (replace with actual API call)
function loadForestData() {{
    return Promise.resolve(FOREST_DATA);
}}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ Sample web data created: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Build Knowledge Forest from literature notes')
    parser.add_argument('--notes-dir', default='.', help='Directory containing markdown notes')
    parser.add_argument('--db-path', default='zettelkasten.db', help='Path to SQLite database')
    parser.add_argument('--output', default='forest_data.json', help='Output JSON file')
    parser.add_argument('--web-data', action='store_true', help='Create sample web data file')
    parser.add_argument('--explore', type=str, help='Explore pathways from a specific note')
    parser.add_argument('--recommend', type=str, help='Get recommendations for a specific note')
    
    args = parser.parse_args()
    
    # Build the forest
    forest_data = build_knowledge_forest(args.notes_dir, args.db_path, args.output)
    
    # Create web data if requested
    if args.web_data:
        create_sample_web_data(forest_data, "sample_forest_data.js")
    
    # Handle exploration commands
    if args.explore or args.recommend:
        forest = KnowledgeForest(args.db_path)
        
        if args.explore:
            node_id = find_node_id(forest, args.explore)
            if node_id:
                print(f"\n🧭 Exploring from '{args.explore}':")
                pathways = forest.find_pathways(node_id, max_depth=3)
                
                for i, pathway in enumerate(pathways[:5], 1):
                    path_titles = [n.title for n in pathway['nodes']]
                    print(f"   {i}. {' → '.join(path_titles)}")
                    print(f"      Strength: {pathway['strength']:.2f}, Depth: {pathway['depth']}")
            else:
                print(f"❌ Note '{args.explore}' not found")
        
        if args.recommend:
            node_id = find_node_id(forest, args.recommend)
            if node_id:
                print(f"\n💡 Recommendations for '{args.recommend}':")
                recommendations = forest.get_node_recommendations(node_id, 5)
                
                for i, rec in enumerate(recommendations, 1):
                    print(f"   {i}. {rec['node'].title}")
                    print(f"      Reason: {rec['reason']}")
                    print(f"      Type: {rec['pathway_type']}, Strength: {rec['strength']:.2f}")
            else:
                print(f"❌ Note '{args.recommend}' not found")
    
    print(f"\n🎉 Knowledge Forest is ready!")
    print(f"   📊 Open forest_data.json to see the complete structure")
    print(f"   🌐 Open knowledge_forest_navigator.html in your browser to explore")
    print(f"   🔧 Run 'python knowledge_forest.py --help' for more options")

def find_node_id(forest: KnowledgeForest, title_or_id: str) -> str:
    """Find node ID by title or exact ID"""
    # Try exact ID first
    if title_or_id in forest.nodes:
        return title_or_id
    
    # Try to find by title
    for node_id, node in forest.nodes.items():
        if node.title.lower() == title_or_id.lower():
            return node_id
    
    # Try partial match
    for node_id, node in forest.nodes.items():
        if title_or_id.lower() in node.title.lower():
            return node_id
    
    return None

if __name__ == "__main__":
    main()