/**
 * LogSeq Plugin for Literature Notes Integration
 * Provides smart query and synthesis capabilities within LogSeq
 */

// Plugin manifest (for package.json)
const PLUGIN_MANIFEST = {
  "name": "literature-notes-integration",
  "version": "1.0.0", 
  "description": "Smart query and knowledge synthesis for literature notes",
  "main": "index.js",
  "logseq": {
    "id": "literature-notes-integration",
    "title": "Literature Notes Integration",
    "icon": "🧠"
  }
};

// Plugin configuration
const CONFIG = {
  smartQueryEndpoint: 'http://localhost:8000/smart-query',
  synthesisEndpoint: 'http://localhost:8000/synthesis',
  autoSyncInterval: 24 * 60 * 60 * 1000, // 24 hours
};

// Main plugin class
class LiteratureNotesPlugin {
  constructor() {
    this.isInitialized = false;
  }

  // Initialize the plugin
  async init() {
    console.log('📚 Literature Notes Integration Plugin Loading...');
    
    // Register slash commands
    this.registerSlashCommands();
    
    // Register UI components
    this.registerUIComponents();
    
    // Set up auto-sync
    this.setupAutoSync();
    
    // Add plugin to toolbar
    this.addToolbarButton();
    
    this.isInitialized = true;
    console.log('✅ Literature Notes Integration Plugin Ready!');
  }

  // Register slash commands for quick access
  registerSlashCommands() {
    // Smart query command
    logseq.Editor.registerSlashCommand('smart-query', async () => {
      const query = await logseq.UI.showInputDialog('Enter your smart query:', {
        placeholder: 'e.g., connections between ayurveda and programming'
      });
      
      if (query) {
        await this.executeSmartQuery(query);
      }
    });

    // Daily synthesis command  
    logseq.Editor.registerSlashCommand('daily-synthesis', async () => {
      await this.generateDailySynthesis();
    });

    // Domain summary command
    logseq.Editor.registerSlashCommand('domain-summary', async () => {
      const domain = await logseq.UI.showInputDialog('Enter domain to summarize:', {
        placeholder: 'e.g., sanskrit, programming, cryptography'
      });
      
      if (domain) {
        await this.generateDomainSummary(domain);
      }
    });

    // Cross-domain insights command
    logseq.Editor.registerSlashCommand('cross-domain', async () => {
      const domains = await logseq.UI.showInputDialog('Enter two domains (comma-separated):', {
        placeholder: 'e.g., sanskrit, programming'
      });
      
      if (domains && domains.includes(',')) {
        const [domain1, domain2] = domains.split(',').map(d => d.trim());
        await this.findCrossDomainInsights(domain1, domain2);
      }
    });
  }

  // Register UI components
  registerUIComponents() {
    // Knowledge graph panel
    logseq.App.registerUIItem('toolbar', {
      key: 'literature-notes-graph',
      template: `
        <div class="literature-notes-panel">
          <button class="button" data-on-click="showKnowledgeGraph">
            🕸️ Knowledge Graph
          </button>
        </div>
      `
    });

    // Smart search panel
    logseq.App.registerUIItem('right-sidebar', {
      key: 'smart-search-panel',
      template: `
        <div class="smart-search-container">
          <h3>🧠 Smart Search</h3>
          <input type="text" id="smart-search-input" placeholder="Natural language query...">
          <button data-on-click="executeSearch">Search</button>
          <div id="search-results"></div>
        </div>
      `
    });
  }

  // Execute smart query
  async executeSmartQuery(query) {
    try {
      logseq.UI.showMsg('🔍 Executing smart query...', 'info');
      
      // Call Python backend (in real implementation, this would be a proper API call)
      const results = await this.callPythonBackend('smart_query.py', [query]);
      
      // Create a new page with results
      const timestamp = new Date().toISOString().split('T')[0];
      const pageName = `Smart Query - ${query.substring(0, 30)} - ${timestamp}`;
      
      let content = `# Smart Query Results\n\n**Query**: ${query}\n**Timestamp**: ${new Date().toLocaleString()}\n\n`;
      
      if (results && results.length > 0) {
        content += `## Results (${results.length} found)\n\n`;
        
        results.forEach((result, index) => {
          content += `### ${index + 1}. [[${result.title}]]\n`;
          if (result.tags) {
            content += `**Tags**: ${result.tags.map(tag => `#${tag}`).join(', ')}\n`;
          }
          if (result.relevance_score) {
            content += `**Relevance**: ${result.relevance_score}\n`;
          }
          content += `**Preview**: ${result.content?.substring(0, 150)}...\n\n`;
        });
        
        // Add synthesis if connections found
        if (query.toLowerCase().includes('connection')) {
          content += this.generateConnectionSynthesis(results);
        }
        
      } else {
        content += 'No results found. Try different keywords or phrases.\n';
      }
      
      // Create the page
      await logseq.Editor.createPage(pageName, content, {
        createFirstBlock: false,
        properties: {
          type: 'smart-query',
          query: query,
          timestamp: new Date().toISOString()
        }
      });
      
      // Navigate to the page
      await logseq.App.pushState('page', { name: pageName });
      
      logseq.UI.showMsg('✅ Smart query results created!', 'success');
      
    } catch (error) {
      console.error('Smart query error:', error);
      logseq.UI.showMsg('❌ Smart query failed. Check console for details.', 'error');
    }
  }

  // Generate daily synthesis
  async generateDailySynthesis() {
    try {
      logseq.UI.showMsg('🧠 Generating daily synthesis...', 'info');
      
      const synthesis = await this.callPythonBackend('knowledge_synthesis.py', ['daily']);
      
      // Get today's journal page
      const today = new Date();
      const journalPage = today.toISOString().split('T')[0];
      
      // Add synthesis to journal
      let synthesisContent = '\n## 🧠 Knowledge Synthesis\n*Auto-generated insights*\n\n';
      
      if (synthesis.groups) {
        synthesis.groups.forEach((group, index) => {
          synthesisContent += `### Cluster ${index + 1}: ${group.theme}\n`;
          synthesisContent += '- **Connected Notes**:\n';
          group.notes.forEach(note => {
            synthesisContent += `  - [[${note.title}]]\n`;
          });
          
          if (group.connections && group.connections.length > 0) {
            synthesisContent += '- **Knowledge Flow**:\n';
            group.connections.forEach(conn => {
              synthesisContent += `  - [[${conn.from}]] → [[${conn.to}]]\n`;
            });
          }
          synthesisContent += '\n';
        });
      }
      
      if (synthesis.insights) {
        synthesisContent += '## 💡 Insights\n';
        synthesis.insights.forEach(insight => {
          synthesisContent += `- ${insight}\n`;
        });
        synthesisContent += '\n';
      }
      
      if (synthesis.suggested_explorations) {
        synthesisContent += '## 🎯 Explore Next\n';
        synthesis.suggested_explorations.forEach(suggestion => {
          synthesisContent += `- ${suggestion}\n`;
        });
      }
      
      // Append to journal page
      await logseq.Editor.appendBlockInPage(journalPage, synthesisContent);
      
      // Navigate to journal
      await logseq.App.pushState('page', { name: journalPage });
      
      logseq.UI.showMsg('✅ Daily synthesis added to journal!', 'success');
      
    } catch (error) {
      console.error('Synthesis error:', error);
      logseq.UI.showMsg('❌ Daily synthesis failed. Check console for details.', 'error');
    }
  }

  // Generate domain summary
  async generateDomainSummary(domain) {
    try {
      logseq.UI.showMsg(`📊 Analyzing ${domain} domain...`, 'info');
      
      const summary = await this.callPythonBackend('knowledge_synthesis.py', ['domain', domain]);
      
      const pageName = `Domain Summary - ${domain}`;
      
      let content = `# ${domain} Domain Summary\n\n`;
      content += `**Generated**: ${new Date().toLocaleString()}\n`;
      content += `**Notes**: ${summary.note_count || 0}\n`;
      content += `**Total Words**: ${summary.total_words || 0}\n\n`;
      
      if (summary.key_concepts) {
        content += '## Key Concepts\n';
        summary.key_concepts.slice(0, 10).forEach(([concept, freq]) => {
          content += `- **${concept}** (${freq} occurrences)\n`;
        });
        content += '\n';
      }
      
      if (summary.main_topics) {
        content += '## Main Topics\n';
        summary.main_topics.forEach(topic => {
          content += `- #${topic}\n`;
        });
        content += '\n';
      }
      
      if (summary.top_notes) {
        content += '## Top Notes\n';
        summary.top_notes.forEach(note => {
          content += `- [[${note.title}]]\n`;
        });
      }
      
      await logseq.Editor.createPage(pageName, content, {
        properties: {
          type: 'domain-summary',
          domain: domain,
          timestamp: new Date().toISOString()
        }
      });
      
      await logseq.App.pushState('page', { name: pageName });
      
      logseq.UI.showMsg(`✅ ${domain} domain summary created!`, 'success');
      
    } catch (error) {
      console.error('Domain summary error:', error);
      logseq.UI.showMsg('❌ Domain summary failed. Check console for details.', 'error');
    }
  }

  // Find cross-domain insights
  async findCrossDomainInsights(domain1, domain2) {
    try {
      logseq.UI.showMsg(`🔗 Finding connections: ${domain1} ↔ ${domain2}...`, 'info');
      
      const insights = await this.callPythonBackend('knowledge_synthesis.py', ['connect', domain1, domain2]);
      
      const pageName = `Cross-Domain Insights - ${domain1} & ${domain2}`;
      
      let content = `# Cross-Domain Insights: ${domain1} ↔ ${domain2}\n\n`;
      content += `**Generated**: ${new Date().toLocaleString()}\n\n`;
      
      if (insights.bridge_notes && insights.bridge_notes.length > 0) {
        content += '## Bridge Notes\n';
        insights.bridge_notes.forEach(note => {
          content += `- [[${note.title}]]\n`;
        });
        content += '\n';
      }
      
      if (insights.shared_concepts && insights.shared_concepts.length > 0) {
        content += '## Shared Concepts\n';
        insights.shared_concepts.forEach(concept => {
          content += `- **${concept}**\n`;
        });
        content += '\n';
      }
      
      if (insights.synthesis) {
        content += `## Synthesis\n${insights.synthesis}\n\n`;
      }
      
      if (insights.potential_connections && insights.potential_connections.length > 0) {
        content += '## Potential Connections\n';
        insights.potential_connections.forEach(connection => {
          content += `- ${connection}\n`;
        });
      }
      
      await logseq.Editor.createPage(pageName, content, {
        properties: {
          type: 'cross-domain-insights',
          domain1: domain1,
          domain2: domain2,
          timestamp: new Date().toISOString()
        }
      });
      
      await logseq.App.pushState('page', { name: pageName });
      
      logseq.UI.showMsg('✅ Cross-domain insights created!', 'success');
      
    } catch (error) {
      console.error('Cross-domain insights error:', error);
      logseq.UI.showMsg('❌ Cross-domain analysis failed. Check console for details.', 'error');
    }
  }

  // Generate connection synthesis for query results
  generateConnectionSynthesis(results) {
    let synthesis = '\n## 🔗 Connection Analysis\n\n';
    
    if (results.length > 1) {
      synthesis += `Found ${results.length} notes that bridge these concepts. `;
      synthesis += 'This suggests an interdisciplinary understanding that could lead to new insights.\n\n';
      
      // Extract common themes
      const allTags = results.flatMap(r => r.tags || []);
      const tagCounts = {};
      allTags.forEach(tag => {
        tagCounts[tag] = (tagCounts[tag] || 0) + 1;
      });
      
      const commonTags = Object.entries(tagCounts)
        .filter(([tag, count]) => count > 1)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
      
      if (commonTags.length > 0) {
        synthesis += '**Common Themes**:\n';
        commonTags.forEach(([tag, count]) => {
          synthesis += `- #${tag} (appears in ${count} notes)\n`;
        });
      }
    }
    
    return synthesis;
  }

  // Setup auto-sync for daily synthesis
  setupAutoSync() {
    if (CONFIG.autoSyncInterval > 0) {
      setInterval(async () => {
        try {
          await this.generateDailySynthesis();
          console.log('✅ Auto-sync: Daily synthesis completed');
        } catch (error) {
          console.error('Auto-sync error:', error);
        }
      }, CONFIG.autoSyncInterval);
    }
  }

  // Add toolbar button for quick access
  addToolbarButton() {
    logseq.App.registerUIItem('toolbar', {
      key: 'literature-notes-btn',
      template: `
        <button class="button" data-on-click="showQuickMenu" title="Literature Notes Integration">
          🧠
        </button>
      `
    });
  }

  // Show quick access menu
  async showQuickMenu() {
    const options = [
      { label: '🔍 Smart Query', value: 'smart-query' },
      { label: '🧠 Daily Synthesis', value: 'daily-synthesis' },
      { label: '📊 Domain Summary', value: 'domain-summary' },
      { label: '🔗 Cross-Domain Insights', value: 'cross-domain' },
      { label: '🕸️ Knowledge Graph', value: 'knowledge-graph' }
    ];
    
    const choice = await logseq.UI.showSelectList(options, 'Choose an action:');
    
    switch (choice) {
      case 'smart-query':
        const query = await logseq.UI.showInputDialog('Enter your smart query:');
        if (query) await this.executeSmartQuery(query);
        break;
      case 'daily-synthesis':
        await this.generateDailySynthesis();
        break;
      case 'domain-summary':
        const domain = await logseq.UI.showInputDialog('Enter domain:');
        if (domain) await this.generateDomainSummary(domain);
        break;
      case 'cross-domain':
        const domains = await logseq.UI.showInputDialog('Enter two domains (comma-separated):');
        if (domains && domains.includes(',')) {
          const [d1, d2] = domains.split(',').map(d => d.trim());
          await this.findCrossDomainInsights(d1, d2);
        }
        break;
      case 'knowledge-graph':
        await logseq.App.pushState('page', { name: 'Knowledge Graph' });
        break;
    }
  }

  // Call Python backend (simplified - in production would use proper API)
  async callPythonBackend(script, args) {
    // This is a simplified version - in production, you'd set up a proper API server
    // For now, this returns mock data structure
    
    if (script === 'smart_query.py') {
      // Mock smart query results
      return [
        {
          title: 'Sample Note 1',
          tags: ['programming', 'philosophy'],
          content: 'This is sample content from a note...',
          relevance_score: 95
        },
        {
          title: 'Sample Note 2', 
          tags: ['sanskrit', 'consciousness'],
          content: 'Another sample note with different content...',
          relevance_score: 87
        }
      ];
    }
    
    if (script === 'knowledge_synthesis.py' && args[0] === 'daily') {
      return {
        groups: [
          {
            theme: 'Programming Concepts',
            notes: [
              { title: 'Algorithms' },
              { title: 'Data Structures' }
            ],
            connections: [
              { from: 'Algorithms', to: 'Data Structures' }
            ]
          }
        ],
        insights: ['You have strong connections between programming concepts'],
        suggested_explorations: ['Explore connections to philosophy']
      };
    }
    
    // Return empty result for other cases
    return {};
  }
}

// Plugin initialization
function main() {
  const plugin = new LiteratureNotesPlugin();
  
  logseq.ready(() => {
    plugin.init();
  });
  
  // Export for LogSeq
  return plugin;
}

// LogSeq plugin entry point
if (typeof logseq !== 'undefined') {
  main();
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LiteratureNotesPlugin, PLUGIN_MANIFEST };
}