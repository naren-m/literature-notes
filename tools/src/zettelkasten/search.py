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
    
    def __init__(self, db_path: str = "zettelkasten.db"):
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


class ConceptMapper:
    """Maps concepts across different domains to find hidden connections"""
    
    def __init__(self, db_path: str = "zettelkasten.db"):
        self.db_path = db_path
        self.concept_graph = defaultdict(set)
        self._build_concept_graph()
    
    def _build_concept_graph(self):
        """Build a graph of concept relationships from the notes"""
        conn = sqlite3.connect(self.db_path)
        
        # Get all wikilinks to build connections
        cursor = conn.execute("""
            SELECT source_path, target_path FROM links
        """)
        
        for row in cursor:
            source = row[0].replace('.md', '').replace('-', ' ')
            target = row[1].replace('.md', '').replace('-', ' ')
            self.concept_graph[source].add(target)
            self.concept_graph[target].add(source)  # Bidirectional
        
        conn.close()
    
    def find_concept_bridges(self, concept1: str, concept2: str, max_depth: int = 3) -> List[List[str]]:
        """Find paths connecting two concepts"""
        # BFS to find shortest paths
        queue = [(concept1, [concept1])]
        visited = {concept1}
        paths = []
        
        while queue and len(paths) < 5:  # Limit to 5 paths
            current, path = queue.pop(0)
            
            if len(path) > max_depth:
                continue
            
            for neighbor in self.concept_graph.get(current, []):
                if neighbor == concept2:
                    paths.append(path + [neighbor])
                elif neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return paths


def create_enhanced_search_ui():
    """Create an enhanced search UI with advanced features"""
    enhanced_search_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Search - Literature Notes</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
        .smart-search-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .search-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .smart-search-box {
            width: 100%;
            padding: 1rem;
            font-size: 1.1rem;
            border: 2px solid #ddd;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .search-examples {
            margin-bottom: 2rem;
            padding: 1rem;
            background: #f5f5f5;
            border-radius: 8px;
        }
        
        .search-examples h3 {
            margin-top: 0;
        }
        
        .example-query {
            display: inline-block;
            margin: 0.25rem;
            padding: 0.5rem 1rem;
            background: white;
            border: 1px solid #ddd;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .example-query:hover {
            background: #007bff;
            color: white;
            border-color: #007bff;
        }
        
        .search-filters {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }
        
        .filter-group {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .result-enhanced {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s;
        }
        
        .result-enhanced:hover {
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .result-meta {
            display: flex;
            gap: 1rem;
            margin-top: 0.5rem;
            color: #666;
            font-size: 0.9rem;
        }
        
        .concept-bridge {
            background: #e8f4f8;
            border-left: 4px solid #007bff;
            padding: 1rem;
            margin: 1rem 0;
        }
        
        .loading {
            text-align: center;
            padding: 2rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="smart-search-container">
        <div class="search-header">
            <h1>Smart Search</h1>
            <p>Use natural language to explore your knowledge</p>
        </div>
        
        <input type="text" 
               class="smart-search-box" 
               id="smartSearchInput" 
               placeholder="Try: 'connections between ayurveda and programming' or 'recent notes about cryptography'"
               autocomplete="off">
        
        <div class="search-examples">
            <h3>Example Queries</h3>
            <span class="example-query" onclick="runExample(this)">connections between sanskrit and computer science</span>
            <span class="example-query" onclick="runExample(this)">recent notes about leadership</span>
            <span class="example-query" onclick="runExample(this)">similar to memory palace</span>
            <span class="example-query" onclick="runExample(this)">notes about ayurveda #health</span>
            <span class="example-query" onclick="runExample(this)">cryptography concepts this month</span>
        </div>
        
        <div class="search-filters">
            <div class="filter-group">
                <label>Time Range:</label>
                <select id="timeFilter">
                    <option value="">All time</option>
                    <option value="today">Today</option>
                    <option value="week">This week</option>
                    <option value="month">This month</option>
                    <option value="year">This year</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label>Sort by:</label>
                <select id="sortBy">
                    <option value="relevance">Relevance</option>
                    <option value="recent">Most Recent</option>
                    <option value="connections">Most Connected</option>
                    <option value="words">Word Count</option>
                </select>
            </div>
        </div>
        
        <div class="results-header" style="display: none;">
            <h2>Search Results</h2>
            <span id="resultCount"></span>
        </div>
        
        <div id="searchResults"></div>
    </div>
    
    <script>
        // Load the standard search index
        let searchIndex = null;
        let smartQuery = null;
        
        // Initialize smart search
        async function initSmartSearch() {
            try {
                const response = await fetch('/assets/search-index.json');
                searchIndex = await response.json();
                
                // Initialize search on page load if there's a query parameter
                const urlParams = new URLSearchParams(window.location.search);
                const query = urlParams.get('q');
                if (query) {
                    document.getElementById('smartSearchInput').value = query;
                    performSmartSearch(query);
                }
            } catch (error) {
                console.error('Error loading search index:', error);
            }
        }
        
        // Run example query
        function runExample(element) {
            const query = element.textContent;
            document.getElementById('smartSearchInput').value = query;
            performSmartSearch(query);
        }
        
        // Perform smart search
        async function performSmartSearch(query) {
            const resultsDiv = document.getElementById('searchResults');
            const resultsHeader = document.querySelector('.results-header');
            const resultCount = document.getElementById('resultCount');
            
            resultsDiv.innerHTML = '<div class="loading">Searching...</div>';
            resultsHeader.style.display = 'flex';
            
            try {
                // For now, use enhanced client-side search
                // In production, this would call the Python backend
                const results = enhancedClientSearch(query);
                
                resultCount.textContent = `${results.length} results found`;
                displayResults(results);
            } catch (error) {
                resultsDiv.innerHTML = '<p>Error performing search. Please try again.</p>';
            }
        }
        
        // Enhanced client-side search (temporary implementation)
        function enhancedClientSearch(query) {
            if (!searchIndex) return [];
            
            const queryLower = query.toLowerCase();
            const terms = queryLower.split(/\s+/).filter(t => t.length > 2);
            
            // Score each note
            const scored = searchIndex.map(note => {
                let score = 0;
                const titleLower = note.title.toLowerCase();
                const contentLower = note.content.toLowerCase();
                const tagsLower = note.tags.toLowerCase();
                
                terms.forEach(term => {
                    // Title matches are worth more
                    if (titleLower.includes(term)) score += 10;
                    if (contentLower.includes(term)) score += 1;
                    if (tagsLower.includes(term)) score += 5;
                });
                
                // Boost recent notes if searching for "recent"
                if (queryLower.includes('recent')) {
                    // This would use actual dates in production
                    score += Math.random() * 5;
                }
                
                // Boost if searching for connections
                if (queryLower.includes('connection') || queryLower.includes('between')) {
                    // Count how many different terms appear
                    const matchedTerms = terms.filter(term => 
                        contentLower.includes(term) || titleLower.includes(term)
                    ).length;
                    if (matchedTerms > 1) score += matchedTerms * 5;
                }
                
                return { ...note, score };
            });
            
            // Filter and sort
            return scored
                .filter(note => note.score > 0)
                .sort((a, b) => b.score - a.score)
                .slice(0, 20);
        }
        
        // Display results with enhanced formatting
        function displayResults(results) {
            const resultsDiv = document.getElementById('searchResults');
            
            if (results.length === 0) {
                resultsDiv.innerHTML = '<p>No results found. Try different keywords or browse by tags.</p>';
                return;
            }
            
            const html = results.map(result => `
                <div class="result-enhanced">
                    <h3><a href="${result.url}">${highlightTerms(result.title)}</a></h3>
                    <div class="result-meta">
                        <span>📝 ${result.word_count} words</span>
                        ${result.tags ? `<span>🏷️ ${highlightTerms(result.tags)}</span>` : ''}
                        ${result.score ? `<span>📊 Relevance: ${Math.round(result.score)}</span>` : ''}
                    </div>
                    <p>${highlightTerms(result.content)}</p>
                </div>
            `).join('');
            
            resultsDiv.innerHTML = html;
        }
        
        // Highlight search terms
        function highlightTerms(text) {
            const query = document.getElementById('smartSearchInput').value;
            const terms = query.toLowerCase().split(/\s+/).filter(t => t.length > 2);
            
            let highlighted = text;
            terms.forEach(term => {
                const regex = new RegExp(`(${term})`, 'gi');
                highlighted = highlighted.replace(regex, '<mark>$1</mark>');
            });
            
            return highlighted;
        }
        
        // Event listeners
        document.getElementById('smartSearchInput').addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                performSmartSearch(e.target.value);
            }
        });
        
        // Time filter
        document.getElementById('timeFilter').addEventListener('change', (e) => {
            const query = document.getElementById('smartSearchInput').value;
            if (query) {
                const timeQuery = e.target.value ? `${query} ${e.target.value}` : query;
                performSmartSearch(timeQuery);
            }
        });
        
        // Initialize on load
        initSmartSearch();
    </script>
</body>
</html>
"""
    
    return enhanced_search_html


# Command-line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "generate-ui":
            # Generate the enhanced search UI
            ui_html = create_enhanced_search_ui()
            with open("smart-search.html", "w") as f:
                f.write(ui_html)
            print("Enhanced search UI generated: smart-search.html")
        else:
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
        print("  python smart_query.py generate-ui    # Generate enhanced search UI")
        print("  python smart_query.py <query>        # Run a smart query")
        print("\nExample queries:")
        print("  python smart_query.py connections between ayurveda and programming")
        print("  python smart_query.py recent notes about cryptography")
        print("  python smart_query.py similar to memory palace")