---
layout: "default"
title: "Search"
breadcrumbs:
  - title: "Home"
    url: "/"
---

<div class="search-container">
    <input type="text" id="search-input" class="search-box" placeholder="Search notes..." />
    <div id="search-results"></div>
</div>

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
let searchIndex;
let documents;

// Load search index
fetch('/assets/search-index.json')
    .then(response => response.json())
    .then(data => {
        documents = data;
        
        // Build lunr index
        searchIndex = lunr(function() {
            this.ref('id');
            this.field('title', { boost: 10 });
            this.field('content');
            this.field('tags', { boost: 5 });
            
            documents.forEach(doc => {
                this.add(doc);
            });
        });
        
        // Enable search
        document.getElementById('search-input').addEventListener('input', performSearch);
        
        // Check for URL params
        const urlParams = new URLSearchParams(window.location.search);
        const query = urlParams.get('q');
        if (query) {
            document.getElementById('search-input').value = query;
            performSearch();
        }
    });

function performSearch() {
    const query = document.getElementById('search-input').value;
    const resultsContainer = document.getElementById('search-results');
    
    if (!query.trim() || !searchIndex) {
        resultsContainer.innerHTML = '';
        return;
    }
    
    try {
        const results = searchIndex.search(query);
        displayResults(results, query);
    } catch (error) {
        console.error('Search error:', error);
        resultsContainer.innerHTML = '<p>Search error. Please try a different query.</p>';
    }
}

function displayResults(results, query) {
    const resultsContainer = document.getElementById('search-results');
    
    if (results.length === 0) {
        resultsContainer.innerHTML = `<p>No results found for "${query}"</p>`;
        return;
    }
    
    let html = `<h2>Found ${results.length} results for "${query}"</h2><div class="note-grid">`;
    
    results.slice(0, 20).forEach(result => {
        const doc = documents.find(d => d.id === result.ref);
        if (!doc) return;
        
        // Highlight search terms
        let excerpt = doc.content;
        const terms = query.toLowerCase().split(/\s+/);
        terms.forEach(term => {
            const regex = new RegExp(`(${term})`, 'gi');
            excerpt = excerpt.replace(regex, '<mark>$1</mark>');
        });
        
        html += `
        <div class="note-card">
            <h3><a href="${doc.url}">${doc.title}</a></h3>
            <div class="note-meta">
                ${doc.word_count} words
                ${doc.tags ? `• Tags: ${doc.tags}` : ''}
            </div>
            <div class="note-excerpt">${excerpt}</div>
        </div>`;
    });
    
    html += '</div>';
    resultsContainer.innerHTML = html;
}

// Update URL with search query
document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value;
    const url = new URL(window.location);
    if (query) {
        url.searchParams.set('q', query);
    } else {
        url.searchParams.delete('q');
    }
    window.history.replaceState({}, '', url);
});
</script>

<style>
.search-container {
    max-width: 800px;
    margin: 0 auto;
}

.search-box {
    width: 100%;
    max-width: none;
    font-size: 1.2rem;
    padding: 1rem;
    margin-bottom: 2rem;
}

#search-results {
    margin-top: 2rem;
}

#search-results h2 {
    color: var(--secondary-color);
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}

mark {
    background: #ffeb3b;
    padding: 0.1em 0.2em;
    border-radius: 0.2em;
}

.note-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}
</style>