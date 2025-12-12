#!/usr/bin/env python3
"""
Clean Knowledge Forest Builder
Fixed version that handles duplicates and creates cleaner connections.
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
class CleanNote:
    """Clean note representation with deduplication"""
    id: str
    title: str
    canonical_path: str  # Primary path for this note
    all_paths: List[str]  # All paths that refer to this same content
    content: str
    tags: List[str]
    wikilinks: List[str]
    word_count: int
    content_hash: str  # For deduplication

class CleanKnowledgeForest:
    """Clean knowledge forest builder with deduplication"""
    
    def __init__(self):
        self.notes: Dict[str, CleanNote] = {}
        self.title_to_id: Dict[str, str] = {}  # For deduplication by title
        self.content_hash_to_id: Dict[str, str] = {}  # For deduplication by content
        self.connections: Dict[str, Dict[str, float]] = defaultdict(dict)
        self.clusters: Dict[str, List[str]] = defaultdict(list)
    
    def process_directory(self, directory: str = ".") -> Dict[str, Any]:
        """Process all markdown files in directory with deduplication"""
        print("📂 Scanning and deduplicating markdown files...")
        
        processed_count = 0
        skipped_count = 0
        
        for md_file in Path(directory).rglob("*.md"):
            # Skip certain files and directories
            if (md_file.name in ['README.md', 'Readme.md'] or 
                "/.git/" in str(md_file) or 
                "/node_modules/" in str(md_file) or
                "/logseq/bak/" in str(md_file) or  # Skip LogSeq backup files
                "/bak/" in str(md_file) or  # Skip general backup files
                "/.obsidian/" in str(md_file) or
                "/2025_" in str(md_file) or "/2024_" in str(md_file) and "desktop" in str(md_file).lower()):  # Skip timestamped backup files
                continue
            
            try:
                note = self._process_file(md_file)
                if note:
                    existing_id = self._find_duplicate(note)
                    if existing_id:
                        # Merge with existing note
                        self._merge_notes(existing_id, note)
                        skipped_count += 1
                    else:
                        # Add as new note
                        self.notes[note.id] = note
                        self.title_to_id[note.title.lower()] = note.id
                        self.content_hash_to_id[note.content_hash] = note.id
                        processed_count += 1
                    
                    if (processed_count + skipped_count) % 50 == 0:
                        print(f"   Processed {processed_count} files, merged {skipped_count} duplicates...")
                        
            except Exception as e:
                print(f"⚠️  Error processing {md_file.name}: {e}")
        
        print(f"✅ Processed {processed_count} unique files, merged {skipped_count} duplicates")
        
        # Build connections
        print("🔗 Building connections...")
        self._build_connections()
        
        # Create clusters
        print("🎯 Creating clusters...")
        self._create_clusters()
        
        # Generate export data
        print("📦 Generating export data...")
        return self._export_data()
    
    def _process_file(self, file_path: Path) -> Optional[CleanNote]:
        """Process a single markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return None
        
        if not content.strip() or len(content) < 10:  # Skip very short files
            return None
        
        # Generate clean ID from filename only (not path)
        note_id = self._filename_to_id(file_path.name)
        
        # Extract title
        title = self._extract_title(content, file_path.name)
        
        # Skip if title is too generic or just a date
        generic_titles = ['index', 'readme', 'untitled', '', 'note', 'notes', 'temp', 'test']
        if (title.lower() in generic_titles or 
            re.match(r'^\d{4}[\s_-]\d{2}[\s_-]\d{2}', title.lower()) or  # Date patterns
            len(title.strip()) < 2):
            return None
        
        # Extract tags
        tags = self._extract_tags(content)
        
        # Extract wikilinks
        wikilinks = self._extract_wikilinks(content)
        
        # Count words
        word_count = len(content.split())
        
        # Create content hash for deduplication
        content_hash = self._hash_content(content)
        
        return CleanNote(
            id=note_id,
            title=title,
            canonical_path=str(file_path),
            all_paths=[str(file_path)],
            content=content,
            tags=tags,
            wikilinks=wikilinks,
            word_count=word_count,
            content_hash=content_hash
        )
    
    def _filename_to_id(self, filename: str) -> str:
        """Convert filename to clean ID"""
        # Remove extension and clean up
        node_id = Path(filename).stem
        node_id = node_id.lower()
        node_id = re.sub(r'[^a-z0-9_]', '_', node_id)
        node_id = re.sub(r'_+', '_', node_id)  # Collapse multiple underscores
        node_id = node_id.strip('_')  # Remove leading/trailing underscores
        
        return node_id
    
    def _hash_content(self, content: str) -> str:
        """Create a better hash of content for deduplication"""
        # Normalize content by removing markdown formatting and extra whitespace
        normalized = re.sub(r'[#*`\[\]()-]', ' ', content.lower())
        normalized = re.sub(r'\s+', ' ', normalized.strip())
        
        # Remove common prefixes and suffixes that might vary
        normalized = re.sub(r'^(index|readme|untitled)\s*', '', normalized)
        normalized = re.sub(r'\s*(index|readme)$', '', normalized)
        
        # Use first 150 chars as hash, but ensure we have meaningful content
        if len(normalized) < 20:
            return normalized
        
        return normalized[:150] if len(normalized) > 50 else normalized
    
    def _find_duplicate(self, note: CleanNote) -> Optional[str]:
        """Find if this note is a duplicate of an existing one"""
        # Normalize title for comparison
        normalized_title = note.title.lower().strip()
        
        # Check by exact title match first
        if normalized_title in self.title_to_id:
            return self.title_to_id[normalized_title]
        
        # Check by content hash
        if note.content_hash in self.content_hash_to_id:
            return self.content_hash_to_id[note.content_hash]
        
        # Check for very similar titles (fuzzy matching)
        for existing_title, existing_id in self.title_to_id.items():
            # Remove common variations
            clean_existing = re.sub(r'\s+', ' ', existing_title.strip())
            clean_new = re.sub(r'\s+', ' ', normalized_title.strip())
            
            # Check if one is a subset of the other (handles "Index" vs "Index Page" cases)
            if (clean_existing in clean_new or clean_new in clean_existing) and abs(len(clean_existing) - len(clean_new)) < 10:
                return existing_id
            
            # Check for very high similarity (same words, different order)
            existing_words = set(clean_existing.split())
            new_words = set(clean_new.split())
            if existing_words and new_words:
                similarity = len(existing_words & new_words) / len(existing_words | new_words)
                if similarity > 0.8:  # 80% word overlap
                    return existing_id
        
        return None
    
    def _merge_notes(self, existing_id: str, new_note: CleanNote):
        """Merge new note into existing note"""
        existing_note = self.notes[existing_id]
        
        # Add the new path
        existing_note.all_paths.append(new_note.canonical_path)
        
        # Merge tags (keep unique)
        all_tags = set(existing_note.tags + new_note.tags)
        existing_note.tags = list(all_tags)
        
        # Merge wikilinks (keep unique)
        all_wikilinks = set(existing_note.wikilinks + new_note.wikilinks)
        existing_note.wikilinks = list(all_wikilinks)
        
        # Use longer content if significantly different
        if len(new_note.content) > len(existing_note.content) * 1.5:
            existing_note.content = new_note.content
            existing_note.word_count = new_note.word_count
    
    def _extract_title(self, content: str, filename: str) -> str:
        """Extract title from content"""
        lines = content.split('\n')
        
        # Look for first heading
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                if title and not title.startswith('#'):  # Avoid multiple #
                    return title
        
        # Fallback to filename
        title = Path(filename).stem.replace('-', ' ').replace('_', ' ')
        # Clean up the title
        title = re.sub(r'\d{4}[-_]\d{2}[-_]\d{2}', '', title)  # Remove dates
        title = re.sub(r'[tT]\d{2}[_:]\d{2}[_:]\d{2}', '', title)  # Remove timestamps
        title = re.sub(r'desktop', '', title, flags=re.IGNORECASE)
        title = re.sub(r'\s+', ' ', title).strip().title()
        
        return title if title else "Untitled"
    
    def _extract_tags(self, content: str) -> List[str]:
        """Extract tags from content"""
        tags = set()
        
        # Extract hashtags (but limit to reasonable ones)
        hashtag_pattern = r'#(\w+)'
        hashtags = re.findall(hashtag_pattern, content)
        # Filter out very short or numeric-only tags
        meaningful_hashtags = [tag for tag in hashtags 
                              if len(tag) > 2 and not tag.isdigit() and len(tag) < 20]
        tags.update(meaningful_hashtags[:10])  # Limit to 10 hashtags
        
        # Extract from YAML frontmatter
        if content.startswith('---'):
            try:
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    frontmatter = parts[1]
                    for line in frontmatter.split('\n'):
                        if 'tags:' in line or 'tag:' in line:
                            tag_content = line.split(':', 1)[1].strip()
                            tag_content = re.sub(r'[\[\]"\']', '', tag_content)
                            yaml_tags = [t.strip() for t in tag_content.split(',')]
                            # Filter meaningful tags
                            meaningful_tags = [t for t in yaml_tags 
                                             if t and len(t) > 2 and len(t) < 20 and not t.isdigit()]
                            tags.update(meaningful_tags[:5])  # Limit to 5 from YAML
            except:
                pass
        
        return list(tags)[:10]  # Maximum 10 tags per note
    
    def _extract_wikilinks(self, content: str) -> List[str]:
        """Extract wikilinks"""
        pattern = r'\[\[([^\]]+)\]\]'
        matches = re.findall(pattern, content)
        # Clean and filter wikilinks
        clean_links = []
        for match in matches:
            link = match.strip()
            if link and len(link) > 1 and len(link) < 50:  # Reasonable length
                clean_links.append(link)
        return clean_links[:10]  # Limit to 10 wikilinks
    
    def _build_connections(self):
        """Build clean connections between notes"""
        for note_id, note in self.notes.items():
            connections = self._calculate_connections(note)
            # Only keep stronger connections
            strong_connections = {k: v for k, v in connections.items() if v > 0.2}
            self.connections[note_id] = strong_connections
    
    def _calculate_connections(self, note: CleanNote) -> Dict[str, float]:
        """Calculate connections for a note with higher thresholds"""
        connections = {}
        
        # Extract key terms
        note_terms = self._extract_key_terms(note.content)
        note_tags = set(note.tags)
        
        for other_id, other_note in self.notes.items():
            if other_id == note.id:
                continue
            
            strength = 0.0
            
            # 1. Strong tag overlap (higher weight)
            other_tags = set(other_note.tags)
            if note_tags and other_tags:
                tag_intersection = note_tags & other_tags
                if tag_intersection:
                    tag_overlap = len(tag_intersection) / len(note_tags | other_tags)
                    strength += tag_overlap * 0.5  # Increased weight
            
            # 2. Content similarity (meaningful terms only)
            other_terms = self._extract_key_terms(other_note.content)
            if note_terms and other_terms:
                term_intersection = note_terms & other_terms
                if len(term_intersection) >= 2:  # At least 2 common terms
                    term_overlap = len(term_intersection) / len(note_terms | other_terms)
                    strength += term_overlap * 0.3
            
            # 3. Direct wikilink connections (very strong)
            note_links = {link.lower() for link in note.wikilinks}
            other_title = other_note.title.lower()
            note_title = note.title.lower()
            
            if (other_title in note_links or 
                note_title in {link.lower() for link in other_note.wikilinks}):
                strength += 0.4  # Strong direct connection
            
            # Only keep meaningful connections
            if strength > 0.2:
                connections[other_id] = round(strength, 3)
        
        # Limit connections per node to avoid overcrowding
        if len(connections) > 10:
            # Keep only the strongest connections
            sorted_connections = sorted(connections.items(), key=lambda x: x[1], reverse=True)
            connections = dict(sorted_connections[:10])
        
        return connections
    
    def _extract_key_terms(self, content: str) -> Set[str]:
        """Extract meaningful key terms from content"""
        # Clean content more thoroughly
        clean_content = re.sub(r'[#*`\[\](){}"-]', ' ', content.lower())
        clean_content = re.sub(r'https?://\S+', '', clean_content)  # Remove URLs
        clean_content = re.sub(r'\d+', '', clean_content)  # Remove numbers
        
        words = clean_content.split()
        
        # Expanded stop words list
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 
            'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 
            'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 
            'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 
            'let', 'put', 'say', 'she', 'too', 'use', 'will', 'with',
            'this', 'that', 'from', 'they', 'have', 'been', 'more',
            'than', 'what', 'when', 'where', 'some', 'make', 'time',
            'very', 'into', 'back', 'good', 'much', 'know', 'well',
            'should', 'would', 'could', 'there', 'each', 'which',
            'their', 'said', 'before', 'here', 'think', 'just',
            'also', 'after', 'first', 'most', 'people', 'other',
            'many', 'then', 'them', 'these', 'only', 'come', 'work',
            'life', 'may', 'years', 'through', 'both', 'under',
            'might', 'those', 'such', 'being', 'over', 'another',
            'between', 'during', 'without', 'index', 'file', 'path'
        }
        
        key_terms = {
            word for word in words 
            if len(word) > 4  # Longer words are more meaningful
            and word not in stop_words 
            and word.isalpha()  # Only letters
            and len(word) < 20  # Not too long
        }
        
        # Limit to most frequent meaningful terms
        return set(list(key_terms)[:20])
    
    def _create_clusters(self):
        """Create semantic clusters with higher thresholds"""
        visited = set()
        cluster_id = 0
        
        for note_id in self.notes.keys():
            if note_id in visited:
                continue
            
            cluster_nodes = self._expand_cluster(note_id, visited, threshold=0.3)
            
            # Only keep clusters with multiple meaningful connections
            if len(cluster_nodes) >= 2:
                cluster_name = f"cluster_{cluster_id}"
                self.clusters[cluster_name] = cluster_nodes
                cluster_id += 1
    
    def _expand_cluster(self, start_node: str, visited: Set[str], threshold: float = 0.3) -> List[str]:
        """Expand cluster using connected nodes with higher threshold"""
        cluster = [start_node]
        visited.add(start_node)
        queue = [start_node]
        
        while queue and len(cluster) < 20:  # Limit cluster size
            current = queue.pop(0)
            current_connections = self.connections.get(current, {})
            
            for connected_id, strength in current_connections.items():
                if connected_id not in visited and strength >= threshold:
                    cluster.append(connected_id)
                    visited.add(connected_id)
                    queue.append(connected_id)
        
        return cluster
    
    def _classify_node_type(self, note: CleanNote) -> str:
        """Classify node type"""
        content_lower = note.content.lower()
        title_lower = note.title.lower()
        
        # Practice indicators
        practice_keywords = ['practice', 'exercise', 'technique', 'method', 'steps', 'how to', 'guide', 'tutorial']
        if any(keyword in content_lower or keyword in title_lower for keyword in practice_keywords):
            return 'practice'
        
        # Reference indicators
        if ('reference' in note.tags or 'bibliography' in content_lower or 
            'source:' in content_lower or 'link:' in content_lower or
            'http' in content_lower):
            return 'reference'
        
        # Synthesis indicators
        synthesis_keywords = ['synthesis', 'summary', 'overview', 'integration', 'index']
        if any(keyword in content_lower or keyword in title_lower for keyword in synthesis_keywords):
            return 'synthesis'
        
        return 'concept'
    
    def _export_data(self) -> Dict[str, Any]:
        """Export clean data for visualization"""
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
                'path': note.canonical_path,
                'all_paths': note.all_paths
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
        )[:5]
        
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
    
    parser = argparse.ArgumentParser(description='Clean Knowledge Forest Builder')
    parser.add_argument('--directory', '-d', default='.', help='Directory to scan')
    parser.add_argument('--output', '-o', default='clean_forest.json', help='Output file')
    parser.add_argument('--sample', '-s', action='store_true', help='Create sample for web viewer')
    parser.add_argument('--max-nodes', type=int, default=50, help='Max nodes for sample (default: 50)')
    
    args = parser.parse_args()
    
    print("🌱 Building Clean Knowledge Forest...")
    print(f"📂 Scanning directory: {args.directory}")
    
    forest = CleanKnowledgeForest()
    data = forest.process_directory(args.directory)
    
    # Save main data
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved clean forest data to: {args.output}")
    
    # Print summary
    metadata = data['metadata']
    print("\n🌟 Clean Knowledge Forest Summary:")
    print(f"   📝 Total Unique Notes: {metadata['total_nodes']}")
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
        # Create a meaningful sample
        sample_nodes = data['nodes'][:args.max_nodes]
        sample_node_ids = {n['id'] for n in sample_nodes}
        
        # Include edges that connect sample nodes
        sample_edges = [edge for edge in data['edges'] 
                       if edge['source'] in sample_node_ids 
                       and edge['target'] in sample_node_ids]
        
        # Include relevant clusters
        sample_clusters = {k: [nid for nid in v if nid in sample_node_ids] 
                          for k, v in data['clusters'].items() 
                          if any(nid in sample_node_ids for nid in v)}
        
        sample_data = {
            'nodes': sample_nodes,
            'edges': sample_edges,
            'clusters': {k: v for k, v in sample_clusters.items() if len(v) > 1},
            'metadata': {
                **metadata,
                'total_nodes': len(sample_nodes),
                'total_edges': len(sample_edges),
                'total_clusters': len(sample_clusters)
            }
        }
        
        sample_file = 'sample_forest_data.js'
        js_content = f"""// Clean Knowledge Forest Data
const FOREST_DATA = {json.dumps(sample_data, indent=2, ensure_ascii=False)};

// Make data available globally
window.FOREST_DATA = FOREST_DATA;
"""
        
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"📄 Created clean sample data: {sample_file}")
        print(f"   Sample includes {len(sample_nodes)} nodes and {len(sample_edges)} connections")
        print("🌐 You can now open knowledge_forest_navigator.html in your browser!")
    
    print("\n✨ Clean Knowledge Forest is ready!")
    print("🔧 Much cleaner connections and no duplicates!")

if __name__ == "__main__":
    main()