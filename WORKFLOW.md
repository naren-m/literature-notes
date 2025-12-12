# Your Literature Notes Workflow

**Last Updated:** December 12, 2024

---

## 📝 Daily Workflow (3 Simple Steps)

### 1. Write Your Notes

**Using LogSeq:**
```
1. Open LogSeq application
2. Open "literature-notes" folder as vault
3. Write your notes (LogSeq handles everything automatically)
4. Save and close
```

**File Locations for New Notes:**

| Type | Location | Example |
|------|----------|---------|
| Computer Science | `content/domains/computer-science/` | cryptography/, coding-practices/ |
| Mathematics | `content/domains/mathematics/` | statistics/, general/ |
| Sanskrit/Philosophy | `content/domains/humanities/` | sanskrit-literature/, history/ |
| Ayurveda/Wellness | `content/domains/wellness/` | ayurveda/ |
| Books | `content/media/books/` | Book notes, summaries |
| Articles | `content/media/articles/` | Article highlights |
| Podcasts | `content/media/podcasts/` | Podcast notes |
| Videos | `content/media/videos/` | Video notes |
| People | `content/people/` | Biographical notes |
| Research | `content/research/` | Research projects |
| Daily Journal | `content/journal/` | Daily reflections |

**Note:** You can still write anywhere in the vault - LogSeq will handle it. The structure above is just for organization.

---

### 2. Commit Your Changes

```bash
cd /path/to/literature-notes

# See what changed
git status

# Add all changes
git add .

# Commit with a message
git commit -m "Add notes about [topic]"

# Or use the shorthand
git commit -am "Add notes about [topic]"
```

**Commit Message Tips:**
- Keep it short and descriptive
- Examples:
  - "Add notes on Sanskrit grammar"
  - "Update cryptography concepts"
  - "Daily journal entry Dec 12"
  - "Research notes: entropy and vikalpa"

---

### 3. Push to GitHub

```bash
git push
```

**That's it!** GitHub Actions will automatically:
- ✅ Build your digital garden (GitHub Pages)
- ✅ Update backlinks between notes
- ✅ Format markdown files
- ✅ Deploy to your public website

---

## 🤖 What Happens Automatically

### When You Push to GitHub

**1. Jekyll Build (GitHub Actions)**
- Runs on every push to `main` branch
- Builds your digital garden from `content/` directory
- Excludes technical files (Python scripts, configs, etc.)
- Generates static website

**2. README Updates (GitHub Actions)**
- Updates README files in directories
- Maintains documentation
- Keeps structure documentation current

**3. GitHub Pages Deployment**
- Your notes become a public website
- Accessible at your GitHub Pages URL
- Markdown files rendered as HTML
- Wikilinks become clickable

---

## 🔧 Behind the Scenes (You Don't Need to Touch These)

### Automatic Database Updates

Your Zettelkasten database is automatically rebuilt when you:
- Use the search functionality
- Run link analysis
- Generate knowledge forest

**Database Location:** `build/database/zettelkasten.db` (auto-generated, gitignored)

### Configuration Files

All your tool configurations are in `config/note-tools/`:
- **LogSeq:** `config/note-tools/logseq/`
- **Obsidian:** `config/note-tools/obsidian/`
- **Foam:** `config/note-tools/foam/`

**Symlinks** maintain backward compatibility:
- `logseq -> config/note-tools/logseq/`
- `.obsidian -> config/note-tools/obsidian/`
- `.foam -> config/note-tools/foam/`

---

## 📊 Optional: Advanced Operations

### Search Your Notes

```bash
# Natural language search
python smart_query.py "cryptography entropy"

# Or using new CLI
python tools/scripts/search_notes.py "sanskrit grammar"
```

### Rebuild Database Manually

```bash
# Rebuild Zettelkasten database
python zettelkasten.py build

# Or using new CLI
python tools/scripts/build_database.py --db build/database/zettelkasten.db index
```

### Generate Knowledge Forest

```bash
# Build semantic network
python build_forest.py

# Or using new CLI
python tools/scripts/build_forest.py
```

### Analyze Links

```bash
# Find missing links and suggestions
python analyze_links.py

# Or using new CLI
python tools/scripts/analyze_links.py
```

---

## 🚀 Quick Reference

### Most Common Commands

```bash
# Daily workflow
git add .
git commit -m "Your message"
git push

# Search notes
python smart_query.py "search terms"

# View statistics
python zettelkasten.py stats

# Check git status
git status

# View recent commits
git log --oneline -5
```

---

## 🛠️ Troubleshooting

### LogSeq Can't Find Configuration

**Problem:** LogSeq says configuration is missing

**Solution:**
```bash
# Check symlink exists
ls -la logseq

# Should show: logseq -> config/note-tools/logseq/

# If missing, recreate it
ln -s config/note-tools/logseq logseq
```

### GitHub Actions Failing

**Problem:** Build fails after push

**Solution:**
1. Check GitHub Actions tab in your repository
2. Look at the error logs
3. Common issues:
   - Jekyll syntax errors in markdown
   - Missing dependencies
   - Incorrect file permissions

### Search Not Working

**Problem:** Can't find notes with search

**Solution:**
```bash
# Rebuild the database
python zettelkasten.py build

# Or
python tools/scripts/build_database.py --db build/database/zettelkasten.db index
```

### Git Push Rejected

**Problem:** `git push` says "rejected"

**Solution:**
```bash
# Pull remote changes first
git pull --rebase

# Then push
git push
```

---

## 📍 File Locations Quick Reference

| Item | Location |
|------|----------|
| Your Notes | `content/` (hierarchical by domain) |
| Database | `build/database/zettelkasten.db` (auto-generated) |
| LogSeq Config | `config/note-tools/logseq/` (symlinked from `logseq/`) |
| Python Tools | `tools/` (you don't need to touch these) |
| Build Artifacts | `build/` (auto-generated, gitignored) |
| GitHub Actions | `.github/workflows/` |
| Jekyll Config | `_config.yml` |

---

## 🎯 Your Workflow Summary

### Simple Version (What You Do)
1. **Write** notes in LogSeq
2. **Commit** changes: `git commit -am "message"`
3. **Push** to GitHub: `git push`
4. **Done!** Everything else is automatic

### What Happens Automatically
- ✅ Database updates
- ✅ Digital garden builds
- ✅ Backlinks updated
- ✅ Website deployed
- ✅ Search indices generated

### What You Never Need to Do
- ❌ Run build scripts manually
- ❌ Update configurations
- ❌ Regenerate database
- ❌ Deploy website manually
- ❌ Fix backlinks manually

---

## 🎁 Bonus: Best Practices

### Commit Frequency
- **Daily:** Best for journal entries and regular note-taking
- **After major updates:** When you finish a research session
- **Before changing devices:** Sync before switching machines

### Note Organization
- Use the hierarchical `content/` structure for better organization
- Tag your notes liberally (LogSeq handles this automatically)
- Use wikilinks `[[Note Title]]` to connect ideas
- Create index notes for major topics

### Backup Strategy
- GitHub is your primary backup (every push creates a backup)
- Consider periodic local backups of `content/` directory
- Git history preserves all changes (you can always rollback)

---

**Questions?** Check:
- `CLAUDE.md` - Full project documentation
- `MIGRATION_COMPLETE.md` - Migration details
- GitHub Actions logs - Build/deployment status

**Your workflow is now simpler and more powerful than ever!** 🚀
