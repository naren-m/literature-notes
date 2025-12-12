#!/usr/bin/env python3
"""
Zettelkasten Visualization Tool
Creates visual representations of note connections and knowledge graphs.
"""

import json
import sqlite3
import argparse
from pathlib import Path
from collections import defaultdict
import html

try:
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False


class ZettelkastenVisualizer:
    """Creates visualizations of the Zettelkasten knowledge graph."""
    
    def __init__(self, db_path: str = "zettelkasten.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
    
    def generate_html_graph(self, output_path: str = "knowledge_graph.html"):
        """Generate an interactive HTML graph using D3.js."""
        nodes, links = self._get_graph_data()
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Zettelkasten Knowledge Graph</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }}
        
        .controls {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        
        .control-group {{
            display: inline-block;
            margin-right: 20px;
            margin-bottom: 10px;
        }}
        
        label {{
            display: block;
            font-weight: bold;
            color: #555;
            margin-bottom: 5px;
        }}
        
        input, select {{
            padding: 5px 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        
        button {{
            background: #007bff;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }}
        
        button:hover {{
            background: #0056b3;
        }}
        
        #graph {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .tooltip {{
            position: absolute;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
            font-size: 12px;
            max-width: 300px;
            z-index: 1000;
        }}
        
        .node {{
            cursor: pointer;
            stroke: #fff;
            stroke-width: 2px;
        }}
        
        .link {{
            stroke: #999;
            stroke-opacity: 0.6;
        }}
        
        .node-label {{
            font-size: 10px;
            fill: #333;
            text-anchor: middle;
            pointer-events: none;
        }}
        
        .stats {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-top: 20px;
        }}
        
        .stats h3 {{
            margin-top: 0;
            color: #333;
        }}
        
        .stat-item {{
            display: inline-block;
            margin-right: 30px;
            font-size: 14px;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #007bff;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧠 Zettelkasten Knowledge Graph</h1>
        
        <div class="controls">
            <div class="control-group">
                <label>Search Notes:</label>
                <input type="text" id="searchInput" placeholder="Type to filter notes...">
            </div>
            <div class="control-group">
                <label>Filter by Tag:</label>
                <select id="tagFilter">
                    <option value="">All tags</option>
                </select>
            </div>
            <div class="control-group">
                <label>Min Connections:</label>
                <input type="number" id="minConnections" value="0" min="0" max="10">
            </div>
            <div class="control-group">
                <label></label>
                <button onclick="resetGraph()">Reset View</button>
            </div>
        </div>
        
        <div id="graph"></div>
        
        <div class="stats">
            <h3>📊 Graph Statistics</h3>
            <div class="stat-item">
                <span>Total Notes: </span>
                <span class="stat-value" id="totalNotes">{len(nodes)}</span>
            </div>
            <div class="stat-item">
                <span>Total Connections: </span>
                <span class="stat-value" id="totalLinks">{len(links)}</span>
            </div>
            <div class="stat-item">
                <span>Filtered Notes: </span>
                <span class="stat-value" id="filteredNotes">{len(nodes)}</span>
            </div>
        </div>
    </div>
    
    <div class="tooltip" id="tooltip" style="display: none;"></div>
    
    <script>
        // Data
        const originalNodes = {json.dumps(nodes, indent=2)};
        const originalLinks = {json.dumps(links, indent=2)};
        
        let nodes = [...originalNodes];
        let links = [...originalLinks];
        
        // Graph dimensions
        const width = 1200;
        const height = 700;
        
        // Create SVG
        const svg = d3.select("#graph")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
        
        // Create zoom behavior
        const zoom = d3.zoom()
            .scaleExtent([0.1, 4])
            .on("zoom", (event) => {{
                g.attr("transform", event.transform);
            }});
        
        svg.call(zoom);
        
        // Create main group for zooming
        const g = svg.append("g");
        
        // Create force simulation
        let simulation;
        
        // Tooltip
        const tooltip = d3.select("#tooltip");
        
        // Color scale for tags
        const colorScale = d3.scaleOrdinal(d3.schemeCategory10);
        
        // Initialize graph
        function initGraph() {{
            // Get all unique tags for the filter
            const allTags = [...new Set(nodes.flatMap(n => n.tags))].sort();
            const tagSelect = d3.select("#tagFilter");
            tagSelect.selectAll("option").remove();
            tagSelect.append("option").attr("value", "").text("All tags");
            allTags.forEach(tag => {{
                tagSelect.append("option").attr("value", tag).text(tag);
            }});
            
            updateGraph();
        }}
        
        function updateGraph() {{
            // Clear existing elements
            g.selectAll("*").remove();
            
            // Filter nodes and links
            const searchTerm = d3.select("#searchInput").property("value").toLowerCase();
            const selectedTag = d3.select("#tagFilter").property("value");
            const minConnections = +d3.select("#minConnections").property("value");
            
            // Filter nodes
            let filteredNodes = originalNodes.filter(node => {{
                const matchesSearch = !searchTerm || 
                    node.title.toLowerCase().includes(searchTerm) ||
                    node.content.toLowerCase().includes(searchTerm);
                
                const matchesTag = !selectedTag || node.tags.includes(selectedTag);
                
                const connectionCount = originalLinks.filter(link => 
                    link.source === node.id || link.target === node.id
                ).length;
                const matchesConnections = connectionCount >= minConnections;
                
                return matchesSearch && matchesTag && matchesConnections;
            }});
            
            const nodeIds = new Set(filteredNodes.map(n => n.id));
            
            // Filter links to only include those between filtered nodes
            let filteredLinks = originalLinks.filter(link => 
                nodeIds.has(link.source) && nodeIds.has(link.target)
            );
            
            nodes = filteredNodes;
            links = filteredLinks;
            
            // Update stats
            d3.select("#filteredNotes").text(nodes.length);
            
            if (nodes.length === 0) {{
                g.append("text")
                    .attr("x", width / 2)
                    .attr("y", height / 2)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "20px")
                    .attr("fill", "#999")
                    .text("No notes match the current filters");
                return;
            }}
            
            // Create force simulation
            simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(d => Math.sqrt(d.word_count) * 0.5 + 10));
            
            // Create links
            const link = g.append("g")
                .selectAll("line")
                .data(links)
                .enter().append("line")
                .attr("class", "link")
                .attr("stroke-width", 1);
            
            // Create nodes
            const node = g.append("g")
                .selectAll("circle")
                .data(nodes)
                .enter().append("circle")
                .attr("class", "node")
                .attr("r", d => Math.sqrt(d.word_count) * 0.5 + 5)
                .attr("fill", d => {{
                    if (d.tags.length > 0) {{
                        return colorScale(d.tags[0]);
                    }}
                    return "#69b3a2";
                }})
                .on("mouseover", showTooltip)
                .on("mouseout", hideTooltip)
                .on("click", nodeClick)
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));
            
            // Create labels
            const label = g.append("g")
                .selectAll("text")
                .data(nodes)
                .enter().append("text")
                .attr("class", "node-label")
                .text(d => d.title.length > 20 ? d.title.substring(0, 20) + "..." : d.title);
            
            // Update positions on tick
            simulation.on("tick", () => {{
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);
                
                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);
                
                label
                    .attr("x", d => d.x)
                    .attr("y", d => d.y + 25);
            }});
        }}
        
        function showTooltip(event, d) {{
            tooltip
                .style("display", "block")
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px")
                .html(`
                    <strong>${{d.title}}</strong><br>
                    <em>${{d.path}}</em><br>
                    Words: ${{d.word_count}}<br>
                    Tags: ${{d.tags.join(", ") || "None"}}<br>
                    Links: ${{d.wikilinks.length}}<br>
                    Backlinks: ${{d.backlinks.length}}
                `);
        }}
        
        function hideTooltip() {{
            tooltip.style("display", "none");
        }}
        
        function nodeClick(event, d) {{
            // Highlight connected nodes
            const connectedNodeIds = new Set();
            connectedNodeIds.add(d.id);
            
            links.forEach(link => {{
                if (link.source.id === d.id) connectedNodeIds.add(link.target.id);
                if (link.target.id === d.id) connectedNodeIds.add(link.source.id);
            }});
            
            g.selectAll(".node")
                .style("opacity", node => connectedNodeIds.has(node.id) ? 1 : 0.3);
            
            g.selectAll(".link")
                .style("opacity", link => 
                    link.source.id === d.id || link.target.id === d.id ? 1 : 0.1
                );
        }}
        
        function resetGraph() {{
            d3.select("#searchInput").property("value", "");
            d3.select("#tagFilter").property("value", "");
            d3.select("#minConnections").property("value", 0);
            
            g.selectAll(".node").style("opacity", 1);
            g.selectAll(".link").style("opacity", 1);
            
            updateGraph();
        }}
        
        // Drag functions
        function dragstarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }}
        
        function dragged(event, d) {{
            d.fx = event.x;
            d.fy = event.y;
        }}
        
        function dragended(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }}
        
        // Event listeners
        d3.select("#searchInput").on("input", updateGraph);
        d3.select("#tagFilter").on("change", updateGraph);
        d3.select("#minConnections").on("input", updateGraph);
        
        // Initialize
        initGraph();
    </script>
</body>
</html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Interactive HTML graph generated: {output_path}")
        return output_path
    
    def generate_network_graph(self, output_path: str = "network_graph.png"):
        """Generate a static network graph using NetworkX and Matplotlib."""
        if not HAS_NETWORKX:
            print("NetworkX and Matplotlib are required for static graphs.")
            print("Install with: pip install networkx matplotlib")
            return None
        
        nodes, links = self._get_graph_data()
        
        # Create NetworkX graph
        G = nx.Graph()
        
        # Add nodes
        for node in nodes:
            G.add_node(node['id'], 
                      title=node['title'],
                      word_count=node['word_count'],
                      tags=node['tags'])
        
        # Add edges
        for link in links:
            G.add_edge(link['source'], link['target'])
        
        # Create layout
        pos = nx.spring_layout(G, k=3, iterations=50)
        
        # Set up the plot
        plt.figure(figsize=(16, 12))
        plt.title("Zettelkasten Knowledge Graph", fontsize=16, fontweight='bold')
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.5, edge_color='gray')
        
        # Prepare node attributes
        node_sizes = [G.nodes[node]['word_count'] * 2 + 100 for node in G.nodes()]
        node_colors = []
        
        # Color nodes by primary tag
        color_map = {}
        colors = plt.cm.Set3(range(12))
        color_idx = 0
        
        for node in G.nodes():
            tags = G.nodes[node]['tags']
            if tags:
                primary_tag = tags[0]
                if primary_tag not in color_map:
                    color_map[primary_tag] = colors[color_idx % len(colors)]
                    color_idx += 1
                node_colors.append(color_map[primary_tag])
            else:
                node_colors.append('lightgray')
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, 
                             node_size=node_sizes,
                             node_color=node_colors,
                             alpha=0.8)
        
        # Draw labels for highly connected nodes
        high_degree_nodes = [n for n, d in G.degree() if d >= 2]
        labels = {n: G.nodes[n]['title'][:15] + ('...' if len(G.nodes[n]['title']) > 15 else '') 
                 for n in high_degree_nodes}
        
        nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')
        
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        plt.close()
        
        print(f"Static network graph generated: {output_path}")
        return output_path
    
    def _get_graph_data(self):
        """Get nodes and links data for visualization."""
        # Get all notes
        notes = self.conn.execute("SELECT * FROM notes").fetchall()
        
        # Get all links
        links_query = self.conn.execute("""
            SELECT source_path, target_path FROM links
        """).fetchall()
        
        # Create nodes list
        nodes = []
        for note in notes:
            nodes.append({
                'id': note['path'],
                'title': note['title'],
                'path': note['path'],
                'word_count': note['word_count'],
                'tags': json.loads(note['tags']),
                'wikilinks': json.loads(note['wikilinks']),
                'backlinks': json.loads(note['backlinks']),
                'content': note['content'][:200] + '...' if len(note['content']) > 200 else note['content']
            })
        
        # Create links list
        links = []
        for link in links_query:
            links.append({
                'source': link['source_path'],
                'target': link['target_path']
            })
        
        return nodes, links
    
    def generate_tag_hierarchy(self, output_path: str = "tag_hierarchy.html"):
        """Generate a hierarchical view of tags and their relationships."""
        # Get tag co-occurrence data
        tag_cooccurrence = defaultdict(int)
        notes = self.conn.execute("SELECT tags FROM notes").fetchall()
        
        for note in notes:
            tags = json.loads(note['tags'])
            for i, tag1 in enumerate(tags):
                for tag2 in tags[i+1:]:
                    pair = tuple(sorted([tag1, tag2]))
                    tag_cooccurrence[pair] += 1
        
        # Generate HTML
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Tag Hierarchy - Zettelkasten</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .tag-item {{ 
            background: #f0f8ff; 
            padding: 10px; 
            margin: 5px 0; 
            border-radius: 5px; 
            border-left: 4px solid #007bff;
        }}
        .co-occurrence {{ 
            color: #666; 
            font-size: 0.9em; 
            margin-left: 20px; 
        }}
        h1 {{ color: #333; }}
        h2 {{ color: #555; margin-top: 30px; }}
    </style>
</head>
<body>
    <h1>🏷️ Tag Hierarchy</h1>
    <h2>Tag Co-occurrence Patterns</h2>
        """
        
        # Sort by co-occurrence frequency
        sorted_cooccurrences = sorted(tag_cooccurrence.items(), key=lambda x: x[1], reverse=True)
        
        for (tag1, tag2), count in sorted_cooccurrences[:20]:
            html_content += f"""
    <div class="tag-item">
        <strong>#{tag1}</strong> + <strong>#{tag2}</strong>
        <div class="co-occurrence">Appears together in {count} notes</div>
    </div>
            """
        
        html_content += """
</body>
</html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Tag hierarchy generated: {output_path}")
        return output_path
    
    def close(self):
        """Close database connection."""
        self.conn.close()


def main():
    """Main CLI interface for visualization."""
    parser = argparse.ArgumentParser(description="Zettelkasten Visualization Tool")
    parser.add_argument("--db", default="zettelkasten.db", help="Database file path")
    parser.add_argument("--type", choices=['html', 'network', 'tags', 'all'], 
                       default='html', help="Type of visualization")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    visualizer = ZettelkastenVisualizer(args.db)
    
    try:
        if args.type == 'html' or args.type == 'all':
            output = args.output or "knowledge_graph.html"
            visualizer.generate_html_graph(output)
        
        if args.type == 'network' or args.type == 'all':
            output = args.output or "network_graph.png"
            visualizer.generate_network_graph(output)
        
        if args.type == 'tags' or args.type == 'all':
            output = args.output or "tag_hierarchy.html" 
            visualizer.generate_tag_hierarchy(output)
    
    finally:
        visualizer.close()


if __name__ == "__main__":
    main()