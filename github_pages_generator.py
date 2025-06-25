#!/usr/bin/env python3
"""
GitHub Pages Generator for Zettelkasten
Creates GitHub Pages-compatible markdown files with proper navigation and cross-references.
"""

import os
import re
import json
import sqlite3
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
from urllib.parse import quote
import shutil


class GitHubPagesGenerator:
    """Generates GitHub Pages compatible structure from Zettelkasten database."""
    
    def __init__(self, db_path: str = "zettelkasten.db", output_dir: str = "docs"):
        self.db_path = db_path
        self.output_dir = Path(output_dir)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        
        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        
        # Path mappings for URL generation
        self.path_to_url = {}
        self.title_to_path = {}
        
    def generate_all(self):
        """Generate complete GitHub Pages structure."""
        print("🚀 Generating GitHub Pages structure...")
        
        # Create basic structure
        self._create_jekyll_config()
        self._create_layouts()
        self._create_assets()
        
        # Build path mappings
        self._build_path_mappings()
        
        # Generate pages
        self._generate_note_pages()
        self._generate_index_pages()
        self._generate_tag_pages()
        self._generate_topic_pages()
        self._generate_main_index()
        
        print(f"✅ GitHub Pages site generated in '{self.output_dir}'")
        print("\n📋 Next steps:")
        print("1. Push to GitHub repository")
        print("2. Enable GitHub Pages in repository settings")
        print("3. Choose 'Deploy from branch' and select 'docs' folder")
        print("4. Your site will be available at: https://username.github.io/repository-name/")
    
    def _create_jekyll_config(self):
        """Create Jekyll configuration file."""
        config = {
            'title': 'Literature Notes',
            'description': 'A comprehensive knowledge management system',
            'baseurl': '',
            'url': '',
            'theme': 'minima',
            'plugins': ['jekyll-feed', 'jekyll-sitemap'],
            'markdown': 'kramdown',
            'highlighter': 'rouge',
            'kramdown': {
                'input': 'GFM',
                'syntax_highlighter': 'rouge'
            },
            'exclude': ['*.py', '*.db', 'requirements.txt', 'zettel']
        }
        
        config_path = self.output_dir / "_config.yml"
        with open(config_path, 'w') as f:
            f.write("# Jekyll configuration for Literature Notes\n")
            for key, value in config.items():
                if isinstance(value, dict):
                    f.write(f"{key}:\n")
                    for subkey, subvalue in value.items():
                        f.write(f"  {subkey}: {subvalue}\n")
                elif isinstance(value, list):
                    f.write(f"{key}:\n")
                    for item in value:
                        f.write(f"  - {item}\n")
                else:
                    f.write(f"{key}: {value}\n")
    
    def _create_layouts(self):
        """Create Jekyll layout files."""
        layouts_dir = self.output_dir / "_layouts"
        layouts_dir.mkdir(exist_ok=True)
        
        # Default layout
        default_layout = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} - {% endif %}{{ site.title }}</title>
    <link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css">
</head>
<body>
    <header class="site-header">
        <nav class="site-nav">
            <a href="{{ "/" | relative_url }}" class="site-title">🧠 {{ site.title }}</a>
            <div class="nav-links">
                <a href="{{ "/topics/" | relative_url }}">📚 Topics</a>
                <a href="{{ "/tags/" | relative_url }}">🏷️ Tags</a>
                <a href="{{ "/search/" | relative_url }}">🔍 Search</a>
                <a href="{{ "/graph/" | relative_url }}">🕸️ Graph</a>
            </div>
        </nav>
    </header>
    
    <main class="page-content">
        {% if page.breadcrumbs %}
        <nav class="breadcrumbs">
            {% for crumb in page.breadcrumbs %}
                <a href="{{ crumb.url | relative_url }}">{{ crumb.title }}</a>
                {% unless forloop.last %} / {% endunless %}
            {% endfor %}
        </nav>
        {% endif %}
        
        <article class="post">
            {% if page.title %}
            <header class="post-header">
                <h1 class="post-title">{{ page.title }}</h1>
                {% if page.tags and page.tags.size > 0 %}
                <div class="post-tags">
                    {% for tag in page.tags %}
                        <a href="{{ "/tags/" | append: tag | append: "/" | relative_url }}" class="tag">#{{ tag }}</a>
                    {% endfor %}
                </div>
                {% endif %}
            </header>
            {% endif %}
            
            <div class="post-content">
                {{ content }}
            </div>
            
            {% if page.backlinks and page.backlinks.size > 0 %}
            <footer class="post-footer">
                <h3>📥 Referenced by</h3>
                <ul class="backlinks">
                    {% for backlink in page.backlinks %}
                        <li><a href="{{ backlink.url | relative_url }}">{{ backlink.title }}</a></li>
                    {% endfor %}
                </ul>
            </footer>
            {% endif %}
        </article>
    </main>
    
    <footer class="site-footer">
        <p>&copy; {{ 'now' | date: "%Y" }} Literature Notes. Generated with Zettelkasten system.</p>
    </footer>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/plugins/autoloader/prism-autoloader.min.js"></script>
</body>
</html>'''
        
        with open(layouts_dir / "default.html", 'w') as f:
            f.write(default_layout)
    
    def _create_assets(self):
        """Create CSS and JavaScript assets."""
        assets_dir = self.output_dir / "assets" / "css"
        assets_dir.mkdir(parents=True, exist_ok=True)
        
        css = '''/* Literature Notes Styles */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --info-color: #17a2b8;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --light-color: #f8f9fa;
    --dark-color: #343a40;
    --border-color: #dee2e6;
    --link-color: #0066cc;
    --code-bg: #f4f4f4;
}

* {
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #fff;
}

.site-header {
    background: var(--light-color);
    border-bottom: 1px solid var(--border-color);
    padding: 1rem 0;
    margin-bottom: 2rem;
}

.site-nav {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.site-title {
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
    color: var(--primary-color);
}

.nav-links {
    display: flex;
    gap: 1.5rem;
}

.nav-links a {
    text-decoration: none;
    color: var(--secondary-color);
    font-weight: 500;
    transition: color 0.2s;
}

.nav-links a:hover {
    color: var(--primary-color);
}

.page-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    min-height: calc(100vh - 200px);
}

.breadcrumbs {
    background: var(--light-color);
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
}

.breadcrumbs a {
    color: var(--link-color);
    text-decoration: none;
}

.breadcrumbs a:hover {
    text-decoration: underline;
}

.post-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border-color);
}

.post-title {
    color: var(--dark-color);
    margin-bottom: 0.5rem;
}

.post-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag {
    background: var(--primary-color);
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 500;
}

.tag:hover {
    background: #0056b3;
    color: white;
}

.post-content {
    margin-bottom: 3rem;
}

.post-content h1, .post-content h2, .post-content h3, 
.post-content h4, .post-content h5, .post-content h6 {
    color: var(--dark-color);
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.post-content h1 { font-size: 2rem; }
.post-content h2 { font-size: 1.5rem; }
.post-content h3 { font-size: 1.25rem; }

.post-content p {
    margin-bottom: 1rem;
}

.post-content ul, .post-content ol {
    margin-bottom: 1rem;
    padding-left: 2rem;
}

.post-content li {
    margin-bottom: 0.5rem;
}

.post-content code {
    background: var(--code-bg);
    padding: 0.2rem 0.4rem;
    border-radius: 0.25rem;
    font-size: 0.9em;
}

.post-content pre {
    background: var(--code-bg);
    padding: 1rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    margin-bottom: 1rem;
}

.post-content pre code {
    background: none;
    padding: 0;
}

.post-content blockquote {
    border-left: 4px solid var(--primary-color);
    padding-left: 1rem;
    margin: 1rem 0;
    font-style: italic;
    color: var(--secondary-color);
}

.post-content table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

.post-content th, .post-content td {
    border: 1px solid var(--border-color);
    padding: 0.5rem;
    text-align: left;
}

.post-content th {
    background: var(--light-color);
    font-weight: bold;
}

.post-footer {
    border-top: 1px solid var(--border-color);
    padding-top: 1.5rem;
    margin-top: 2rem;
}

.backlinks {
    list-style: none;
    padding: 0;
}

.backlinks li {
    margin-bottom: 0.5rem;
}

.backlinks a {
    color: var(--link-color);
    text-decoration: none;
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    transition: background-color 0.2s;
}

.backlinks a:hover {
    background: var(--light-color);
    text-decoration: none;
}

.site-footer {
    background: var(--light-color);
    border-top: 1px solid var(--border-color);
    padding: 2rem 0;
    margin-top: 3rem;
    text-align: center;
    color: var(--secondary-color);
}

/* Index pages */
.note-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.note-card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    padding: 1.5rem;
    transition: box-shadow 0.2s;
}

.note-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.note-card h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
}

.note-card h3 a {
    color: var(--dark-color);
    text-decoration: none;
}

.note-card h3 a:hover {
    color: var(--primary-color);
}

.note-meta {
    color: var(--secondary-color);
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.note-excerpt {
    color: #666;
    font-size: 0.95rem;
    line-height: 1.5;
}

/* Tag cloud */
.tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 2rem 0;
}

.tag-cloud .tag {
    font-size: calc(0.8rem + 0.3rem * var(--tag-weight, 1));
}

/* Search */
.search-box {
    width: 100%;
    max-width: 500px;
    padding: 0.75rem;
    border: 2px solid var(--border-color);
    border-radius: 0.5rem;
    font-size: 1rem;
    margin-bottom: 2rem;
}

.search-box:focus {
    outline: none;
    border-color: var(--primary-color);
}

/* Responsive */
@media (max-width: 768px) {
    .site-nav {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-links {
        gap: 1rem;
    }
    
    .note-grid {
        grid-template-columns: 1fr;
    }
    
    .page-content {
        padding: 0 0.5rem;
    }
}'''
        
        with open(assets_dir / "style.css", 'w') as f:
            f.write(css)
    
    def _build_path_mappings(self):
        """Build mappings between file paths, URLs, and titles."""
        notes = self.conn.execute("SELECT path, title FROM notes").fetchall()
        
        for note in notes:
            path = note['path']
            title = note['title']
            
            # Convert file path to URL path
            url_path = self._path_to_url_path(path)
            self.path_to_url[path] = url_path
            self.title_to_path[title.lower()] = path
    
    def _path_to_url_path(self, file_path: str) -> str:
        """Convert file system path to URL path."""
        # Remove .md extension and convert to URL-friendly format
        url_path = file_path.replace('.md', '')
        url_path = url_path.replace(' ', '-').lower()
        url_path = re.sub(r'[^a-z0-9\-_/]', '', url_path)
        return url_path + '/'
    
    def _generate_note_pages(self):
        """Generate individual note pages."""
        print("📝 Generating note pages...")
        
        notes = self.conn.execute("SELECT * FROM notes").fetchall()
        
        for note in notes:
            self._generate_single_note_page(note)
    
    def _generate_single_note_page(self, note):
        """Generate a single note page."""
        # Create directory structure
        url_path = self.path_to_url[note['path']]
        page_dir = self.output_dir / url_path.strip('/')
        page_dir.mkdir(parents=True, exist_ok=True)
        
        # Parse note data
        tags = json.loads(note['tags'])
        wikilinks = json.loads(note['wikilinks'])
        backlinks = json.loads(note['backlinks'])
        
        # Convert content - replace wikilinks with proper markdown links
        content = self._convert_wikilinks_to_markdown(note['content'])
        
        # Build frontmatter
        frontmatter = {
            'layout': 'default',
            'title': note['title'],
            'tags': tags,
            'word_count': note['word_count'],
            'created': note['created'],
            'modified': note['modified']
        }
        
        # Add backlinks for Jekyll
        if backlinks:
            backlink_data = []
            for backlink_path in backlinks:
                backlink_note = self.conn.execute(
                    "SELECT title FROM notes WHERE path = ?", 
                    (backlink_path,)
                ).fetchone()
                if backlink_note:
                    backlink_data.append({
                        'title': backlink_note['title'],
                        'url': self.path_to_url.get(backlink_path, '#')
                    })
            frontmatter['backlinks'] = backlink_data
        
        # Generate breadcrumbs
        path_parts = note['path'].split('/')
        if len(path_parts) > 1:
            breadcrumbs = [{'title': 'Home', 'url': '/'}]
            current_path = ''
            for i, part in enumerate(path_parts[:-1]):  # Exclude filename
                current_path += part + '/'
                breadcrumbs.append({
                    'title': part.replace('-', ' ').title(),
                    'url': f'/topics/{current_path.lower().replace(" ", "-")}/'
                })
            frontmatter['breadcrumbs'] = breadcrumbs
        
        # Write page
        page_content = self._format_frontmatter(frontmatter) + content
        
        with open(page_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _convert_wikilinks_to_markdown(self, content: str) -> str:
        """Convert [[wikilinks]] to proper markdown links."""
        def replace_wikilink(match):
            link_text = match.group(1).strip()
            
            # Find matching note by title
            matching_path = self.title_to_path.get(link_text.lower())
            if matching_path:
                url = self.path_to_url[matching_path]
                return f"[{link_text}]({url})"
            else:
                # Link not found, keep as text but mark it
                return f"*{link_text}*"
        
        return re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, content)
    
    def _format_frontmatter(self, data: dict) -> str:
        """Format frontmatter for Jekyll."""
        lines = ['---']
        for key, value in data.items():
            if isinstance(value, list):
                if value:  # Only add if list is not empty
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
    
    def _generate_index_pages(self):
        """Generate topic index pages."""
        print("📚 Generating topic indexes...")
        
        # Group notes by directory
        notes = self.conn.execute("SELECT * FROM notes ORDER BY path").fetchall()
        
        topic_groups = defaultdict(list)
        for note in notes:
            path_parts = note['path'].split('/')
            if len(path_parts) > 1:
                topic = path_parts[0]
                topic_groups[topic].append(note)
        
        # Create topic index pages
        topics_dir = self.output_dir / "topics"
        topics_dir.mkdir(exist_ok=True)
        
        for topic, topic_notes in topic_groups.items():
            self._generate_topic_index(topic, topic_notes)
    
    def _generate_topic_index(self, topic: str, notes):
        """Generate index page for a specific topic."""
        topic_dir = self.output_dir / "topics" / topic.lower().replace(' ', '-')
        topic_dir.mkdir(parents=True, exist_ok=True)
        
        # Group by subtopic
        subtopic_groups = defaultdict(list)
        for note in notes:
            path_parts = note['path'].split('/')
            if len(path_parts) > 2:
                subtopic = path_parts[1]
                subtopic_groups[subtopic].append(note)
            else:
                subtopic_groups['_root'].append(note)
        
        # Generate content
        content_lines = []
        
        if '_root' in subtopic_groups:
            content_lines.extend([
                "## Overview\n",
                '<div class="note-grid">'
            ])
            for note in subtopic_groups['_root']:
                url = self.path_to_url[note['path']]
                tags = json.loads(note['tags'])
                excerpt = note['content'][:200] + '...' if len(note['content']) > 200 else note['content']
                # Remove markdown formatting from excerpt
                excerpt = re.sub(r'[#*`\[\]()]', '', excerpt).strip()
                
                content_lines.append(f'''
<div class="note-card">
    <h3><a href="{url}">{note['title']}</a></h3>
    <div class="note-meta">
        {note['word_count']} words
        {f"• Tags: {', '.join(f'#{tag}' for tag in tags[:3])}" if tags else ""}
    </div>
    <div class="note-excerpt">{excerpt}</div>
</div>''')
            
            content_lines.append('</div>\n')
            del subtopic_groups['_root']
        
        # Add subtopics
        if subtopic_groups:
            content_lines.append("## Subtopics\n")
            for subtopic, subtopic_notes in sorted(subtopic_groups.items()):
                content_lines.append(f"### {subtopic.replace('-', ' ').title()}\n")
                content_lines.append('<div class="note-grid">')
                
                for note in subtopic_notes:
                    url = self.path_to_url[note['path']]
                    tags = json.loads(note['tags'])
                    excerpt = note['content'][:150] + '...' if len(note['content']) > 150 else note['content']
                    excerpt = re.sub(r'[#*`\[\]()]', '', excerpt).strip()
                    
                    content_lines.append(f'''
<div class="note-card">
    <h3><a href="{url}">{note['title']}</a></h3>
    <div class="note-meta">
        {note['word_count']} words
        {f"• Tags: {', '.join(f'#{tag}' for tag in tags[:2])}" if tags else ""}
    </div>
    <div class="note-excerpt">{excerpt}</div>
</div>''')
                
                content_lines.append('</div>\n')
        
        # Write page
        frontmatter = {
            'layout': 'default',
            'title': f"{topic.replace('-', ' ').title()} - Topics",
            'breadcrumbs': [
                {'title': 'Home', 'url': '/'},
                {'title': 'Topics', 'url': '/topics/'}
            ]
        }
        
        page_content = self._format_frontmatter(frontmatter) + '\n'.join(content_lines)
        
        with open(topic_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _generate_tag_pages(self):
        """Generate tag index and individual tag pages."""
        print("🏷️ Generating tag pages...")
        
        tags_dir = self.output_dir / "tags" 
        tags_dir.mkdir(exist_ok=True)
        
        # Get all tags with counts
        tag_data = self.conn.execute("""
            SELECT tag, COUNT(*) as count 
            FROM tags 
            GROUP BY tag 
            ORDER BY count DESC, tag
        """).fetchall()
        
        # Generate main tags index
        self._generate_tags_index(tag_data)
        
        # Generate individual tag pages
        for tag_row in tag_data:
            tag = tag_row['tag']
            notes = self.conn.execute("""
                SELECT n.* FROM notes n
                JOIN tags t ON n.path = t.note_path
                WHERE t.tag = ?
                ORDER BY n.title
            """, (tag,)).fetchall()
            
            self._generate_single_tag_page(tag, notes)
    
    def _generate_tags_index(self, tag_data):
        """Generate main tags index page."""
        content_lines = [
            '<div class="tag-cloud">'
        ]
        
        max_count = max(row['count'] for row in tag_data) if tag_data else 1
        
        for tag_row in tag_data:
            tag = tag_row['tag']
            count = tag_row['count']
            weight = count / max_count
            
            content_lines.append(
                f'<a href="{tag}/" class="tag" style="--tag-weight: {weight}">'
                f'#{tag} ({count})</a>'
            )
        
        content_lines.append('</div>')
        
        # Add tag list
        content_lines.extend([
            "\n## All Tags\n",
            "| Tag | Notes |",
            "|-----|-------|"
        ])
        
        for tag_row in tag_data:
            tag = tag_row['tag']
            count = tag_row['count']
            content_lines.append(f"| [#{tag}]({tag}/) | {count} |")
        
        frontmatter = {
            'layout': 'default',
            'title': 'Tags',
            'breadcrumbs': [
                {'title': 'Home', 'url': '/'}
            ]
        }
        
        page_content = self._format_frontmatter(frontmatter) + '\n'.join(content_lines)
        
        with open(self.output_dir / "tags" / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _generate_single_tag_page(self, tag: str, notes):
        """Generate page for a specific tag."""
        tag_dir = self.output_dir / "tags" / tag
        tag_dir.mkdir(exist_ok=True)
        
        content_lines = [
            f"Notes tagged with **#{tag}** ({len(notes)} total)\n",
            '<div class="note-grid">'
        ]
        
        for note in notes:
            url = self.path_to_url[note['path']]
            tags = json.loads(note['tags'])
            other_tags = [t for t in tags if t != tag]
            excerpt = note['content'][:200] + '...' if len(note['content']) > 200 else note['content']
            excerpt = re.sub(r'[#*`\[\]()]', '', excerpt).strip()
            
            content_lines.append(f'''
<div class="note-card">
    <h3><a href="{url}">{note['title']}</a></h3>
    <div class="note-meta">
        {note['word_count']} words
        {f"• Also: {', '.join(f'#{t}' for t in other_tags[:3])}" if other_tags else ""}
    </div>
    <div class="note-excerpt">{excerpt}</div>
</div>''')
        
        content_lines.append('</div>')
        
        frontmatter = {
            'layout': 'default',
            'title': f"#{tag}",
            'breadcrumbs': [
                {'title': 'Home', 'url': '/'},
                {'title': 'Tags', 'url': '/tags/'}
            ]
        }
        
        page_content = self._format_frontmatter(frontmatter) + '\n'.join(content_lines)
        
        with open(tag_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _generate_topic_pages(self):
        """Generate main topics index page."""
        topics_dir = self.output_dir / "topics"
        
        # Get topic statistics
        topic_stats = defaultdict(int)
        notes = self.conn.execute("SELECT path FROM notes").fetchall()
        
        for note in notes:
            path_parts = note['path'].split('/')
            if len(path_parts) > 1:
                topic = path_parts[0]
                topic_stats[topic] += 1
        
        content_lines = [
            "Browse notes by topic and category.\n",
            '<div class="note-grid">'
        ]
        
        for topic, count in sorted(topic_stats.items()):
            topic_title = topic.replace('-', ' ').title()
            topic_url = topic.lower().replace(' ', '-')
            
            content_lines.append(f'''
<div class="note-card">
    <h3><a href="{topic_url}/">{topic_title}</a></h3>
    <div class="note-meta">{count} notes</div>
    <div class="note-excerpt">Explore {topic_title.lower()} related notes and concepts.</div>
</div>''')
        
        content_lines.append('</div>')
        
        frontmatter = {
            'layout': 'default',
            'title': 'Topics',
            'breadcrumbs': [
                {'title': 'Home', 'url': '/'}
            ]
        }
        
        page_content = self._format_frontmatter(frontmatter) + '\n'.join(content_lines)
        
        with open(topics_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def _generate_main_index(self):
        """Generate main index page."""
        print("🏠 Generating main index...")
        
        # Get statistics  
        stats = self.conn.execute("""
            SELECT 
                COUNT(*) as total_notes,
                SUM(word_count) as total_words
            FROM notes
        """).fetchone()
        
        unique_tags = self.conn.execute("""
            SELECT COUNT(DISTINCT tag) as unique_tags
            FROM tags
        """).fetchone()
        
        stats = dict(stats)
        stats['unique_tags'] = unique_tags['unique_tags']
        
        total_links = self.conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
        
        # Get recent notes
        recent_notes = self.conn.execute("""
            SELECT * FROM notes 
            ORDER BY modified DESC 
            LIMIT 6
        """).fetchall()
        
        # Get top tags
        top_tags = self.conn.execute("""
            SELECT tag, COUNT(*) as count 
            FROM tags 
            GROUP BY tag 
            ORDER BY count DESC 
            LIMIT 12
        """).fetchall()
        
        content_lines = [
            "Welcome to my digital knowledge garden - a collection of interconnected notes on various topics including programming, philosophy, science, and more.\n",
            
            "## 📊 Overview\n",
            
            f"- **{stats['total_notes']} notes** with {stats['total_words']:,} total words",
            f"- **{total_links} connections** between ideas", 
            f"- **{stats['unique_tags']} tags** for organization",
            f"- Last updated: {datetime.now().strftime('%B %d, %Y')}\n",
            
            "## 🗂️ Browse\n",
            
            '<div class="note-grid">',
            '''
<div class="note-card">
    <h3><a href="topics/">📚 Topics</a></h3>
    <div class="note-excerpt">Browse notes organized by subject area and category.</div>
</div>

<div class="note-card">
    <h3><a href="tags/">🏷️ Tags</a></h3>
    <div class="note-excerpt">Explore notes by tags and themes.</div>
</div>

<div class="note-card">
    <h3><a href="search/">🔍 Search</a></h3>
    <div class="note-excerpt">Search across all notes and content.</div>
</div>

<div class="note-card">
    <h3><a href="graph/">🕸️ Knowledge Graph</a></h3>
    <div class="note-excerpt">Visualize connections between ideas.</div>
</div>''',
            '</div>\n',
            
            "## 🏷️ Popular Tags\n",
            
            '<div class="tag-cloud">'
        ]
        
        max_count = max(row['count'] for row in top_tags) if top_tags else 1
        for tag_row in top_tags:
            tag = tag_row['tag']
            count = tag_row['count']
            weight = count / max_count
            content_lines.append(
                f'<a href="tags/{tag}/" class="tag" style="--tag-weight: {weight}">'
                f'#{tag} ({count})</a>'
            )
        
        content_lines.extend([
            '</div>\n',
            
            "## 📝 Recent Updates\n",
            
            '<div class="note-grid">'
        ])
        
        for note in recent_notes:
            url = self.path_to_url[note['path']]
            tags = json.loads(note['tags'])
            excerpt = note['content'][:150] + '...' if len(note['content']) > 150 else note['content']
            excerpt = re.sub(r'[#*`\[\]()]', '', excerpt).strip()
            
            content_lines.append(f'''
<div class="note-card">
    <h3><a href="{url}">{note['title']}</a></h3>
    <div class="note-meta">
        {note['word_count']} words
        {f"• {', '.join(f'#{tag}' for tag in tags[:2])}" if tags else ""}
    </div>
    <div class="note-excerpt">{excerpt}</div>
</div>''')
        
        content_lines.append('</div>')
        
        frontmatter = {
            'layout': 'default',
            'title': 'Literature Notes'
        }
        
        page_content = self._format_frontmatter(frontmatter) + '\n'.join(content_lines)
        
        with open(self.output_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(page_content)
    
    def close(self):
        """Close database connection."""
        self.conn.close()


def main():
    """Main CLI interface for GitHub Pages generation."""
    parser = argparse.ArgumentParser(description="GitHub Pages Generator for Zettelkasten")
    parser.add_argument("--db", default="zettelkasten.db", help="Database file path")
    parser.add_argument("--output", default="docs", help="Output directory")
    parser.add_argument("--clean", action="store_true", help="Clean output directory first")
    
    args = parser.parse_args()
    
    # Clean output directory if requested
    if args.clean and Path(args.output).exists():
        shutil.rmtree(args.output)
        print(f"🧹 Cleaned output directory: {args.output}")
    
    generator = GitHubPagesGenerator(args.db, args.output)
    
    try:
        generator.generate_all()
    finally:
        generator.close()


if __name__ == "__main__":
    main()