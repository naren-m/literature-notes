#!/usr/bin/env python3
"""
Integrate API functionality with your regular documentation
Creates API endpoints accessible from your main Jekyll site
"""

import os
import shutil
from pathlib import Path

def create_api_integration():
    """Create API integration files for your Jekyll site"""
    
    print("🔗 Integrating API with your documentation...")
    
    # Create API search page for Jekyll
    api_search_page = """---
layout: default
title: Smart Search API
---

# Smart Search API

<style>
.api-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
}

.search-box {
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    border: 2px solid #ddd;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.api-status {
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1rem;
}

.status-connected {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    color: #155724;
}

.status-disconnected {
    background: #f8d7da;
    border: 1px solid #f5c6cb;
    color: #721c24;
}

.result-item {
    background: #f9f9f9;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
    border-left: 4px solid #007bff;
}

.result-title {
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.result-meta {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.api-info {
    background: #e8f4f8;
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 2rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: white;
    padding: 1rem;
    border-radius: 4px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: #007bff;
}

.stat-label {
    color: #666;
    font-size: 0.9rem;
}
</style>

<div class="api-container">
    <div class="api-info">
        <h3>🧠 Smart Search Integration</h3>
        <p>This page connects to your local API server to provide intelligent search across your literature notes.</p>
        <p><strong>API Status:</strong> <span id="apiStatus">Checking...</span></p>
    </div>
    
    <div class="stats-grid" id="statsGrid" style="display: none;">
        <div class="stat-card">
            <div class="stat-number" id="noteCount">-</div>
            <div class="stat-label">Notes</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="linkCount">-</div>
            <div class="stat-label">Links</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="tagCount">-</div>
            <div class="stat-label">Tags</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="wordCount">-</div>
            <div class="stat-label">Total Words</div>
        </div>
    </div>
    
    <input type="text" 
           class="search-box" 
           id="smartSearchInput" 
           placeholder="Try: 'connections between programming and philosophy' or 'sanskrit and computer science'"
           autocomplete="off">
    
    <div id="searchResults"></div>
    
    <div style="margin-top: 2rem;">
        <h3>📋 Example Queries</h3>
        <ul>
            <li><code>connections between sanskrit and programming</code></li>
            <li><code>ayurveda and modern wellness</code></li>
            <li><code>memory techniques</code></li>
            <li><code>leadership and productivity</code></li>
            <li><code>cryptography concepts</code></li>
        </ul>
        
        <h3>🔧 API Endpoints</h3>
        <ul>
            <li><strong>Health Check:</strong> <code>GET /health</code></li>
            <li><strong>Statistics:</strong> <code>GET /stats</code></li>
            <li><strong>Search:</strong> <code>GET /search?q=query</code></li>
            <li><strong>Smart Query:</strong> <code>POST /smart-query</code></li>
            <li><strong>List Notes:</strong> <code>GET /notes</code></li>
        </ul>
    </div>
</div>

<script>
const API_BASE = 'http://localhost:8083';
let apiConnected = false;

// Check API status on page load
async function checkApiStatus() {
    try {
        const response = await fetch(`${API_BASE}/health`);
        if (response.ok) {
            const data = await response.json();
            document.getElementById('apiStatus').innerHTML = 
                '<span style="color: green;">✅ Connected</span>';
            apiConnected = true;
            loadStats();
        } else {
            throw new Error('API not responding');
        }
    } catch (error) {
        document.getElementById('apiStatus').innerHTML = 
            '<span style="color: red;">❌ Disconnected</span> - Start API with: <code>python minimal_api.py</code>';
        apiConnected = false;
    }
}

// Load statistics
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        if (response.ok) {
            const data = await response.json();
            document.getElementById('noteCount').textContent = data.notes || 0;
            document.getElementById('linkCount').textContent = data.links || 0;
            document.getElementById('tagCount').textContent = data.tags || 0;
            document.getElementById('wordCount').textContent = data.total_words || 0;
            document.getElementById('statsGrid').style.display = 'grid';
        }
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// Perform smart search
async function performSearch(query) {
    if (!apiConnected) {
        document.getElementById('searchResults').innerHTML = 
            '<p style="color: red;">❌ API not connected. Please start the API server first.</p>';
        return;
    }
    
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '<div style="text-align: center; padding: 2rem; color: #666;">🔍 Searching...</div>';
    
    try {
        const response = await fetch(`${API_BASE}/smart-query`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query })
        });
        
        if (response.ok) {
            const data = await response.json();
            displayResults(data.results, query);
        } else {
            throw new Error('Search failed');
        }
    } catch (error) {
        resultsDiv.innerHTML = '<p style="color: red;">❌ Search failed. Check if API server is running.</p>';
    }
}

// Display search results
function displayResults(results, query) {
    const resultsDiv = document.getElementById('searchResults');
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found. Try different keywords.</p>';
        return;
    }
    
    let html = `<h3>🔍 Search Results for "${query}" (${results.length} found)</h3>`;
    
    results.forEach(result => {
        const highlightedTitle = highlightTerms(result.title, query);
        const highlightedContent = highlightTerms(result.content, query);
        
        html += `
            <div class="result-item">
                <div class="result-title">${highlightedTitle}</div>
                <div class="result-meta">
                    📝 ${result.word_count} words
                    ${result.relevance_score ? `📊 Relevance: ${result.relevance_score}` : ''}
                    ${result.path ? `📁 ${result.path}` : ''}
                </div>
                <div>${highlightedContent}</div>
            </div>
        `;
    });
    
    resultsDiv.innerHTML = html;
}

// Highlight search terms
function highlightTerms(text, query) {
    const terms = query.toLowerCase().split(/\\s+/).filter(t => t.length > 2);
    let highlighted = text;
    
    terms.forEach(term => {
        const regex = new RegExp(`(${term})`, 'gi');
        highlighted = highlighted.replace(regex, '<mark>$1</mark>');
    });
    
    return highlighted;
}

// Event listeners
document.getElementById('smartSearchInput').addEventListener('keyup', (e) => {
    if (e.key === 'Enter' && e.target.value.trim()) {
        performSearch(e.target.value.trim());
    }
});

// Initialize on page load
checkApiStatus();
</script>
"""
    
    # Save the API search page
    with open('api-search.md', 'w') as f:
        f.write(api_search_page)
    
    print("✅ Created api-search.md")
    
    # Update main index.md to include API search link
    try:
        with open('index.md', 'r') as f:
            content = f.read()
        
        # Add API search section if not already present
        if 'API Search' not in content and 'api-search' not in content:
            api_section = """
## 🧠 Smart Search & API

- **[Smart Search API](/api-search/)** - Intelligent search with natural language queries
- **API Server** - RESTful endpoints for programmatic access
- **Real-time Integration** - Live connection to your knowledge base

"""
            
            # Insert after the first heading or at the end
            if '\n##' in content:
                parts = content.split('\n##', 1)
                content = parts[0] + api_section + '\n##' + parts[1]
            else:
                content += api_section
            
            with open('index.md', 'w') as f:
                f.write(content)
            
            print("✅ Updated index.md with API search link")
    
    except FileNotFoundError:
        print("⚠️ index.md not found, skipping update")
    
    # Create API documentation page
    api_docs = """---
layout: default
title: API Documentation
---

# Literature Notes API Documentation

## 🚀 Getting Started

Start the API server:
```bash
python minimal_api.py
```

The API will be available at: `http://localhost:8083`

## 📍 Endpoints

### Health Check
```
GET /health
```
Returns API status and basic database info.

### Statistics
```
GET /stats
```
Returns counts of notes, links, tags, and total words.

### Search
```
GET /search?q=query
```
Simple text search across note titles and content.

### Smart Query
```
POST /smart-query
Content-Type: application/json

{
  "query": "connections between programming and philosophy"
}
```
Advanced search with natural language processing and relevance scoring.

### List Notes
```
GET /notes
```
Returns list of recent notes with metadata.

## 🧪 Example Usage

### cURL Examples
```bash
# Health check
curl http://localhost:8083/health

# Get statistics
curl http://localhost:8083/stats

# Simple search
curl "http://localhost:8083/search?q=programming"

# Smart query
curl -X POST -H "Content-Type: application/json" \\
  -d '{"query":"connections between sanskrit and programming"}' \\
  http://localhost:8083/smart-query
```

### JavaScript Examples
```javascript
// Health check
const health = await fetch('http://localhost:8083/health');
const healthData = await health.json();

// Smart query
const response = await fetch('http://localhost:8083/smart-query', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: 'programming concepts' })
});
const results = await response.json();
```

## 🔧 Integration

### With Your Jekyll Site
The API can be integrated directly into your Jekyll pages using JavaScript:

1. **Check API status** before making requests
2. **Display results** in your existing page layouts
3. **Handle errors** gracefully when API is offline

### With External Tools
The API provides standard REST endpoints that can be used with:
- Custom scripts and automation
- Browser extensions
- Mobile apps
- Other documentation tools

## 🛠️ Configuration

The API automatically:
- **Finds your database** in common locations
- **Creates sample data** if no database exists
- **Handles CORS** for browser integration
- **Provides error handling** for robustness

## 📊 Response Format

All responses are JSON with consistent structure:
```json
{
  "query": "search term",
  "results": [...],
  "count": 5,
  "timestamp": "2025-06-30T..."
}
```

Error responses include:
```json
{
  "error": "Error description",
  "timestamp": "2025-06-30T..."
}
```
"""
    
    with open('api-docs.md', 'w') as f:
        f.write(api_docs)
    
    print("✅ Created api-docs.md")
    
    # Create a startup script for easy API management
    startup_script = """#!/bin/bash

# Literature Notes API Startup Script
echo "🚀 Starting Literature Notes API Integration..."

# Check if API is already running
if curl -s http://localhost:8083/health > /dev/null 2>&1; then
    echo "✅ API already running at http://localhost:8083"
    echo "📍 Smart Search: http://localhost:4000/api-search/"
    echo "📍 API Docs: http://localhost:4000/api-docs/"
else
    echo "🔧 Starting API server..."
    python minimal_api.py &
    API_PID=$!
    
    # Wait for API to start
    sleep 3
    
    if curl -s http://localhost:8083/health > /dev/null 2>&1; then
        echo "✅ API started successfully (PID: $API_PID)"
        echo "📍 API Server: http://localhost:8083"
        echo "📍 Smart Search: http://localhost:4000/api-search/"
        echo "📍 API Docs: http://localhost:4000/api-docs/"
    else
        echo "❌ API failed to start"
        exit 1
    fi
fi

# Start Jekyll if not running
if ! curl -s http://localhost:4000 > /dev/null 2>&1; then
    echo "🌐 Starting Jekyll server..."
    bundle exec jekyll serve --host 0.0.0.0 --port 4000 &
    JEKYLL_PID=$!
    
    echo "⏳ Waiting for Jekyll to start..."
    sleep 5
    
    if curl -s http://localhost:4000 > /dev/null 2>&1; then
        echo "✅ Jekyll started successfully (PID: $JEKYLL_PID)"
    else
        echo "❌ Jekyll failed to start"
    fi
else
    echo "✅ Jekyll already running at http://localhost:4000"
fi

echo ""
echo "🎉 Literature Notes Integration Ready!"
echo "📍 Documentation: http://localhost:4000"
echo "📍 Smart Search: http://localhost:4000/api-search/"
echo "📍 API Documentation: http://localhost:4000/api-docs/"
echo "📍 Direct API: http://localhost:8083"
echo ""
echo "🛑 To stop: pkill -f 'python minimal_api.py' && pkill -f jekyll"
"""
    
    with open('start_docs_with_api.sh', 'w') as f:
        f.write(startup_script)
    
    os.chmod('start_docs_with_api.sh', 0o755)
    print("✅ Created start_docs_with_api.sh")
    
    print("\n🎉 Integration complete!")
    return True

def update_navigation():
    """Update site navigation to include API features"""
    print("\n🧭 Updating site navigation...")
    
    # Check if _config.yml exists and update navigation
    try:
        config_path = '_config.yml'
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = f.read()
            
            # Add API navigation if not already present
            if 'api-search' not in config and 'Smart Search' not in config:
                navigation_addition = """
# API Integration
smart_search_enabled: true
api_base_url: "http://localhost:8083"
"""
                config += navigation_addition
                
                with open(config_path, 'w') as f:
                    f.write(config)
                
                print("✅ Updated _config.yml")
        
    except Exception as e:
        print(f"⚠️ Could not update _config.yml: {e}")

def main():
    """Main integration function"""
    print("🔗 Literature Notes API Integration")
    print("=" * 50)
    
    # Create integration files
    create_api_integration()
    
    # Update navigation
    update_navigation()
    
    print("\n📋 Next Steps:")
    print("1. Start the integrated system:")
    print("   ./start_docs_with_api.sh")
    print("")
    print("2. Or start manually:")
    print("   python minimal_api.py &")
    print("   bundle exec jekyll serve")
    print("")
    print("3. Access your documentation with API:")
    print("   📍 Main site: http://localhost:4000")
    print("   📍 Smart Search: http://localhost:4000/api-search/")
    print("   📍 API Docs: http://localhost:4000/api-docs/")
    print("")
    print("✨ Your literature notes now have intelligent search integrated!")

if __name__ == "__main__":
    main()