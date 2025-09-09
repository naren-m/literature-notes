#!/usr/bin/env python3
"""
Simple Knowledge Forest Builder
Creates a knowledge forest directly from markdown files without external dependencies.
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Optional, Tuple, Any
from datetime import datetime
import math

@dataclass
class SimpleNote:
    """Simple note representation"""
    id: str
    title: str
    path: str
    content: str
    tags: List[str]
    wikilinks: List[str]
    word_count: int

class SimpleKnowledgeForest:
    """Simplified knowledge forest builder"""
    
    def __init__(self):
        self.notes: Dict[str, SimpleNote] = {}
        self.connections: Dict[str, Dict[str, float]] = defaultdict(dict)
        self.clusters: Dict[str, List[str]] = defaultdict(list)
    
    def process_directory(self, directory: str = ".") -> Dict[str, Any]:
        """Process all markdown files in directory"""
        print("📂 Scanning markdown files...")
        
        processed_count = 0
        for md_file in Path(directory).rglob("*.md"):
            # Skip certain files
            if (md_file.name in ['README.md', 'Readme.md'] or 
                "/.git/" in str(md_file) or 
                "/node_modules/" in str(md_file)):
                continue
            
            try:
                note = self._process_file(md_file)
                if note:
                    self.notes[note.id] = note
                    processed_count += 1
                    
                    if processed_count % 50 == 0:
                        print(f"   Processed {processed_count} files...")
                        
            except Exception as e:
                print(f"⚠️  Error processing {md_file.name}: {e}")
        
        print(f"✅ Processed {processed_count} files")
        
        # Build connections
        print("🔗 Building connections...")
        self._build_connections()
        
        # Create clusters
        print("🎯 Creating clusters...")
        self._create_clusters()
        
        # Generate export data
        print("📦 Generating export data...")
        return self._export_data()
    
    def _process_file(self, file_path: Path) -> Optional[SimpleNote]:
        """Process a single markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return None
        
        if not content.strip():
            return None
        
        # Generate ID from filename
        note_id = self._path_to_id(str(file_path))
        
        # Extract title
        title = self._extract_title(content, file_path.name)
        
        # Extract tags
        tags = self._extract_tags(content)
        
        # Extract wikilinks
        wikilinks = self._extract_wikilinks(content)
        
        # Count words
        word_count = len(content.split())
        
        return SimpleNote(
            id=note_id,
            title=title,
            path=str(file_path),
            content=content,
            tags=tags,
            wikilinks=wikilinks,
            word_count=word_count
        )
    
    def _path_to_id(self, path: str) -> str:
        """Convert path to ID"""
        # Get relative path and filename without extension
        path_obj = Path(path)
        relative_parts = path_obj.parts
        
        # Create ID from directory and filename
        if len(relative_parts) > 1:
            parent_dir = relative_parts[-2] if relative_parts[-2] != '.' else ''
            filename = path_obj.stem
            if parent_dir and parent_dir != filename:
                node_id = f"{parent_dir}_{filename}"
            else:
                node_id = filename
        else:
            node_id = path_obj.stem
        
        # Clean up ID
        node_id = node_id.lower().replace(' ', '_').replace('-', '_')
        node_id = re.sub(r'[^a-z0-9_]', '', node_id)
        
        return node_id
    
    def _extract_title(self, content: str, filename: str) -> str:
        """Extract title from content"""
        lines = content.split('\n')
        
        # Look for first heading
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        
        # Fallback to filename
        return Path(filename).stem.replace('-', ' ').replace('_', ' ').title()
    
    def _extract_tags(self, content: str) -> List[str]:
        """Extract tags from content"""
        tags = set()
        
        # Extract hashtags
        hashtag_pattern = r'#(\w+)'
        hashtags = re.findall(hashtag_pattern, content)
        tags.update(hashtags)
        
        # Extract from YAML frontmatter
        if content.startswith('---'):
            try:
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    frontmatter = parts[1]
                    for line in frontmatter.split('\n'):
                        if 'tags:' in line or 'tag:' in line:
                            # Simple tag extraction
                            tag_content = line.split(':', 1)[1].strip()
                            tag_content = re.sub(r'[\[\]"\']', '', tag_content)
                            yaml_tags = [t.strip() for t in tag_content.split(',')]
                            tags.update([t for t in yaml_tags if t])
            except:
                pass
        
        return list(tags)
    
    def _extract_wikilinks(self, content: str) -> List[str]:
        """Extract wikilinks"""
        pattern = r'\[\[([^\]]+)\]\]'
        matches = re.findall(pattern, content)
        return [m.strip() for m in matches]
    
    def _build_connections(self):
        """Build connections between notes"""
        for note_id, note in self.notes.items():
            connections = self._calculate_connections(note)
            self.connections[note_id] = connections
    
    def _calculate_connections(self, note: SimpleNote) -> Dict[str, float]:
        """Calculate connections for a note"""
        connections = {}
        
        # Extract key terms
        note_terms = self._extract_key_terms(note.content)
        note_tags = set(note.tags)
        
        for other_id, other_note in self.notes.items():
            if other_id == note.id:
                continue
            
            strength = 0.0
            
            # Tag similarity
            other_tags = set(other_note.tags)
            if note_tags and other_tags:
                tag_overlap = len(note_tags & other_tags) / len(note_tags | other_tags)
                strength += tag_overlap * 0.3
            
            # Content similarity
            other_terms = self._extract_key_terms(other_note.content)
            if note_terms and other_terms:
                term_overlap = len(note_terms & other_terms) / len(note_terms | other_terms)
                strength += term_overlap * 0.4
            
            # Wikilink connections
            note_links = {link.lower() for link in note.wikilinks}
            other_title = other_note.title.lower()
            note_title = note.title.lower()
            
            if (other_title in note_links or 
                note_title in {link.lower() for link in other_note.wikilinks}):
                strength += 0.3
            
            # Keep connections above threshold
            if strength > 0.1:
                connections[other_id] = round(strength, 3)
        
        return connections
    
    def _extract_key_terms(self, content: str) -> Set[str]:
        """Extract key terms from content"""
        # Clean content
        clean_content = re.sub(r'[#*`\[\](){}"-]', ' ', content.lower())
        words = clean_content.split()
        
        # Filter meaningful terms
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 
            'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 
            'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 
            'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 
            'let', 'put', 'say', 'she', 'too', 'use', 'will', 'with',
            'this', 'that', 'from', 'they', 'have', 'been', 'more',
            'than', 'what', 'when', 'where', 'some', 'make', 'time'
        }
        
        key_terms = {
            word for word in words 
            if len(word) > 3 
            and word not in stop_words 
            and word.isalpha()
        }
        
        return key_terms
    
    def _create_clusters(self):
        """Create semantic clusters"""
        visited = set()
        cluster_id = 0
        
        for note_id in self.notes.keys():
            if note_id in visited:
                continue
            
            cluster_name = f"cluster_{cluster_id}"
            cluster_nodes = self._expand_cluster(note_id, visited)
            
            if len(cluster_nodes) > 1:  # Only keep clusters with multiple nodes
                self.clusters[cluster_name] = cluster_nodes
                cluster_id += 1
    
    def _expand_cluster(self, start_node: str, visited: Set[str], threshold: float = 0.2) -> List[str]:
        """Expand cluster using connected nodes"""
        cluster = [start_node]
        visited.add(start_node)
        queue = [start_node]
        
        while queue:
            current = queue.pop(0)
            current_connections = self.connections.get(current, {})
            
            for connected_id, strength in current_connections.items():
                if connected_id not in visited and strength >= threshold:
                    cluster.append(connected_id)
                    visited.add(connected_id)
                    queue.append(connected_id)
        
        return cluster
    
    def _classify_node_type(self, note: SimpleNote) -> str:
        """Classify node type"""
        content_lower = note.content.lower()
        
        # Practice indicators
        practice_keywords = ['practice', 'exercise', 'technique', 'method', 'steps', 'how to']
        if any(keyword in content_lower for keyword in practice_keywords):
            return 'practice'
        
        # Reference indicators
        if ('reference' in note.tags or 'bibliography' in content_lower or 
            'source:' in content_lower or 'link:' in content_lower):
            return 'reference'
        
        # Synthesis indicators
        synthesis_keywords = ['synthesis', 'summary', 'overview', 'integration']
        if any(keyword in content_lower for keyword in synthesis_keywords):
            return 'synthesis'
        
        return 'concept'
    
    def _export_data(self) -> Dict[str, Any]:
        """Export data for visualization"""
        nodes = []
        edges = []
        
        # Prepare nodes
        for note_id, note in self.notes.items():
            node_type = self._classify_node_type(note)
            connection_count = len(self.connections.get(note_id, {}))
            
            # Find which clusters this node belongs to
            node_clusters = []
            for cluster_name, cluster_nodes in self.clusters.items():
                if note_id in cluster_nodes:
                    node_clusters.append(cluster_name)
            
            nodes.append({
                'id': note_id,
                'title': note.title,
                'type': node_type,
                'tags': note.tags,
                'clusters': node_clusters,
                'connection_count': connection_count,
                'word_count': note.word_count,
                'path': note.path
            })
        
        # Prepare edges
        for source_id, connections in self.connections.items():
            for target_id, strength in connections.items():
                edges.append({
                    'source': source_id,
                    'target': target_id,
                    'strength': strength,
                    'type': 'semantic'
                })
        
        # Generate metadata
        type_counts = Counter(node['type'] for node in nodes)
        connection_counts = [node['connection_count'] for node in nodes]
        avg_connections = sum(connection_counts) / len(connection_counts) if connection_counts else 0
        
        most_connected = sorted(nodes, key=lambda x: x['connection_count'], reverse=True)[:5]
        largest_clusters = sorted(
            [(name, len(nodes_list)) for name, nodes_list in self.clusters.items()],
            key=lambda x: x[1], reverse=True
        )[:3]
        
        metadata = {
            'total_nodes': len(nodes),
            'total_edges': len(edges),
            'total_clusters': len(self.clusters),
            'node_types': dict(type_counts),
            'avg_connections_per_node': round(avg_connections, 2),
            'most_connected_nodes': [
                {
                    'title': node['title'],
                    'connections': node['connection_count'],
                    'type': node['type']
                } for node in most_connected
            ],
            'largest_clusters': [
                {'name': name, 'size': size} for name, size in largest_clusters
            ]
        }
        
        return {
            'nodes': nodes,
            'edges': edges,
            'clusters': dict(self.clusters),
            'metadata': metadata
        }

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple Knowledge Forest Builder')
    parser.add_argument('--directory', '-d', default='.', help='Directory to scan')
    parser.add_argument('--output', '-o', default='forest_data.json', help='Output file')
    parser.add_argument('--sample', '-s', action='store_true', help='Create sample for web viewer')
    
    args = parser.parse_args()
    
    print("🌱 Building Simple Knowledge Forest...")
    print(f"📂 Scanning directory: {args.directory}")
    
    forest = SimpleKnowledgeForest()
    data = forest.process_directory(args.directory)
    
    # Save main data
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved forest data to: {args.output}")
    
    # Print summary
    metadata = data['metadata']
    print("\n🌟 Knowledge Forest Summary:")
    print(f"   📝 Total Notes: {metadata['total_nodes']}")
    print(f"   🔗 Total Connections: {metadata['total_edges']}")
    print(f"   🎯 Clusters: {metadata['total_clusters']}")
    print(f"   📊 Node Types: {metadata['node_types']}")
    print(f"   🔢 Avg Connections/Note: {metadata['avg_connections_per_node']}")
    
    if metadata['most_connected_nodes']:
        print("\n🏆 Most Connected Notes:")
        for i, node in enumerate(metadata['most_connected_nodes'][:3], 1):
            print(f"   {i}. {node['title']} ({node['connections']} connections)")
    
    if metadata['largest_clusters']:
        print("\n📊 Largest Clusters:")
        for i, cluster in enumerate(metadata['largest_clusters'], 1):
            print(f"   {i}. {cluster['name']} ({cluster['size']} notes)")
    
    # Create sample data for web viewer if requested
    if args.sample:
        # Create a smaller sample for the web viewer
        sample_data = {
            'nodes': data['nodes'][:20],  # First 20 nodes
            'edges': [edge for edge in data['edges'] 
                     if edge['source'] in [n['id'] for n in data['nodes'][:20]] 
                     and edge['target'] in [n['id'] for n in data['nodes'][:20]]],
            'clusters': {k: v for k, v in data['clusters'].items() 
                        if any(node_id in [n['id'] for n in data['nodes'][:20]] for node_id in v)},
            'metadata': data['metadata']
        }
        
        sample_file = 'sample_forest_data.js'
        js_content = f"""// Sample Knowledge Forest Data
const FOREST_DATA = {json.dumps(sample_data, indent=2, ensure_ascii=False)};

// Make data available globally
window.FOREST_DATA = FOREST_DATA;
"""
        
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"📄 Created sample data: {sample_file}")
        print("🌐 You can now open knowledge_forest_navigator.html in your browser!")
    
    print("\n✨ Knowledge Forest is ready!")
    print("🔧 Use the data in your visualization tools or web interface.")

if __name__ == "__main__":
    main()