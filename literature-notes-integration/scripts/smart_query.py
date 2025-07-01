#!/usr/bin/env python3
"""
Smart Query System for Literature Notes
Enhances search with natural language understanding and concept-based discovery
"""

import json
import re
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Set
import os
from collections import defaultdict, Counter

class SmartQueryProcessor:
    """Processes natural language queries into structured search operations"""
    
    def __init__(self, db_path: str = "../zettelkasten.db"):
        self.db_path = db_path
        
        # Query patterns for natural language understanding
        self.temporal_patterns = {
            'recent': lambda: (datetime.now() - timedelta(days=30)).isoformat(),
            'today': lambda: datetime.now().date().isoformat(),
            'this week': lambda: (datetime.now() - timedelta(days=7)).isoformat(),
            'this month': lambda: (datetime.now() - timedelta(days=30)).isoformat(),
            'this year': lambda: (datetime.now() - timedelta(days=365)).isoformat(),
        }
        
        # Conceptual relationships between domains
        self.concept_bridges = {
            'philosophy': ['vedanta', 'sanskrit', 'consciousness', 'dharma', 'karma'],
            'computer science': ['programming', 'cryptography', 'algorithms', 'security'],
            'wellness': ['ayurveda', 'yoga', 'meditation', 'health', 'pancha vayu'],
            'leadership': ['management', 'success', 'productivity', 'habits'],
            'learning': ['memory', 'study', 'knowledge', 'understanding'],
        }
        
        # Query type patterns
        self.query_types = {
            'connection': r'(connection|link|relate|between|bridge)',
            'similar': r'(similar|like|related|same as)',
            'about': r'(about|regarding|concerning|on)',
            'by': r'(by|from|author|written)',
            'tagged': r'(tagged|tag|label|category)',
            'recent': r'(recent|latest|new|updated)',
        }
    
    def parse_query(self, query: str) -> Dict:
        """Parse natural language query into structured components"""
        query_lower = query.lower()
        parsed = {
            'original': query,
            'type': 'basic',
            'terms': [],
            'filters': {},
            'concepts': []
        }
        
        # Detect query type
        for qtype, pattern in self.query_types.items():
            if re.search(pattern, query_lower):
                parsed['type'] = qtype
                break
        
        # Extract temporal filters
        for temporal, date_func in self.temporal_patterns.items():
            if temporal in query_lower:
                parsed['filters']['after_date'] = date_func()
                query_lower = query_lower.replace(temporal, '')
        
        # Extract tag filters
        tag_matches = re.findall(r'#(\w+)', query_lower)
        if tag_matches:
            parsed['filters']['tags'] = tag_matches
            for tag in tag_matches:
                query_lower = query_lower.replace(f'#{tag}', '')
        
        # Extract concepts and expand them
        for concept, related in self.concept_bridges.items():
            if concept in query_lower:
                parsed['concepts'].extend([concept] + related)
        
        # Extract remaining search terms
        # Remove common words and query type indicators
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'show', 'find', 'search', 'list', 'get', 'me', 'all'}
        terms = [word for word in query_lower.split() 
                if word not in stop_words and len(word) > 2]
        parsed['terms'] = terms
        
        return parsed
    
    def execute_smart_query(self, query: str) -> List[Dict]:
        """Execute a smart query and return enhanced results"""
        parsed = self.parse_query(query)
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        try:
            if parsed['type'] == 'connection':
                return self._find_connections(conn, parsed)
            elif parsed['type'] == 'similar':
                return self._find_similar(conn, parsed)
            elif parsed['type'] == 'recent':
                return self._find_recent(conn, parsed)
            else:
                return self._execute_enhanced_search(conn, parsed)
        finally:
            conn.close()
    
    def _find_connections(self, conn, parsed: Dict) -> List[Dict]:
        """Find notes that connect different concepts"""
        if len(parsed['terms']) < 2:
            return []
        
        # Find notes that mention multiple concepts
        concept_notes = defaultdict(set)
        for term in parsed['terms'] + parsed['concepts']:
            cursor = conn.execute("""
                SELECT DISTINCT path, title, content
                FROM notes
                WHERE content LIKE ? OR title LIKE ?
            """, (f'%{term}%', f'%{term}%'))
            
            for row in cursor:
                concept_notes[term].add(row['path'])
        
        # Find intersection - notes mentioning multiple concepts
        if len(concept_notes) >= 2:
            common_paths = set.intersection(*concept_notes.values())
            
            results = []
            for path in common_paths:
                note = self._get_note_details(conn, path)
                note['connection_strength'] = len([t for t in parsed['terms'] 
                                                 if t in note['content'].lower()])
                results.append(note)
            
            # Sort by connection strength
            results.sort(key=lambda x: x['connection_strength'], reverse=True)
            return results[:20]
        
        return []
    
    def _find_similar(self, conn, parsed: Dict) -> List[Dict]:
        """Find notes similar to a given topic or note"""
        if not parsed['terms']:
            return []
        
        # Get reference note or topic
        reference_term = ' '.join(parsed['terms'])
        
        # Find the reference note
        cursor = conn.execute("""
            SELECT path, tags, wikilinks
            FROM notes
            WHERE title LIKE ? OR content LIKE ?
            LIMIT 1
        """, (f'%{reference_term}%', f'%{reference_term}%'))
        
        reference = cursor.fetchone()
        if not reference:
            return []
        
        # Get tags and links from reference
        ref_tags = json.loads(reference['tags']) if reference['tags'] else []
        ref_links = json.loads(reference['wikilinks']) if reference['wikilinks'] else []
        
        # Find similar notes based on shared tags and links
        similar_notes = []
        
        # Find notes with similar tags
        if ref_tags:
            placeholders = ','.join('?' * len(ref_tags))
            cursor = conn.execute(f"""
                SELECT DISTINCT n.path, n.title, n.tags,
                       COUNT(DISTINCT t.tag) as shared_tags
                FROM notes n
                JOIN tags t ON n.path = t.note_path
                WHERE t.tag IN ({placeholders})
                AND n.path != ?
                GROUP BY n.path
                ORDER BY shared_tags DESC
                LIMIT 10
            """, ref_tags + [reference['path']])
            
            for row in cursor:
                note = self._get_note_details(conn, row['path'])
                note['similarity_score'] = row['shared_tags']
                similar_notes.append(note)
        
        return similar_notes
    
    def _find_recent(self, conn, parsed: Dict) -> List[Dict]:
        """Find recently created or modified notes"""
        date_filter = parsed['filters'].get('after_date', 
                                          (datetime.now() - timedelta(days=30)).isoformat())
        
        query = """
            SELECT path, title, modified, created
            FROM notes
            WHERE modified >= ? OR created >= ?
        """
        
        # Add term filters if present
        params = [date_filter, date_filter]
        if parsed['terms']:
            term_conditions = []
            for term in parsed['terms']:
                term_conditions.append("(content LIKE ? OR title LIKE ?)")
                params.extend([f'%{term}%', f'%{term}%'])
            query += " AND (" + " OR ".join(term_conditions) + ")"
        
        query += " ORDER BY modified DESC LIMIT 20"
        
        cursor = conn.execute(query, params)
        results = []
        for row in cursor:
            note = self._get_note_details(conn, row['path'])
            results.append(note)
        
        return results
    
    def _execute_enhanced_search(self, conn, parsed: Dict) -> List[Dict]:
        """Execute enhanced search with all filters and concept expansion"""
        # Build dynamic query
        conditions = []
        params = []
        
        # Add term searches with concept expansion
        all_terms = parsed['terms'] + parsed['concepts']
        if all_terms:
            term_conditions = []
            for term in all_terms:
                term_conditions.append("(content LIKE ? OR title LIKE ?)")
                params.extend([f'%{term}%', f'%{term}%'])
            conditions.append("(" + " OR ".join(term_conditions) + ")")
        
        # Add tag filters
        if 'tags' in parsed['filters']:
            tag_conditions = []
            for tag in parsed['filters']['tags']:
                tag_conditions.append("tags LIKE ?")
                params.append(f'%{tag}%')
            conditions.append("(" + " OR ".join(tag_conditions) + ")")
        
        # Add date filters
        if 'after_date' in parsed['filters']:
            conditions.append("(modified >= ? OR created >= ?)")
            params.extend([parsed['filters']['after_date']] * 2)
        
        # Build final query
        where_clause = " AND ".join(conditions) if conditions else "1=1"
        query = f"""
            SELECT path, title, content, tags, word_count,
                   (SELECT COUNT(*) FROM links WHERE target_path = notes.path) as backlink_count
            FROM notes
            WHERE {where_clause}
            ORDER BY backlink_count DESC, modified DESC
            LIMIT 50
        """
        
        cursor = conn.execute(query, params)
        results = []
        
        for row in cursor:
            note = dict(row)
            note['tags'] = json.loads(note['tags']) if note['tags'] else []
            
            # Calculate relevance score
            score = 0
            content_lower = note['content'].lower()
            title_lower = note['title'].lower()
            
            for term in parsed['terms']:
                score += title_lower.count(term) * 10  # Title matches worth more
                score += content_lower.count(term)
            
            note['relevance_score'] = score
            results.append(note)
        
        # Sort by relevance
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        return results[:20]
    
    def _get_note_details(self, conn, path: str) -> Dict:
        """Get detailed information about a note"""
        cursor = conn.execute("""
            SELECT path, title, content, tags, created, modified, word_count,
                   (SELECT COUNT(*) FROM links WHERE target_path = notes.path) as backlinks,
                   (SELECT COUNT(*) FROM links WHERE source_path = notes.path) as outlinks
            FROM notes
            WHERE path = ?
        """, (path,))
        
        row = cursor.fetchone()
        if row:
            note = dict(row)
            note['tags'] = json.loads(note['tags']) if note['tags'] else []
            return note
        return {}


# Command-line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Run a smart query
        query = " ".join(sys.argv[1:])
        processor = SmartQueryProcessor()
        results = processor.execute_smart_query(query)
        
        print(f"\nResults for: '{query}'")
        print(f"Found {len(results)} notes\n")
        
        for i, note in enumerate(results[:5], 1):
            print(f"{i}. {note['title']}")
            print(f"   Tags: {', '.join(note.get('tags', []))}")
            print(f"   Words: {note.get('word_count', 0)}")
            if 'relevance_score' in note:
                print(f"   Relevance: {note['relevance_score']}")
            print()
    else:
        print("Usage:")
        print("  python smart_query.py <query>        # Run a smart query")
        print("\nExample queries:")
        print("  python smart_query.py connections between ayurveda and programming")
        print("  python smart_query.py recent notes about cryptography")
        print("  python smart_query.py similar to memory palace")