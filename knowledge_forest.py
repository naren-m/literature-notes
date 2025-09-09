#!/usr/bin/env python3
"""
Knowledge Forest System
Creates an interconnected web of knowledge with semantic pathways and intelligent navigation.
Builds upon existing zettelkasten infrastructure to create forest-like knowledge structures.
"""

import sqlite3
import json
import re
import os
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Optional, Tuple, Any
from datetime import datetime
import random
import math

@dataclass
class KnowledgeNode:
    """Represents a node in the knowledge forest"""
    id: str
    title: str
    path: str
    content: str
    tags: List[str]
    node_type: str  # 'concept', 'practice', 'reference', 'synthesis'
    connections: Dict[str, float]  # node_id -> strength
    semantic_clusters: List[str]
    depth_level: int = 0
    last_visited: Optional[datetime] = None

@dataclass 
class KnowledgePathway:
    """Represents a semantic pathway between nodes"""
    start_node: str
    end_node: str
    pathway_type: str  # 'conceptual', 'causal', 'hierarchical', 'associative'
    strength: float
    intermediate_nodes: List[str]
    created: datetime
    usage_count: int = 0

class KnowledgeForest:
    """Knowledge Forest system for semantic navigation and discovery"""
    
    def __init__(self, db_path: str = "zettelkasten.db"):
        self.db_path = db_path
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.pathways: List[KnowledgePathway] = []
        self.semantic_clusters: Dict[str, List[str]] = defaultdict(list)
        self.forest_graph = defaultdict(list)
        self._initialize()
    
    def _initialize(self):
        """Initialize the knowledge forest from existing database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # Load existing notes as nodes
        cursor = conn.execute("""
            SELECT path, title, content, tags, wikilinks, backlinks
            FROM notes
        """)
        
        for row in cursor:
            node_id = self._path_to_id(row['path'])
            tags = json.loads(row['tags']) if row['tags'] else []
            
            node = KnowledgeNode(
                id=node_id,
                title=row['title'],
                path=row['path'],
                content=row['content'],
                tags=tags,
                node_type=self._classify_node_type(row['content'], tags),
                connections={},
                semantic_clusters=[]
            )
            
            self.nodes[node_id] = node
        
        conn.close()
        
        # Build connections and pathways
        self._build_semantic_connections()
        self._create_semantic_clusters()
        self._generate_pathways()
    
    def _path_to_id(self, path: str) -> str:
        """Convert file path to node ID"""
        return Path(path).stem.lower().replace(' ', '_').replace('-', '_')
    
    def _classify_node_type(self, content: str, tags: List[str]) -> str:
        """Classify node type based on content and tags"""
        content_lower = content.lower()
        
        # Check for practice indicators
        practice_keywords = ['practice', 'exercise', 'technique', 'method', 'steps', 'how to']
        if any(keyword in content_lower for keyword in practice_keywords):
            return 'practice'
        
        # Check for reference indicators
        if 'reference' in tags or 'bibliography' in content_lower or 'source:' in content_lower:
            return 'reference'
        
        # Check for synthesis indicators
        synthesis_keywords = ['synthesis', 'summary', 'overview', 'integration', 'connects']
        if any(keyword in content_lower for keyword in synthesis_keywords):
            return 'synthesis'
        
        return 'concept'
    
    def _build_semantic_connections(self):
        """Build semantic connections between nodes"""
        for node_id, node in self.nodes.items():
            connections = self._find_semantic_connections(node)
            node.connections = connections
    
    def _find_semantic_connections(self, node: KnowledgeNode) -> Dict[str, float]:
        """Find semantic connections for a node"""
        connections = {}
        
        # Extract key terms from the node
        node_terms = self._extract_key_terms(node.content)
        node_tags = set(node.tags)
        
        for other_id, other_node in self.nodes.items():
            if other_id == node.id:
                continue
            
            # Calculate connection strength based on multiple factors
            strength = 0.0
            
            # 1. Tag overlap
            other_tags = set(other_node.tags)
            tag_overlap = len(node_tags & other_tags) / max(len(node_tags | other_tags), 1)
            strength += tag_overlap * 0.3
            
            # 2. Content similarity (key terms)
            other_terms = self._extract_key_terms(other_node.content)
            term_overlap = len(node_terms & other_terms) / max(len(node_terms | other_terms), 1)
            strength += term_overlap * 0.4
            
            # 3. Wiki-link connections
            node_links = self._extract_wikilinks(node.content)
            other_links = self._extract_wikilinks(other_node.content)
            if other_node.title in node_links or node.title in other_links:
                strength += 0.3
            
            # Only keep connections above threshold
            if strength > 0.1:
                connections[other_id] = strength
        
        return connections
    
    def _extract_key_terms(self, content: str) -> Set[str]:
        """Extract key terms from content"""
        # Remove markdown and extract meaningful terms
        clean_content = re.sub(r'[#*`\[\]()-]', ' ', content.lower())
        words = clean_content.split()
        
        # Filter meaningful terms (length > 3, not common words)
        stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use'}
        
        key_terms = {word for word in words 
                    if len(word) > 3 and word not in stop_words 
                    and word.isalpha()}
        
        return key_terms
    
    def _extract_wikilinks(self, content: str) -> Set[str]:
        """Extract wiki-style links from content"""
        pattern = r'\[\[([^\]]+)\]\]'
        matches = re.findall(pattern, content)
        return set(matches)
    
    def _create_semantic_clusters(self):
        """Create semantic clusters of related nodes"""
        # Use simple clustering based on connection strength
        visited = set()
        cluster_id = 0
        
        for node_id, node in self.nodes.items():
            if node_id in visited:
                continue
            
            # Start new cluster
            cluster_name = f"cluster_{cluster_id}"
            cluster_nodes = self._expand_cluster(node_id, visited)
            
            for cluster_node_id in cluster_nodes:
                self.nodes[cluster_node_id].semantic_clusters.append(cluster_name)
                self.semantic_clusters[cluster_name].append(cluster_node_id)
            
            cluster_id += 1
    
    def _expand_cluster(self, start_node: str, visited: Set[str], threshold: float = 0.3) -> List[str]:
        """Expand cluster using connected nodes"""
        cluster = [start_node]
        visited.add(start_node)
        queue = [start_node]
        
        while queue:
            current = queue.pop(0)
            current_node = self.nodes[current]
            
            for connected_id, strength in current_node.connections.items():
                if connected_id not in visited and strength >= threshold:
                    cluster.append(connected_id)
                    visited.add(connected_id)
                    queue.append(connected_id)
        
        return cluster
    
    def _generate_pathways(self):
        """Generate semantic pathways between nodes"""
        self.pathways = []
        
        for node_id, node in self.nodes.items():
            for connected_id, strength in node.connections.items():
                if strength > 0.2:  # Only strong connections become pathways
                    pathway_type = self._classify_pathway_type(node, self.nodes[connected_id])
                    
                    pathway = KnowledgePathway(
                        start_node=node_id,
                        end_node=connected_id,
                        pathway_type=pathway_type,
                        strength=strength,
                        intermediate_nodes=[],
                        created=datetime.now()
                    )
                    
                    self.pathways.append(pathway)
    
    def _classify_pathway_type(self, node1: KnowledgeNode, node2: KnowledgeNode) -> str:
        """Classify the type of pathway between two nodes"""
        # Hierarchical: one is more general than the other
        if node1.node_type == 'concept' and node2.node_type == 'practice':
            return 'hierarchical'
        
        # Causal: practice leads to concept or vice versa
        if 'technique' in node1.content.lower() and 'effect' in node2.content.lower():
            return 'causal'
        
        # Conceptual: both are concepts
        if node1.node_type == 'concept' and node2.node_type == 'concept':
            return 'conceptual'
        
        return 'associative'
    
    def find_pathways(self, start_node: str, end_node: str = None, max_depth: int = 3) -> List[Dict[str, Any]]:
        """Find pathways between nodes"""
        if end_node:
            return self._find_direct_pathways(start_node, end_node, max_depth)
        else:
            return self._find_exploration_pathways(start_node, max_depth)
    
    def _find_direct_pathways(self, start: str, end: str, max_depth: int) -> List[Dict[str, Any]]:
        """Find pathways from start to end node"""
        pathways = []
        
        # BFS to find paths
        queue = [(start, [start], 0)]
        visited = {start}
        
        while queue:
            current, path, depth = queue.pop(0)
            
            if depth >= max_depth:
                continue
            
            if current == end and len(path) > 1:
                pathway_strength = self._calculate_path_strength(path)
                pathways.append({
                    'path': path,
                    'nodes': [self.nodes[node_id] for node_id in path],
                    'strength': pathway_strength,
                    'depth': depth
                })
                continue
            
            # Explore connections
            current_node = self.nodes.get(current)
            if current_node:
                for connected_id, strength in current_node.connections.items():
                    if connected_id not in path and strength > 0.15:  # Avoid cycles and weak connections
                        queue.append((connected_id, path + [connected_id], depth + 1))
        
        # Sort by strength and return top pathways
        pathways.sort(key=lambda x: x['strength'], reverse=True)
        return pathways[:10]
    
    def _find_exploration_pathways(self, start: str, max_depth: int) -> List[Dict[str, Any]]:
        """Find interesting pathways for exploration from a starting node"""
        pathways = []
        visited = set()
        
        def explore(current: str, path: List[str], depth: int):
            if depth >= max_depth or current in visited:
                return
            
            visited.add(current)
            current_node = self.nodes.get(current)
            if not current_node:
                return
            
            # Add current path if interesting
            if len(path) > 1:
                pathway_strength = self._calculate_path_strength(path)
                if pathway_strength > 0.2:
                    pathways.append({
                        'path': path,
                        'nodes': [self.nodes[node_id] for node_id in path],
                        'strength': pathway_strength,
                        'depth': depth,
                        'end_type': current_node.node_type
                    })
            
            # Explore strongest connections
            connections = sorted(current_node.connections.items(), key=lambda x: x[1], reverse=True)
            for connected_id, strength in connections[:3]:  # Top 3 connections
                if strength > 0.2:
                    explore(connected_id, path + [connected_id], depth + 1)
        
        explore(start, [start], 0)
        
        # Sort and deduplicate
        pathways.sort(key=lambda x: x['strength'], reverse=True)
        return pathways[:15]
    
    def _calculate_path_strength(self, path: List[str]) -> float:
        """Calculate strength of a pathway"""
        if len(path) < 2:
            return 0.0
        
        total_strength = 0.0
        for i in range(len(path) - 1):
            current_node = self.nodes.get(path[i])
            if current_node and path[i + 1] in current_node.connections:
                total_strength += current_node.connections[path[i + 1]]
        
        # Average strength with decay for longer paths
        avg_strength = total_strength / (len(path) - 1)
        decay_factor = 0.9 ** (len(path) - 2)
        return avg_strength * decay_factor
    
    def get_node_recommendations(self, node_id: str, count: int = 5) -> List[Dict[str, Any]]:
        """Get recommended nodes to explore from current node"""
        node = self.nodes.get(node_id)
        if not node:
            return []
        
        recommendations = []
        
        # Get strongly connected nodes
        for connected_id, strength in sorted(node.connections.items(), key=lambda x: x[1], reverse=True)[:count]:
            connected_node = self.nodes[connected_id]
            recommendations.append({
                'node': connected_node,
                'reason': 'Direct Connection',
                'strength': strength,
                'pathway_type': self._classify_pathway_type(node, connected_node)
            })
        
        # Get nodes from same cluster
        cluster_recommendations = []
        for cluster in node.semantic_clusters:
            for cluster_node_id in self.semantic_clusters[cluster]:
                if cluster_node_id != node_id and cluster_node_id not in [r['node'].id for r in recommendations]:
                    cluster_node = self.nodes[cluster_node_id]
                    cluster_recommendations.append({
                        'node': cluster_node,
                        'reason': f'Cluster: {cluster}',
                        'strength': 0.6,  # Default cluster strength
                        'pathway_type': 'associative'
                    })
        
        recommendations.extend(cluster_recommendations[:max(0, count - len(recommendations))])
        return recommendations[:count]
    
    def generate_forest_summary(self) -> Dict[str, Any]:
        """Generate summary of the knowledge forest"""
        total_nodes = len(self.nodes)
        total_pathways = len(self.pathways)
        total_clusters = len(self.semantic_clusters)
        
        # Node type distribution
        type_dist = Counter(node.node_type for node in self.nodes.values())
        
        # Connection statistics
        connection_counts = [len(node.connections) for node in self.nodes.values()]
        avg_connections = sum(connection_counts) / len(connection_counts) if connection_counts else 0
        
        # Cluster size distribution
        cluster_sizes = [len(nodes) for nodes in self.semantic_clusters.values()]
        avg_cluster_size = sum(cluster_sizes) / len(cluster_sizes) if cluster_sizes else 0
        
        return {
            'total_nodes': total_nodes,
            'total_pathways': total_pathways,
            'total_clusters': total_clusters,
            'node_types': dict(type_dist),
            'avg_connections_per_node': round(avg_connections, 2),
            'avg_cluster_size': round(avg_cluster_size, 2),
            'most_connected_nodes': self._get_most_connected_nodes(5),
            'largest_clusters': self._get_largest_clusters(3)
        }
    
    def _get_most_connected_nodes(self, count: int) -> List[Dict[str, Any]]:
        """Get most connected nodes"""
        nodes_by_connections = sorted(
            self.nodes.values(),
            key=lambda x: len(x.connections),
            reverse=True
        )
        
        return [
            {
                'title': node.title,
                'connections': len(node.connections),
                'type': node.node_type,
                'clusters': len(node.semantic_clusters)
            }
            for node in nodes_by_connections[:count]
        ]
    
    def _get_largest_clusters(self, count: int) -> List[Dict[str, Any]]:
        """Get largest semantic clusters"""
        clusters_by_size = sorted(
            self.semantic_clusters.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        return [
            {
                'cluster_name': cluster_name,
                'size': len(node_ids),
                'sample_nodes': [self.nodes[node_id].title for node_id in node_ids[:3]]
            }
            for cluster_name, node_ids in clusters_by_size[:count]
        ]
    
    def export_forest_data(self) -> Dict[str, Any]:
        """Export forest data for visualization"""
        nodes_data = []
        edges_data = []
        
        for node in self.nodes.values():
            nodes_data.append({
                'id': node.id,
                'title': node.title,
                'type': node.node_type,
                'tags': node.tags,
                'clusters': node.semantic_clusters,
                'connection_count': len(node.connections)
            })
            
            # Add edges
            for connected_id, strength in node.connections.items():
                edges_data.append({
                    'source': node.id,
                    'target': connected_id,
                    'strength': strength,
                    'type': 'semantic'
                })
        
        return {
            'nodes': nodes_data,
            'edges': edges_data,
            'clusters': dict(self.semantic_clusters),
            'metadata': self.generate_forest_summary()
        }

def main():
    """Main function for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Knowledge Forest System')
    parser.add_argument('--explore', type=str, help='Explore pathways from a node')
    parser.add_argument('--pathway', nargs=2, help='Find pathway between two nodes')
    parser.add_argument('--summary', action='store_true', help='Generate forest summary')
    parser.add_argument('--export', type=str, help='Export forest data to JSON file')
    
    args = parser.parse_args()
    
    forest = KnowledgeForest()
    
    if args.summary:
        summary = forest.generate_forest_summary()
        print(json.dumps(summary, indent=2))
    
    elif args.explore:
        pathways = forest.find_pathways(args.explore)
        print(f"Exploration pathways from '{args.explore}':")
        for i, pathway in enumerate(pathways[:5], 1):
            print(f"{i}. {' → '.join([node.title for node in pathway['nodes']])} (strength: {pathway['strength']:.2f})")
    
    elif args.pathway:
        start, end = args.pathway
        pathways = forest.find_pathways(start, end)
        print(f"Pathways from '{start}' to '{end}':")
        for i, pathway in enumerate(pathways[:3], 1):
            print(f"{i}. {' → '.join([node.title for node in pathway['nodes']])} (strength: {pathway['strength']:.2f})")
    
    elif args.export:
        data = forest.export_forest_data()
        with open(args.export, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Forest data exported to {args.export}")

if __name__ == "__main__":
    main()