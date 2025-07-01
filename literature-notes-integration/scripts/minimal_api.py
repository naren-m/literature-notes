#!/usr/bin/env python3
"""
Minimal API Server for Literature Notes Integration
Uses only Python standard library - no external dependencies
"""

import http.server
import socketserver
import json
import sqlite3
import urllib.parse
from datetime import datetime
import os

class LiteratureNotesHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP handler for literature notes API"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        try:
            if path == '/':
                self.send_json_response({
                    "message": "Literature Notes Minimal API",
                    "status": "running",
                    "timestamp": datetime.now().isoformat(),
                    "endpoints": ["/health", "/stats", "/search", "/notes"]
                })
            
            elif path == '/health':
                self.handle_health()
            
            elif path == '/stats':
                self.handle_stats()
            
            elif path == '/search':
                query = query_params.get('q', [''])[0]
                self.handle_search(query)
            
            elif path == '/notes':
                self.handle_notes()
            
            else:
                self.send_error(404, "Endpoint not found")
                
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
    
    def do_POST(self):
        """Handle POST requests"""
        try:
            if self.path == '/smart-query':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                query = data.get('query', '')
                self.handle_smart_query(query)
            elif self.path == '/file-content':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                file_path = data.get('path', '')
                self.handle_file_content(file_path)
            else:
                self.send_error(404, "POST endpoint not found")
                
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
    
    def handle_health(self):
        """Health check endpoint"""
        try:
            # Test database connection
            db_path = self.get_db_path()
            conn = sqlite3.connect(db_path)
            cursor = conn.execute("SELECT COUNT(*) FROM notes")
            note_count = cursor.fetchone()[0]
            conn.close()
            
            response = {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "database": "connected",
                "notes": note_count
            }
            self.send_json_response(response)
            
        except Exception as e:
            response = {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.send_json_response(response, 500)
    
    def handle_stats(self):
        """System statistics endpoint"""
        try:
            db_path = self.get_db_path()
            conn = sqlite3.connect(db_path)
            
            cursor = conn.execute("SELECT COUNT(*) FROM notes")
            note_count = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT COUNT(*) FROM links")
            link_count = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT COUNT(DISTINCT tag) FROM tags")
            tag_count = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT SUM(word_count) FROM notes WHERE word_count IS NOT NULL")
            result = cursor.fetchone()
            total_words = result[0] if result[0] else 0
            
            conn.close()
            
            response = {
                "notes": note_count,
                "links": link_count,
                "tags": tag_count,
                "total_words": total_words,
                "timestamp": datetime.now().isoformat()
            }
            self.send_json_response(response)
            
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)
    
    def handle_search(self, query):
        """Simple search endpoint"""
        if not query:
            self.send_json_response({"error": "Query parameter 'q' required"}, 400)
            return
        
        try:
            db_path = self.get_db_path()
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
                content = row['content'] or ''
                results.append({
                    'title': row['title'],
                    'content': content[:200] + '...' if len(content) > 200 else content,
                    'path': row['path'],
                    'word_count': row['word_count'] or 0,
                    'tags': row['tags'] or ''
                })
            
            conn.close()
            
            response = {
                "query": query,
                "results": results,
                "count": len(results),
                "timestamp": datetime.now().isoformat()
            }
            self.send_json_response(response)
            
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)
    
    def handle_smart_query(self, query):
        """Smart query endpoint"""
        if not query:
            self.send_json_response({"error": "Query required"}, 400)
            return
        
        try:
            # Simple smart query implementation
            terms = query.lower().split()
            
            db_path = self.get_db_path()
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
                content = row['content'] or ''
                title = row['title'] or ''
                
                # Calculate simple relevance score
                score = 0
                content_lower = content.lower()
                title_lower = title.lower()
                
                for term in terms:
                    score += title_lower.count(term) * 10
                    score += content_lower.count(term)
                
                results.append({
                    'title': title,
                    'content': content[:300] + '...' if len(content) > 300 else content,
                    'path': row['path'],
                    'word_count': row['word_count'] or 0,
                    'tags': row['tags'] or '',
                    'relevance_score': score
                })
            
            # Sort by relevance
            results.sort(key=lambda x: x['relevance_score'], reverse=True)
            
            conn.close()
            
            response = {
                "query": query,
                "results": results,
                "count": len(results),
                "timestamp": datetime.now().isoformat()
            }
            self.send_json_response(response)
            
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)
    
    def handle_file_content(self, file_path):
        """Get content of a specific file"""
        if not file_path:
            self.send_json_response({"error": "File path required"}, 400)
            return
        
        try:
            # Try to get content from database first
            db_path = self.get_db_path()
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            
            # Look for the file in database
            cursor = conn.execute("SELECT * FROM notes WHERE path = ? OR path LIKE ?", 
                                (file_path, f'%{file_path}%'))
            row = cursor.fetchone()
            
            if row:
                response = {
                    "path": row['path'],
                    "title": row['title'],
                    "content": row['content'] or '',
                    "word_count": row['word_count'] or 0,
                    "tags": row['tags'] or '',
                    "found_in": "database"
                }
                conn.close()
                self.send_json_response(response)
                return
            
            conn.close()
            
            # Try to read file directly from filesystem
            import os
            
            # Clean up the path
            clean_path = file_path.lstrip('/')
            
            # Possible file locations
            possible_paths = [
                clean_path,
                f"docs/{clean_path}",
                f"{clean_path}",
                clean_path.replace('.md', '') + '.md'
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        response = {
                            "path": file_path,
                            "title": os.path.basename(path).replace('.md', ''),
                            "content": content,
                            "word_count": len(content.split()),
                            "tags": '',
                            "found_in": "filesystem",
                            "actual_path": path
                        }
                        self.send_json_response(response)
                        return
                    except Exception as e:
                        continue
            
            # File not found
            self.send_json_response({
                "error": f"File not found: {file_path}",
                "searched_paths": possible_paths
            }, 404)
            
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)
    
    def handle_notes(self):
        """List all notes"""
        try:
            db_path = self.get_db_path()
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            
            cursor = conn.execute('''
                SELECT path, title, word_count, created
                FROM notes
                ORDER BY created DESC
                LIMIT 20
            ''')
            
            results = []
            for row in cursor:
                results.append({
                    'title': row['title'],
                    'path': row['path'],
                    'word_count': row['word_count'] or 0,
                    'created': row['created']
                })
            
            conn.close()
            
            response = {
                "notes": results,
                "count": len(results)
            }
            self.send_json_response(response)
            
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)
    
    def get_db_path(self):
        """Get database path"""
        # Try multiple locations
        possible_paths = [
            "zettelkasten.db",
            "../zettelkasten.db",
            "literature-notes-integration/data/zettelkasten.db"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        # If no database exists, create a minimal one
        print("⚠️ No database found, creating minimal database...")
        self.create_minimal_database("zettelkasten.db")
        return "zettelkasten.db"
    
    def create_minimal_database(self, db_path):
        """Create a minimal database for testing"""
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
            ('demo1.md', 'Programming and Philosophy Connection', 
             'Programming requires logical thinking similar to philosophical reasoning. '
             'Both involve systematic problem-solving and understanding complex relationships.',
             '["programming", "philosophy", "thinking"]', '[]', '[]', 
             '2025-06-30', '2025-06-30', 25),
            
            ('demo2.md', 'Sanskrit Language Structure', 
             'Sanskrit grammar follows systematic rules similar to programming languages. '
             'The precision and structure make it ideal for knowledge representation.',
             '["sanskrit", "language", "structure"]', '[]', '[]',
             '2025-06-30', '2025-06-30', 22),
            
            ('demo3.md', 'Memory Techniques for Learning',
             'Ancient memory palace techniques can enhance programming learning. '
             'Systematic organization helps in both memory retention and code structure.',
             '["memory", "learning", "techniques"]', '[]', '[]',
             '2025-06-30', '2025-06-30', 20),
        ]
        
        cursor.executemany('''INSERT OR REPLACE INTO notes 
            (path, title, content, tags, wikilinks, backlinks, created, modified, word_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', sample_notes)
        
        conn.commit()
        conn.close()
        print("✅ Minimal database created with sample data")
    
    def send_json_response(self, data, status_code=200):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        json_data = json.dumps(data, indent=2)
        self.wfile.write(json_data.encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")

def main():
    """Start the minimal API server"""
    PORT = 8083
    
    print("🚀 Starting Minimal Literature Notes API Server")
    print("=" * 50)
    print(f"📍 Server: http://localhost:{PORT}")
    print(f"📍 Health: http://localhost:{PORT}/health")
    print(f"📍 Stats: http://localhost:{PORT}/stats")
    print(f"📍 Search: http://localhost:{PORT}/search?q=programming")
    print(f"📍 Notes: http://localhost:{PORT}/notes")
    print("\n🧪 Test Commands:")
    print(f"   curl http://localhost:{PORT}/health")
    print(f"   curl http://localhost:{PORT}/stats")
    print(f"   curl 'http://localhost:{PORT}/search?q=programming'")
    print(f'   curl -X POST -H "Content-Type: application/json" -d \'{{"query":"programming"}}\' http://localhost:{PORT}/smart-query')
    print("\n🛑 Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), LiteratureNotesHandler) as httpd:
            print(f"✅ Server started successfully on port {PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use. Try a different port or stop the existing service.")
            print(f"💡 Kill existing process: lsof -ti:{PORT} | xargs kill")
        else:
            print(f"❌ Server error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()