// Auto-render markdown files when accessed directly
(function() {
    // Check if current URL ends with .md
    if (window.location.pathname.endsWith('.md')) {
        // Add marked.js and DOMPurify for markdown rendering
        const scripts = [
            'https://cdn.jsdelivr.net/npm/marked@9.1.6/marked.min.js',
            'https://cdn.jsdelivr.net/npm/dompurify@3.0.5/dist/purify.min.js',
            'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js',
            'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js'
        ];
        
        const styles = [
            'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-github.min.css'
        ];
        
        // Load styles
        styles.forEach(href => {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = href;
            document.head.appendChild(link);
        });
        
        // Load scripts sequentially
        let loadedScripts = 0;
        
        function loadNextScript() {
            if (loadedScripts < scripts.length) {
                const script = document.createElement('script');
                script.src = scripts[loadedScripts];
                script.onload = () => {
                    loadedScripts++;
                    loadNextScript();
                };
                document.head.appendChild(script);
            } else {
                // All scripts loaded, render markdown
                renderMarkdown();
            }
        }
        
        loadNextScript();
    }
    
    function renderMarkdown() {
        // Get the raw markdown content
        const rawContent = document.body.textContent || document.body.innerText;
        
        // Configure marked
        marked.setOptions({
            gfm: true,
            breaks: true,
            highlight: function(code, lang) {
                if (lang && Prism.languages[lang]) {
                    return Prism.highlight(code, Prism.languages[lang], lang);
                }
                return code;
            }
        });
        
        // Parse markdown
        const htmlContent = marked.parse(rawContent);
        const sanitizedContent = DOMPurify.sanitize(htmlContent);
        
        // Extract title from first H1 or filename
        let title = 'Literature Note';
        const h1Match = rawContent.match(/^#\s+(.+)$/m);
        if (h1Match) {
            title = h1Match[1];
        } else {
            const pathParts = window.location.pathname.split('/');
            const filename = pathParts[pathParts.length - 1].replace('.md', '');
            title = filename.charAt(0).toUpperCase() + filename.slice(1);
        }
        
        // Create a proper HTML structure
        document.documentElement.innerHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - Literature Notes</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            background-color: #ffffff;
        }
        
        /* Navigation */
        .nav-bar {
            background: #f6f8fa;
            margin: -2rem -2rem 2rem -2rem;
            padding: 1rem 2rem;
            border-bottom: 1px solid #e1e4e8;
        }
        
        .nav-bar a {
            color: #0366d6;
            text-decoration: none;
            margin-right: 1.5rem;
        }
        
        .nav-bar a:hover {
            text-decoration: underline;
        }
        
        /* GitHub-style markdown */
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        
        h1 {
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        
        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        
        h3 { font-size: 1.25em; }
        
        p { margin-bottom: 16px; }
        
        blockquote {
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin: 0 0 16px 0;
        }
        
        code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(27,31,35,0.05);
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, monospace;
        }
        
        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
            margin-bottom: 16px;
        }
        
        pre code {
            display: inline;
            padding: 0;
            margin: 0;
            background-color: transparent;
            border: 0;
        }
        
        ul, ol {
            padding-left: 2em;
            margin-bottom: 16px;
        }
        
        li { margin-bottom: 0.25em; }
        
        table {
            border-spacing: 0;
            border-collapse: collapse;
            margin-bottom: 16px;
            width: 100%;
        }
        
        table th, table td {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }
        
        table th {
            font-weight: 600;
            background-color: #f6f8fa;
        }
        
        table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }
        
        a {
            color: #0366d6;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }
        
        img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            margin: 8px 0;
        }
        
        /* Metadata */
        .note-metadata {
            background: #f6f8fa;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 1rem;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }
        
        .note-metadata span {
            margin-right: 1rem;
        }
        
        /* Edit button */
        .edit-button {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #0366d6;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            text-decoration: none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        
        .edit-button:hover {
            background: #0256c7;
            text-decoration: none;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 1rem;
            }
            
            .nav-bar {
                margin: -1rem -1rem 1rem -1rem;
                padding: 0.75rem 1rem;
            }
        }
    </style>
</head>
<body>
    <nav class="nav-bar">
        <a href="/">🏠 Home</a>
        <a href="/search/">🔍 Search</a>
        <a href="/smart-search.html">🧠 Smart Search</a>
        <a href="/graph/">🕸️ Graph</a>
        <a href="/tags/">🏷️ Tags</a>
    </nav>
    
    <div class="note-metadata">
        <span>📁 ${window.location.pathname}</span>
        <span>📝 ${rawContent.split(/\s+/).length} words</span>
    </div>
    
    <div class="markdown-content">
        ${sanitizedContent}
    </div>
    
    <a href="vscode://file${window.location.pathname}" class="edit-button">
        ✏️ Edit Note
    </a>
    
    <script>
        // Re-initialize Prism for syntax highlighting
        if (typeof Prism !== 'undefined') {
            Prism.highlightAll();
        }
        
        // Handle internal links
        document.querySelectorAll('a').forEach(link => {
            const href = link.getAttribute('href');
            if (href && href.endsWith('.md') && !href.startsWith('http')) {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    // Convert .md link to proper URL
                    const newUrl = href.startsWith('/') ? href : 
                        window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/')) + '/' + href;
                    window.location.href = newUrl;
                });
            }
        });
    </script>
</body>
</html>
        `;
        
        // Trigger syntax highlighting
        setTimeout(() => {
            if (typeof Prism !== 'undefined') {
                Prism.highlightAll();
            }
        }, 100);
    }
})();