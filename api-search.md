---
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
        
        <h3>🔧 Start API Server</h3>
        <p>If the API status shows disconnected, start the server with:</p>
        <pre><code>python minimal_api.py</code></pre>
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
    if (e.key === 'Enter' && e.target.value.trim()) {
        performSearch(e.target.value.trim());
    }
});

// Initialize on page load
checkApiStatus();
</script>