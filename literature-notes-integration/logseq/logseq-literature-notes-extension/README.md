# LogSeq Literature Notes Integration Extension

This extension integrates LogSeq with your Literature Notes system, providing seamless access to your knowledge base directly within LogSeq.

## Features

### 🔍 Smart Search Integration
- **Slash Command**: Use `/Smart Search` to search your literature notes
- **Block Context Menu**: Right-click any block and select "📚 Search Literature Notes"
- **Modal Interface**: Beautiful search modal with real-time results
- **Auto-insertion**: Click search results to insert them into your current page

### 📚 Literature Notes Access
- **Toolbar Button**: Quick access button in LogSeq toolbar
- **External Interface**: Opens your literature notes web interface
- **API Integration**: Direct connection to your Literature Notes API

### 🎯 Content Integration
- **Insert Literature Notes**: Use `/Insert Literature Note` to browse and insert notes
- **Automatic Formatting**: Notes are formatted nicely when inserted
- **Metadata Preservation**: Includes word count, tags, and source information

### ⚙️ Customizable Settings
- **API URL Configuration**: Set your Literature Notes API endpoint
- **Auto-sync Options**: Configure automatic synchronization
- **Sidebar Integration**: Optional sidebar with recent literature notes

## Installation

### Option 1: Manual Installation
1. Copy the extension folder to your LogSeq plugins directory:
   ```
   /path/to/logseq/plugins/literature-notes-integration/
   ```

2. Restart LogSeq

3. Go to Settings → Plugins and enable "Literature Notes Integration"

### Option 2: Development Mode
1. In LogSeq, go to Settings → Advanced → Developer mode
2. Enable developer mode
3. Go to Plugins → Load unpacked plugin
4. Select the extension folder

## Setup

### 1. Start Literature Notes API
Make sure your Literature Notes API is running:
```bash
# Using Docker
cd literature-notes-integration
./start.sh

# Or manually
python3 minimal_api.py
```

### 2. Configure Extension
1. Go to LogSeq Settings → Plugins → Literature Notes Integration
2. Set the API URL (default: `http://localhost:8083`)
3. Configure other preferences as needed

### 3. Test Connection
1. Click the 📚 button in the toolbar
2. Try the `/Smart Search` command
3. Check that search results appear

## Usage

### Smart Search
1. Type `/Smart Search` in any block
2. OR: Right-click any block → "📚 Search Literature Notes"
3. Enter your search query
4. Click results to insert them into your page

### Insert Literature Notes
1. Type `/Insert Literature Note`
2. Browse available notes
3. Select a note to insert its full content

### Toolbar Access
- Click the 📚 button to open the full literature notes interface
- Access your smart search, markdown viewer, and API statistics

## Configuration

### API Settings
```json
{
  "apiUrl": "http://localhost:8083",
  "autoSync": false,
  "showInSidebar": true
}
```

### Custom API Endpoints
If you're running the API on a different port or host:
1. Go to Settings → Plugins → Literature Notes Integration
2. Update the "Literature Notes API URL"
3. Restart LogSeq

## Troubleshooting

### Extension Not Loading
- Check LogSeq console for errors: View → Toggle Developer Tools
- Ensure the extension files are in the correct directory
- Restart LogSeq after installation

### API Connection Failed
- Verify the Literature Notes API is running: `curl http://localhost:8083/health`
- Check the API URL in extension settings
- Ensure there are no firewall or network restrictions

### Search Not Working
- Test API directly: `curl -X POST http://localhost:8083/smart-query -H "Content-Type: application/json" -d '{"query":"test"}'`
- Check browser console for JavaScript errors
- Verify your database has content

### No Search Results
- Ensure your zettelkasten database has content
- Try broader search terms
- Check API logs for errors

## Development

### File Structure
```
logseq-literature-notes-extension/
├── package.json          # Extension metadata
├── index.js              # Main extension code
├── README.md             # Documentation
└── icon.png              # Extension icon (optional)
```

### Key Functions
- `performSmartSearch()`: Executes literature notes search
- `openSmartSearchModal()`: Shows search interface
- `insertLiteratureNote()`: Inserts note content
- `createSidebarInterface()`: Creates sidebar integration

### API Integration
The extension communicates with these API endpoints:
- `GET /health`: Check API status
- `GET /stats`: Get database statistics
- `POST /smart-query`: Perform intelligent search
- `POST /file-content`: Get specific note content
- `GET /notes`: List recent notes

## Contributing

1. Fork the repository
2. Make your changes
3. Test with LogSeq
4. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review LogSeq console logs
3. Test API endpoints directly
4. Create an issue with detailed error information