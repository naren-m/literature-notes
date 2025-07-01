#!/usr/bin/env python3
"""
Web Server for Literature Notes Integration
Provides web interface for smart search and knowledge synthesis
"""

import os
import json
from flask import Flask, render_template, request, jsonify, send_from_directory
from datetime import datetime
import sqlite3
from smart_query import SmartQueryProcessor
from knowledge_synthesis import KnowledgeSynthesizer

app = Flask(__name__)

# Configuration
DB_PATH = os.getenv('NOTES_DB_PATH', '../zettelkasten.db')
WEB_PORT = int(os.getenv('WEB_PORT', 8080))
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

# Initialize processors
query_processor = SmartQueryProcessor(DB_PATH)
synthesizer = KnowledgeSynthesizer(DB_PATH)

@app.route('/')
def index():
    """Main page with smart search interface"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        # Check database connection
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        conn.close()
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'note_count': note_count,
            'services': {
                'database': 'connected',
                'query_processor': 'ready',
                'synthesizer': 'ready'
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/api/smart-query', methods=['POST'])
def smart_query():
    """Execute smart query and return results"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'error': 'Query parameter is required'}), 400
        
        results = query_processor.execute_smart_query(query)
        
        # Format results for web interface
        formatted_results = []
        for result in results:
            formatted_results.append({
                'title': result.get('title', ''),
                'content': result.get('content', '')[:300] + '...',
                'tags': result.get('tags', []),
                'word_count': result.get('word_count', 0),
                'relevance_score': result.get('relevance_score', 0),
                'connection_strength': result.get('connection_strength', 0),
                'path': result.get('path', '')
            })
        
        return jsonify({
            'query': query,
            'results': formatted_results,
            'count': len(formatted_results),
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/synthesis', methods=['POST'])
def generate_synthesis():
    """Generate knowledge synthesis"""
    try:
        data = request.get_json() or {}
        synthesis_type = data.get('type', 'daily')
        
        if synthesis_type == 'daily':
            result = synthesizer.generate_daily_synthesis()
        elif synthesis_type == 'domain':
            domain = data.get('domain', '')
            if not domain:
                return jsonify({'error': 'Domain parameter required for domain synthesis'}), 400
            result = synthesizer.generate_domain_summary(domain)
        elif synthesis_type == 'cross-domain':
            domain1 = data.get('domain1', '')
            domain2 = data.get('domain2', '')
            if not domain1 or not domain2:
                return jsonify({'error': 'Both domain1 and domain2 required for cross-domain synthesis'}), 400
            result = synthesizer.find_cross_domain_insights(domain1, domain2)
        else:
            return jsonify({'error': 'Invalid synthesis type'}), 400
        
        return jsonify({
            'type': synthesis_type,
            'result': result,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/graph')
def knowledge_graph():
    """Get knowledge graph data"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        
        # Get nodes (notes)
        cursor = conn.execute("""
            SELECT path, title, tags,
                   (SELECT COUNT(*) FROM links WHERE target_path = notes.path) as inlinks,
                   (SELECT COUNT(*) FROM links WHERE source_path = notes.path) as outlinks
            FROM notes
            ORDER BY inlinks DESC
            LIMIT 100
        """)
        
        nodes = []
        for row in cursor:
            tags = json.loads(row['tags']) if row['tags'] else []
            nodes.append({
                'id': row['path'],
                'title': row['title'],
                'tags': tags,
                'inlinks': row['inlinks'],
                'outlinks': row['outlinks'],
                'size': min(row['inlinks'] + row['outlinks'] + 1, 10)
            })
        
        # Get edges (links)
        cursor = conn.execute("""
            SELECT l.source_path, l.target_path,
                   n1.title as source_title, n2.title as target_title
            FROM links l
            JOIN notes n1 ON l.source_path = n1.path
            JOIN notes n2 ON l.target_path = n2.path
            LIMIT 200
        """)
        
        edges = []
        for row in cursor:
            edges.append({
                'source': row['source_path'],
                'target': row['target_path'],
                'source_title': row['source_title'],
                'target_title': row['target_title']
            })
        
        conn.close()
        
        return jsonify({
            'nodes': nodes,
            'edges': edges,
            'stats': {
                'node_count': len(nodes),
                'edge_count': len(edges)
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    """Get system statistics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(*) FROM links")
        link_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(DISTINCT tag) FROM tags")
        tag_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT SUM(word_count) FROM notes")
        total_words = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return jsonify({
            'notes': note_count,
            'links': link_count,
            'tags': tag_count,
            'total_words': total_words,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

# Template for the main interface
@app.route('/templates/index.html')
def serve_template():
    """Serve the main template"""
    template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Literature Notes Integration</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { text-align: center; margin-bottom: 2rem; }
        .search-box { width: 100%; padding: 1rem; font-size: 1.1rem; border: 2px solid #ddd; border-radius: 8px; margin-bottom: 1rem; }
        .results { margin-top: 2rem; }
        .result-item { background: #f9f9f9; padding: 1rem; margin-bottom: 1rem; border-radius: 4px; border-left: 4px solid #007bff; }
        .result-title { font-weight: bold; margin-bottom: 0.5rem; }
        .result-meta { color: #666; font-size: 0.9rem; margin-bottom: 0.5rem; }
        .result-content { color: #333; }
        .loading { text-align: center; padding: 2rem; color: #666; }
        .stats { display: flex; gap: 2rem; justify-content: center; margin-bottom: 2rem; }
        .stat-item { text-align: center; }
        .stat-number { font-size: 2rem; font-weight: bold; color: #007bff; }
        .stat-label { color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 Literature Notes Integration</h1>
            <p>Smart search and knowledge synthesis for your notes</p>
        </div>
        
        <div class="stats" id="stats">
            <div class="stat-item">
                <div class="stat-number" id="noteCount">-</div>
                <div class="stat-label">Notes</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="linkCount">-</div>
                <div class="stat-label">Links</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="tagCount">-</div>
                <div class="stat-label">Tags</div>
            </div>
        </div>
        
        <input type="text" 
               class="search-box" 
               id="searchInput" 
               placeholder="Try: 'connections between ayurveda and programming' or 'recent notes about cryptography'"
               autocomplete="off">
        
        <div class="results" id="results"></div>
    </div>
    
    <script>
        // Load stats on page load
        fetch('/api/stats')
            .then(response => response.json())
            .then(data => {
                document.getElementById('noteCount').textContent = data.notes;
                document.getElementById('linkCount').textContent = data.links;
                document.getElementById('tagCount').textContent = data.tags;
            })
            .catch(error => console.error('Error loading stats:', error));
        
        // Search functionality
        document.getElementById('searchInput').addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                performSearch(e.target.value);
            }
        });
        
        async function performSearch(query) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<div class="loading">Searching...</div>';
            
            try {
                const response = await fetch('/api/smart-query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });
                
                const data = await response.json();
                displayResults(data.results);
            } catch (error) {
                resultsDiv.innerHTML = '<p>Error performing search. Please try again.</p>';
            }
        }
        
        function displayResults(results) {
            const resultsDiv = document.getElementById('results');
            
            if (results.length === 0) {
                resultsDiv.innerHTML = '<p>No results found. Try different keywords.</p>';
                return;
            }
            
            const html = results.map(result => `
                <div class="result-item">
                    <div class="result-title">${result.title}</div>
                    <div class="result-meta">
                        📝 ${result.word_count} words
                        ${result.tags.length > 0 ? `🏷️ ${result.tags.join(', ')}` : ''}
                        ${result.relevance_score ? `📊 Relevance: ${result.relevance_score}` : ''}
                    </div>
                    <div class="result-content">${result.content}</div>
                </div>
            `).join('');
            
            resultsDiv.innerHTML = html;
        }
    </script>
</body>
</html>"""
    return template_content

if __name__ == '__main__':
    # Create templates directory and file
    os.makedirs('templates', exist_ok=True)
    
    print(f"🌐 Starting Literature Notes Integration Web Server...")
    print(f"📍 Server will be available at: http://localhost:{WEB_PORT}")
    print(f"📊 Database: {DB_PATH}")
    
    app.run(host='0.0.0.0', port=WEB_PORT, debug=DEBUG)