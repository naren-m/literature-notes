#!/usr/bin/env python3
"""
Search functionality generator for GitHub Pages
Creates client-side search using lunr.js
"""

import json
import sqlite3
import argparse
from pathlib import Path
import re


class SearchGenerator:
    """Generates client-side search functionality for GitHub Pages."""
    
    def __init__(self, db_path: str = "zettelkasten.db", output_dir: str = "docs"):
        self.db_path = db_path
        self.output_dir = Path(output_dir)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        
        # Path mappings
        self.path_to_url = {}
        self._build_path_mappings()
    
    def _build_path_mappings(self):
        """Build mappings between file paths and URLs."""
        notes = self.conn.execute("SELECT path FROM notes").fetchall()
        
        for note in notes:
            path = note['path']
            url_path = self._path_to_url_path(path)
            self.path_to_url[path] = url_path
    
    def _path_to_url_path(self, file_path: str) -> str:
        """Convert file system path to URL path."""
        url_path = file_path.replace('.md', '')
        url_path = url_path.replace(' ', '-').lower()
        url_path = re.sub(r'[^a-z0-9\-_/]', '', url_path)
        return url_path + '/'
    
    def generate_search_functionality(self):
        """Generate complete search functionality."""
        print("🔍 Generating search functionality...")
        
        # Create search directory
        search_dir = self.output_dir / "search"
        search_dir.mkdir(exist_ok=True)
        
        # Generate search index
        self._generate_search_index()
        
        # Generate search page
        self._generate_search_page()
        
        # Copy search assets
        self._create_search_assets()
        
        print("✅ Search functionality generated")
    
    def _generate_search_index(self):
        """Generate search index JSON file."""
        notes = self.conn.execute("SELECT * FROM notes").fetchall()
        
        search_index = []
        
        for note in notes:
            # Clean content for search
            content = note['content']
            # Remove markdown formatting
            content = re.sub(r'[#*`\[\]()]', '', content)
            # Remove extra whitespace
            content = ' '.join(content.split())
            # Truncate for search index
            content = content[:500] + '...' if len(content) > 500 else content
            
            tags = json.loads(note['tags'])
            url = self.path_to_url[note['path']]
            
            search_index.append({
                'id': note['path'],
                'title': note['title'],
                'content': content,
                'tags': ' '.join(tags),
                'url': url,
                'word_count': note['word_count']
            })
        
        # Write search index
        with open(self.output_dir / "assets" / "search-index.json", 'w', encoding='utf-8') as f:
            json.dump(search_index, f, indent=2)
    
    def _generate_search_page(self):
        """Generate search page."""
        content = '''
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
        const terms = query.toLowerCase().split(/\\s+/);
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
</style>'''
        
        frontmatter = {
            'layout': 'default',
            'title': 'Search',
            'breadcrumbs': [
                {'title': 'Home', 'url': '/'}
            ]
        }
        
        page_content = self._format_frontmatter(frontmatter) + content
        
        with open(self.output_dir / "search" / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _create_search_assets(self):
        """Create additional search assets."""
        assets_dir = self.output_dir / "assets"
        assets_dir.mkdir(exist_ok=True)
        
        # Create a simple search suggestion system
        notes = self.conn.execute("SELECT title FROM notes ORDER BY title").fetchall()
        titles = [note['title'] for note in notes]
        
        # Get popular tags
        tags = self.conn.execute("""
            SELECT tag, COUNT(*) as count 
            FROM tags 
            GROUP BY tag 
            ORDER BY count DESC 
            LIMIT 50
        """).fetchall()
        
        suggestions = {
            'titles': titles,
            'tags': [f"#{tag['tag']}" for tag in tags]
        }
        
        with open(assets_dir / "search-suggestions.json", 'w', encoding='utf-8') as f:
            json.dump(suggestions, f, indent=2)
    
    def _format_frontmatter(self, data: dict) -> str:
        """Format frontmatter for Jekyll."""
        lines = ['---']
        for key, value in data.items():
            if isinstance(value, list):
                if value:
                    lines.append(f"{key}:")
                    for item in value:
                        if isinstance(item, dict):
                            lines.append(f"  - title: \"{item['title']}\"")
                            lines.append(f"    url: \"{item['url']}\"")
                        else:
                            lines.append(f"  - {item}")
            elif isinstance(value, str):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        lines.extend(['---', ''])
        return '\n'.join(lines)
    
    def close(self):
        """Close database connection."""
        self.conn.close()


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description="Search Generator for GitHub Pages")
    parser.add_argument("--db", default="zettelkasten.db", help="Database file path")
    parser.add_argument("--output", default="docs", help="Output directory")
    
    args = parser.parse_args()
    
    generator = SearchGenerator(args.db, args.output)
    
    try:
        generator.generate_search_functionality()
    finally:
        generator.close()


if __name__ == "__main__":
    main()