#!/usr/bin/env python3
"""
Simple API Server Starter for Literature Notes Integration
Runs locally without Docker to test functionality
"""

import sys
import os
from pathlib import Path

# Add the scripts directory to Python path
scripts_dir = Path(__file__).parent / 'literature-notes-integration' / 'scripts'
sys.path.insert(0, str(scripts_dir))

try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
    import sqlite3
    from datetime import datetime
    
    print("✅ Flask imports successful")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Installing required packages...")
    os.system("pip install flask flask-cors")
    sys.exit(1)

# Check if database exists
db_path = "zettelkasten.db"
if not os.path.exists(db_path):
    print(f"❌ Database not found at {db_path}")
    print("Creating sample database...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE,
        title TEXT,
        content TEXT,
        tags TEXT,
        wikilinks TEXT,
        backlinks TEXT,
        created TEXT,
        modified TEXT,
        word_count INTEGER
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS links (
        source_path TEXT,
        target_path TEXT,
        link_type TEXT
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tags (
        tag TEXT,
        note_path TEXT
    )''')
    
    # Insert sample data
    sample_notes = [
        ('sample1.md', 'Programming Concepts', 
         'This note explores various programming concepts including algorithms, data structures, and design patterns. '
         'Programming is a creative process that combines logical thinking with problem-solving skills.',
         '["programming", "learning", "technology"]', '[]', '[]', 
         '2025-06-30', '2025-06-30', 25),
        
        ('sample2.md', 'Sanskrit and Philosophy', 
         'Sanskrit is an ancient language that connects to deep philosophical concepts. '
         'The systematic nature of Sanskrit grammar shares similarities with programming languages.',
         '["sanskrit", "philosophy", "language"]', '[]', '[]',
         '2025-06-30', '2025-06-30', 20),
        
        ('sample3.md', 'Memory Techniques',
         'Memory palace and other ancient memory techniques can be applied to learning programming. '
         'Both require systematic organization and practice.',
         '["memory", "learning", "productivity"]', '[]', '[]',
         '2025-06-30', '2025-06-30', 18),
    ]
    
    cursor.executemany('''INSERT OR REPLACE INTO notes 
        (path, title, content, tags, wikilinks, backlinks, created, modified, word_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', sample_notes)
    
    # Insert tags
    sample_tags = [
        ('programming', 'sample1.md'),
        ('learning', 'sample1.md'),
        ('learning', 'sample3.md'),
        ('sanskrit', 'sample2.md'),
        ('philosophy', 'sample2.md'),
        ('memory', 'sample3.md'),
        ('productivity', 'sample3.md'),
    ]
    
    cursor.executemany('INSERT INTO tags (tag, note_path) VALUES (?, ?)', sample_tags)
    
    conn.commit()
    conn.close()
    print("✅ Sample database created")

# Create Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    """Root endpoint"""
    return jsonify({
        "message": "Literature Notes Integration API",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "note": "Simple local API server",
        "endpoints": ["/health", "/stats", "/smart-query", "/search"]
    })

@app.route('/health')
def health():
    """Health check"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        conn.close()
        
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "database": "connected",
            "notes": note_count
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

@app.route('/stats')
def stats():
    """Get system statistics"""
    try:
        conn = sqlite3.connect(db_path)
        
        cursor = conn.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(*) FROM links")
        link_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(DISTINCT tag) FROM tags")
        tag_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT SUM(word_count) FROM notes WHERE word_count IS NOT NULL")
        total_words = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return jsonify({
            "notes": note_count,
            "links": link_count,
            "tags": tag_count,
            "total_words": total_words,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search')
def search():
    """Simple search endpoint"""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({"error": "Query parameter 'q' required"}), 400
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        cursor = conn.execute('''
            SELECT path, title, content, tags, word_count
            FROM notes
            WHERE content LIKE ? OR title LIKE ?
            ORDER BY word_count DESC
            LIMIT 10
        ''', (f'%{query}%', f'%{query}%'))
        
        results = []
        for row in cursor:
            results.append({
                'title': row['title'],
                'content': row['content'][:200] + '...' if len(row['content']) > 200 else row['content'],
                'path': row['path'],
                'word_count': row['word_count'],
                'tags': row['tags']
            })
        
        conn.close()
        
        return jsonify({
            "query": query,
            "results": results,
            "count": len(results)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/smart-query', methods=['POST'])
def smart_query():
    """Smart query endpoint"""
    try:
        data = request.get_json()
        query = data.get('query', '') if data else ''
        
        if not query:
            return jsonify({"error": "Query required in JSON body"}), 400
        
        # Simple implementation - just search for terms
        terms = query.lower().split()
        
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Build search with multiple terms
        conditions = []
        params = []
        
        for term in terms:
            conditions.append("(content LIKE ? OR title LIKE ?)")
            params.extend([f'%{term}%', f'%{term}%'])
        
        if conditions:
            where_clause = " OR ".join(conditions)
            query_sql = f'''
                SELECT path, title, content, tags, word_count
                FROM notes
                WHERE {where_clause}
                ORDER BY word_count DESC
                LIMIT 10
            '''
            
            cursor = conn.execute(query_sql, params)
        else:
            cursor = conn.execute("SELECT * FROM notes LIMIT 5")
        
        results = []
        for row in cursor:
            # Calculate simple relevance score
            score = 0
            content_lower = row['content'].lower()
            title_lower = row['title'].lower()
            
            for term in terms:
                score += title_lower.count(term) * 10
                score += content_lower.count(term)
            
            results.append({
                'title': row['title'],
                'content': row['content'][:300] + '...' if len(row['content']) > 300 else row['content'],
                'path': row['path'],
                'word_count': row['word_count'],
                'tags': row['tags'],
                'relevance_score': score
            })
        
        # Sort by relevance
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        conn.close()
        
        return jsonify({
            "query": query,
            "results": results,
            "count": len(results),
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Simple Literature Notes API Server...")
    print("📍 Server will be available at: http://localhost:8082")
    print("📍 Health check: http://localhost:8082/health")
    print("📍 Statistics: http://localhost:8082/stats")
    print("📍 Search: http://localhost:8082/search?q=programming")
    print("📍 Smart query: POST to http://localhost:8082/smart-query")
    print("\n🧪 Test commands:")
    print("   curl http://localhost:8082/health")
    print("   curl http://localhost:8082/stats")
    print('   curl -X POST -H "Content-Type: application/json" -d \'{"query":"programming"}\' http://localhost:8082/smart-query')
    print("\n🛑 Press Ctrl+C to stop")
    
    try:
        app.run(host='0.0.0.0', port=8082, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        print("💡 Try installing requirements: pip install flask flask-cors")