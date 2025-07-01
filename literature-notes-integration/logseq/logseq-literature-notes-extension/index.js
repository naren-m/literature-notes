/**
 * LogSeq Literature Notes Integration Extension
 * Connects LogSeq with your Literature Notes system for enhanced knowledge management
 */

const API_BASE_URL = 'http://localhost:8083';

async function main() {
  console.log('📚 Literature Notes Extension: Starting...');

  // Register main menu item
  logseq.App.registerUIItem('toolbar', {
    key: 'literature-notes',
    template: `
      <a class="button" data-on-click="openLiteratureNotes" title="Literature Notes Integration">
        <i class="ti ti-books"></i>
      </a>
    `,
  });

  // Register search command
  logseq.Editor.registerSlashCommand('Smart Search', async () => {
    const query = await logseq.Editor.getEditingCursorPosition();
    if (query) {
      openSmartSearchModal();
    }
  });

  // Register block command for literature notes
  logseq.Editor.registerBlockContextMenuItem('📚 Search Literature Notes', async ({ uuid }) => {
    const block = await logseq.Editor.getBlock(uuid);
    if (block) {
      const content = block.content;
      performSmartSearch(content);
    }
  });

  // Register page command
  logseq.Editor.registerSlashCommand('Insert Literature Note', async () => {
    openNotePicker();
  });

  // Register settings
  logseq.useSettingsSchema([
    {
      key: 'apiUrl',
      type: 'string',
      title: 'Literature Notes API URL',
      description: 'URL of your Literature Notes API server',
      default: 'http://localhost:8083'
    },
    {
      key: 'autoSync',
      type: 'boolean',
      title: 'Auto-sync with Literature Notes',
      description: 'Automatically sync notes between LogSeq and Literature Notes',
      default: false
    },
    {
      key: 'showInSidebar',
      type: 'boolean',
      title: 'Show Literature Notes in Sidebar',
      description: 'Display literature notes integration in the sidebar',
      default: true
    }
  ]);

  // Register event handlers
  logseq.provideModel({
    openLiteratureNotes() {
      openMainInterface();
    },
    
    async performSmartSearch(query) {
      return performSmartSearch(query);
    },
    
    async insertLiteratureNote(noteId) {
      return insertLiteratureNote(noteId);
    }
  });

  // Initialize sidebar if enabled
  const settings = logseq.settings;
  if (settings?.showInSidebar) {
    createSidebarInterface();
  }

  console.log('📚 Literature Notes Extension: Loaded successfully!');
}

/**
 * Open the main Literature Notes interface
 */
function openMainInterface() {
  const url = `${getApiUrl()}/smart-search.html`;
  logseq.App.openExternalLink(url);
}

/**
 * Open smart search modal
 */
function openSmartSearchModal() {
  logseq.provideUI({
    key: 'literature-search-modal',
    path: '#literature-search-modal',
    template: `
      <div class="literature-search-modal">
        <div class="modal-overlay" data-on-click="closeModal">
          <div class="modal-content" data-on-click="stopPropagation">
            <div class="modal-header">
              <h3>📚 Smart Literature Search</h3>
              <button class="close-btn" data-on-click="closeModal">×</button>
            </div>
            <div class="modal-body">
              <input 
                type="text" 
                id="search-input" 
                placeholder="Search your literature notes..."
                data-on-keyup="handleSearchKeyup"
              />
              <div id="search-results" class="search-results">
                <p>Start typing to search your literature notes...</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    `,
    style: {
      key: 'literature-search-style',
      style: `
        .literature-search-modal {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          z-index: 999;
        }
        
        .modal-overlay {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.5);
          display: flex;
          align-items: center;
          justify-content: center;
        }
        
        .modal-content {
          background: var(--ls-primary-background-color);
          border-radius: 8px;
          width: 90%;
          max-width: 600px;
          max-height: 80vh;
          overflow: hidden;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        .modal-header {
          padding: 1rem;
          border-bottom: 1px solid var(--ls-border-color);
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        
        .modal-body {
          padding: 1rem;
        }
        
        #search-input {
          width: 100%;
          padding: 0.75rem;
          border: 1px solid var(--ls-border-color);
          border-radius: 4px;
          font-size: 1rem;
          margin-bottom: 1rem;
        }
        
        .search-results {
          max-height: 300px;
          overflow-y: auto;
        }
        
        .search-result-item {
          padding: 0.75rem;
          border: 1px solid var(--ls-border-color);
          border-radius: 4px;
          margin-bottom: 0.5rem;
          cursor: pointer;
          transition: background-color 0.2s;
        }
        
        .search-result-item:hover {
          background-color: var(--ls-secondary-background-color);
        }
        
        .result-title {
          font-weight: bold;
          margin-bottom: 0.25rem;
        }
        
        .result-content {
          font-size: 0.9rem;
          color: var(--ls-secondary-text-color);
        }
        
        .close-btn {
          background: none;
          border: none;
          font-size: 1.5rem;
          cursor: pointer;
          color: var(--ls-primary-text-color);
        }
      `
    }
  });

  // Add event handlers
  logseq.provideModel({
    closeModal() {
      logseq.hideMainUI({ restoreEditingCursor: true });
    },
    
    stopPropagation(e) {
      e.stopPropagation();
    },
    
    async handleSearchKeyup(e) {
      if (e.key === 'Enter') {
        const query = e.target.value;
        if (query.trim()) {
          await performSearchInModal(query);
        }
      }
    },
    
    async insertSearchResult(title, content) {
      await logseq.Editor.insertAtEditingCursor(`
[[Literature Note: ${title}]]

${content}

Source: Literature Notes System
      `);
      logseq.hideMainUI({ restoreEditingCursor: true });
    }
  });

  logseq.showMainUI();
}

/**
 * Perform smart search and display results in modal
 */
async function performSearchInModal(query) {
  try {
    const response = await fetch(`${getApiUrl()}/smart-query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });

    if (!response.ok) {
      throw new Error('Search failed');
    }

    const data = await response.json();
    displaySearchResults(data.results);

  } catch (error) {
    console.error('Search error:', error);
    const resultsDiv = document.getElementById('search-results');
    if (resultsDiv) {
      resultsDiv.innerHTML = '<p style="color: red;">Search failed. Make sure the Literature Notes API is running.</p>';
    }
  }
}

/**
 * Display search results in the modal
 */
function displaySearchResults(results) {
  const resultsDiv = document.getElementById('search-results');
  if (!resultsDiv) return;

  if (results.length === 0) {
    resultsDiv.innerHTML = '<p>No results found.</p>';
    return;
  }

  const html = results.map((result, index) => `
    <div class="search-result-item" data-on-click="insertSearchResult" data-title="${result.title}" data-content="${result.content.substring(0, 200)}...">
      <div class="result-title">${result.title}</div>
      <div class="result-content">${result.content.substring(0, 150)}...</div>
      <small>Relevance: ${result.relevance_score || 'N/A'} | Words: ${result.word_count || 'N/A'}</small>
    </div>
  `).join('');

  resultsDiv.innerHTML = html;
}

/**
 * Perform smart search and show results
 */
async function performSmartSearch(query) {
  try {
    const response = await fetch(`${getApiUrl()}/smart-query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });

    if (!response.ok) {
      throw new Error('Search failed');
    }

    const data = await response.json();
    
    if (data.results && data.results.length > 0) {
      // Create a new page with search results
      const pageName = `Literature Search: ${query}`;
      const content = `# Literature Search Results for "${query}"

Found ${data.results.length} relevant notes:

${data.results.map((result, index) => `
## ${index + 1}. [[${result.title}]]

${result.content.substring(0, 300)}...

**Relevance Score:** ${result.relevance_score}  
**Word Count:** ${result.word_count}  
**Tags:** ${result.tags || 'None'}

---
`).join('')}

Generated by Literature Notes Integration at ${new Date().toISOString()}
`;

      await logseq.Editor.createPage(pageName, content, { redirect: true });
    } else {
      logseq.App.showMsg('No results found for your search.', 'warning');
    }

  } catch (error) {
    console.error('Search error:', error);
    logseq.App.showMsg('Search failed. Make sure the Literature Notes API is running.', 'error');
  }
}

/**
 * Open note picker
 */
function openNotePicker() {
  // This would open a interface to browse and select literature notes
  logseq.App.showMsg('Note picker coming soon!', 'info');
}

/**
 * Insert a literature note into current position
 */
async function insertLiteratureNote(noteId) {
  try {
    const response = await fetch(`${getApiUrl()}/file-content`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path: noteId })
    });

    if (!response.ok) {
      throw new Error('Failed to fetch note');
    }

    const note = await response.json();
    
    const content = `
## Literature Note: ${note.title}

${note.content}

**Source:** Literature Notes System  
**Word Count:** ${note.word_count}  
**Tags:** ${note.tags || 'None'}  
**Path:** ${note.path}
`;

    await logseq.Editor.insertAtEditingCursor(content);
    logseq.App.showMsg(`Inserted literature note: ${note.title}`, 'success');

  } catch (error) {
    console.error('Insert note error:', error);
    logseq.App.showMsg('Failed to insert literature note.', 'error');
  }
}

/**
 * Create sidebar interface
 */
function createSidebarInterface() {
  logseq.App.registerUIItem('pagebar', {
    key: 'literature-notes-sidebar',
    template: `
      <div class="literature-notes-sidebar">
        <h4>📚 Literature Notes</h4>
        <button data-on-click="openSmartSearch" class="btn">Smart Search</button>
        <button data-on-click="openMainInterface" class="btn">Open Interface</button>
        <div id="recent-literature-notes">
          <h5>Recent Literature Notes</h5>
          <p>Loading...</p>
        </div>
      </div>
    `,
  });

  // Load recent notes
  loadRecentNotes();
}

/**
 * Load recent literature notes
 */
async function loadRecentNotes() {
  try {
    const response = await fetch(`${getApiUrl()}/notes`);
    if (!response.ok) {
      throw new Error('Failed to fetch notes');
    }

    const data = await response.json();
    const recentDiv = document.getElementById('recent-literature-notes');
    
    if (recentDiv && data.notes) {
      const html = `
        <h5>Recent Literature Notes</h5>
        ${data.notes.slice(0, 5).map(note => `
          <div class="recent-note" data-on-click="insertLiteratureNote" data-note-id="${note.path}">
            <strong>${note.title}</strong><br>
            <small>${note.word_count} words</small>
          </div>
        `).join('')}
      `;
      recentDiv.innerHTML = html;
    }

  } catch (error) {
    console.error('Load recent notes error:', error);
    const recentDiv = document.getElementById('recent-literature-notes');
    if (recentDiv) {
      recentDiv.innerHTML = '<p>Unable to load recent notes</p>';
    }
  }
}

/**
 * Get API URL from settings
 */
function getApiUrl() {
  const settings = logseq.settings;
  return settings?.apiUrl || API_BASE_URL;
}

// Initialize the extension
logseq.ready(() => {
  main().catch(console.error);
});