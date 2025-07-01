// Intercept clicks on .md links and render them properly
(function() {
    // Function to check if URL is a markdown file
    function isMarkdownUrl(url) {
        return url.endsWith('.md') || url.includes('.md#');
    }
    
    // Function to convert .md URL to rendered URL
    function getRenderedUrl(mdUrl) {
        // Use the markdown viewer with the file parameter
        const baseUrl = window.location.origin;
        return `${baseUrl}/markdown-viewer.html?file=${encodeURIComponent(mdUrl)}`;
    }
    
    // Intercept all link clicks
    document.addEventListener('click', function(e) {
        // Find the closest anchor tag
        let target = e.target;
        while (target && target.tagName !== 'A') {
            target = target.parentElement;
        }
        
        if (!target || !target.href) return;
        
        const href = target.getAttribute('href');
        
        // Check if it's a markdown link
        if (href && isMarkdownUrl(href)) {
            e.preventDefault();
            
            // Determine if it should open in new tab
            const shouldOpenNewTab = target.getAttribute('target') === '_blank' || 
                                   e.ctrlKey || e.metaKey || e.button === 1;
            
            // Convert to full URL if relative
            let fullUrl = href;
            if (!href.startsWith('http')) {
                if (href.startsWith('/')) {
                    fullUrl = href;
                } else {
                    // Relative to current path
                    const currentPath = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/'));
                    fullUrl = currentPath + '/' + href;
                }
            }
            
            const renderedUrl = getRenderedUrl(fullUrl);
            
            if (shouldOpenNewTab) {
                window.open(renderedUrl, '_blank');
            } else {
                window.location.href = renderedUrl;
            }
        }
    });
    
    // Also handle middle-click (mouse wheel click)
    document.addEventListener('auxclick', function(e) {
        if (e.button === 1) { // Middle click
            let target = e.target;
            while (target && target.tagName !== 'A') {
                target = target.parentElement;
            }
            
            if (target && target.href) {
                const href = target.getAttribute('href');
                if (href && isMarkdownUrl(href)) {
                    e.preventDefault();
                    
                    let fullUrl = href;
                    if (!href.startsWith('http')) {
                        if (href.startsWith('/')) {
                            fullUrl = href;
                        } else {
                            const currentPath = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/'));
                            fullUrl = currentPath + '/' + href;
                        }
                    }
                    
                    window.open(getRenderedUrl(fullUrl), '_blank');
                }
            }
        }
    });
})();