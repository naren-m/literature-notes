---
layout: default
title: Smart Search
---

# Smart Search

Use natural language to explore your knowledge with advanced search capabilities.

<style>
.smart-search-container {
    max-width: 900px;
    margin: 0 auto;
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

.synthesis-card {
    background: #e8f4f8;
    border-left: 4px solid #007bff;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 4px;
}

.concept-bridge {
    background: #f0f8ff;
    padding: 0.5rem;
    margin: 0.5rem 0;
    border-radius: 4px;
}

.loading {
    text-align: center;
    padding: 2rem;
    color: #666;
}
</style>

<div class="smart-search-container">
    <input type="text" 
           class="smart-search-box" 
           id="smartSearchInput" 
           placeholder="Try: 'connections between ayurveda and programming' or 'recent notes about cryptography'"
           autocomplete="off">
    
    <div class="search-examples">
        <h3>Try these searches:</h3>
        <span class="example-query" onclick="runExample(this)">connections between sanskrit and computer science</span>
        <span class="example-query" onclick="runExample(this)">recent notes about leadership</span>
        <span class="example-query" onclick="runExample(this)">similar to memory palace</span>
        <span class="example-query" onclick="runExample(this)">notes about ayurveda #health</span>
    </div>
    
    <div id="synthesisSection" style="display: none;">
        <h2>Knowledge Synthesis</h2>
        <div id="synthesisContent"></div>
    </div>
    
    <div id="searchResults"></div>
</div>

<script>
// Enhanced search with synthesis capabilities
let searchIndex = null;
let knowledgeGraph = {};

async function initSmartSearch() {
    try {
        const response = await fetch('/assets/search-index.json');
        searchIndex = await response.json();
        
        // Build knowledge graph from search index
        buildKnowledgeGraph();
        
        // Check for query parameter
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

function buildKnowledgeGraph() {
    // Create a simple graph from tags and titles
    searchIndex.forEach(note => {
        const tags = note.tags ? note.tags.split(' ') : [];
        tags.forEach(tag => {
            if (!knowledgeGraph[tag]) {
                knowledgeGraph[tag] = [];
            }
            knowledgeGraph[tag].push(note);
        });
    });
}

function runExample(element) {
    const query = element.textContent;
    document.getElementById('smartSearchInput').value = query;
    performSmartSearch(query);
}

async function performSmartSearch(query) {
    const resultsDiv = document.getElementById('searchResults');
    const synthesisDiv = document.getElementById('synthesisSection');
    
    resultsDiv.innerHTML = '<div class="loading">Searching...</div>';
    
    // Parse query type
    const queryLower = query.toLowerCase();
    const isConnectionQuery = queryLower.includes('connection') || queryLower.includes('between');
    const isSimilarQuery = queryLower.includes('similar') || queryLower.includes('like');
    const isRecentQuery = queryLower.includes('recent') || queryLower.includes('latest');
    
    let results = [];
    
    if (isConnectionQuery) {
        results = findConnections(query);
        showSynthesis(query, results);
    } else if (isSimilarQuery) {
        results = findSimilar(query);
    } else if (isRecentQuery) {
        results = findRecent(query);
    } else {
        results = enhancedSearch(query);
    }
    
    displayResults(results, query);
}

function findConnections(query) {
    const terms = extractTerms(query);
    if (terms.length < 2) return [];
    
    // Find notes that mention multiple terms
    const termMatches = {};
    terms.forEach(term => {
        termMatches[term] = searchIndex.filter(note => 
            note.content.toLowerCase().includes(term) ||
            note.title.toLowerCase().includes(term)
        );
    });
    
    // Find intersections
    let connections = [];
    const allNotes = Object.values(termMatches).flat();
    const noteCount = {};
    
    allNotes.forEach(note => {
        noteCount[note.id] = (noteCount[note.id] || 0) + 1;
    });
    
    // Get notes that appear for multiple terms
    Object.entries(noteCount).forEach(([id, count]) => {
        if (count > 1) {
            const note = searchIndex.find(n => n.id === id);
            if (note) {
                connections.push({...note, connectionScore: count});
            }
        }
    });
    
    return connections.sort((a, b) => b.connectionScore - a.connectionScore);
}

function findSimilar(query) {
    const referenceTerm = query.replace(/similar to|like/gi, '').trim();
    
    // Find reference note
    const reference = searchIndex.find(note => 
        note.title.toLowerCase().includes(referenceTerm.toLowerCase())
    );
    
    if (!reference) return [];
    
    // Find notes with similar tags
    const refTags = reference.tags ? reference.tags.split(' ') : [];
    
    return searchIndex
        .filter(note => note.id !== reference.id)
        .map(note => {
            const noteTags = note.tags ? note.tags.split(' ') : [];
            const sharedTags = refTags.filter(tag => noteTags.includes(tag));
            return {...note, similarity: sharedTags.length};
        })
        .filter(note => note.similarity > 0)
        .sort((a, b) => b.similarity - a.similarity)
        .slice(0, 10);
}

function findRecent(query) {
    // Simple simulation - in production would use actual dates
    const searchTerms = extractTerms(query.replace(/recent|latest|new/gi, ''));
    
    let results = searchIndex;
    
    if (searchTerms.length > 0) {
        results = results.filter(note => 
            searchTerms.some(term => 
                note.content.toLowerCase().includes(term) ||
                note.title.toLowerCase().includes(term)
            )
        );
    }
    
    // Simulate recency by random selection (in production, would sort by date)
    return results.slice(0, 20);
}

function enhancedSearch(query) {
    const terms = extractTerms(query);
    
    return searchIndex
        .map(note => {
            let score = 0;
            const titleLower = note.title.toLowerCase();
            const contentLower = note.content.toLowerCase();
            
            terms.forEach(term => {
                if (titleLower.includes(term)) score += 10;
                if (contentLower.includes(term)) score += 1;
                if (note.tags && note.tags.toLowerCase().includes(term)) score += 5;
            });
            
            return {...note, score};
        })
        .filter(note => note.score > 0)
        .sort((a, b) => b.score - a.score)
        .slice(0, 20);
}

function showSynthesis(query, results) {
    const synthesisDiv = document.getElementById('synthesisSection');
    const contentDiv = document.getElementById('synthesisContent');
    
    if (results.length > 2) {
        const terms = extractTerms(query);
        
        let synthesisHTML = `
            <div class="synthesis-card">
                <h3>Synthesis: Connecting ${terms.join(' and ')}</h3>
                <p>Found ${results.length} notes that bridge these concepts:</p>
                <ul>
        `;
        
        results.slice(0, 5).forEach(note => {
            synthesisHTML += `<li><a href="${note.url}">${note.title}</a></li>`;
        });
        
        synthesisHTML += `
                </ul>
                <div class="concept-bridge">
                    💡 <strong>Insight:</strong> These notes suggest an interdisciplinary connection 
                    that could lead to new understanding.
                </div>
            </div>
        `;
        
        contentDiv.innerHTML = synthesisHTML;
        synthesisDiv.style.display = 'block';
    } else {
        synthesisDiv.style.display = 'none';
    }
}

function extractTerms(query) {
    const stopWords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                      'to', 'for', 'of', 'with', 'between', 'connection', 
                      'similar', 'like', 'recent', 'latest', 'about', 'notes'];
    
    return query.toLowerCase()
        .split(/\s+/)
        .filter(word => word.length > 2 && !stopWords.includes(word));
}

function displayResults(results, query) {
    const resultsDiv = document.getElementById('searchResults');
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found. Try different keywords.</p>';
        return;
    }
    
    let html = '<h2>Search Results</h2><div class="note-grid">';
    
    results.forEach(result => {
        const highlightedTitle = highlightTerms(result.title, query);
        const highlightedContent = highlightTerms(result.content, query);
        
        html += `
            <div class="note-card">
                <h3><a href="${result.url}">${highlightedTitle}</a></h3>
                <div class="note-meta">
                    📝 ${result.word_count || 0} words
                    ${result.tags ? `🏷️ ${result.tags}` : ''}
                    ${result.connectionScore ? `🔗 Connections: ${result.connectionScore}` : ''}
                    ${result.similarity ? `✨ Similarity: ${result.similarity}` : ''}
                </div>
                <p>${highlightedContent}</p>
            </div>
        `;
    });
    
    html += '</div>';
    resultsDiv.innerHTML = html;
}

function highlightTerms(text, query) {
    const terms = extractTerms(query);
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

// Initialize
initSmartSearch();
</script>