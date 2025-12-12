#!/usr/bin/env python3
"""
Copy interactive graph to GitHub Pages
"""

import shutil
from pathlib import Path


def copy_graph_to_pages(docs_dir="docs"):
    """Copy knowledge graph to GitHub Pages."""
    docs_path = Path(docs_dir)
    graph_dir = docs_path / "graph"
    graph_dir.mkdir(exist_ok=True)
    
    # Copy the knowledge graph HTML file
    if Path("knowledge_graph.html").exists():
        shutil.copy("knowledge_graph.html", graph_dir / "index.html")
        print("✅ Copied knowledge graph to GitHub Pages")
        
        # Create a markdown wrapper for Jekyll
        frontmatter = '''---
layout: default
title: Knowledge Graph
breadcrumbs:
  - title: Home
    url: /
---

<iframe src="index.html" width="100%" height="800px" frameborder="0" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

<p style="margin-top: 1rem; color: #666; font-size: 0.9rem;">
Interactive knowledge graph showing connections between notes. Click and drag to explore, use filters to focus on specific topics.
</p>
'''
        
        with open(graph_dir / "wrapper.md", 'w') as f:
            f.write(frontmatter)
        
    else:
        print("❌ knowledge_graph.html not found. Run visualize.py first.")


if __name__ == "__main__":
    copy_graph_to_pages()