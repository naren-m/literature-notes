# Literature Notes - Organization Guide

> Complete guide to the reorganized structure and self-maintaining workflows

**Last Updated**: 2025-12-11

## 🎯 Overview

This repository has been comprehensively reorganized for better discoverability, maintainability, and parsing. The new structure separates notes, documentation, research, and artifacts into clear, logical domains.

## 📁 New Directory Structure

```
literature-notes/
├── INDEX.md                 # Main navigation hub (auto-generated)
│
├── CSE/                     # Computer Science & Engineering (55 notes)
│   ├── README.md            # Domain index (auto-generated)
│   ├── Cryptography/        # Security, encryption, hashing
│   ├── coding/              # Algorithms, programming
│   └── design_patterns/     # Software architecture
│
├── sanskrit-lit/            # Sanskrit Literature & Philosophy (43 notes)
│   ├── README.md            # Domain index (auto-generated)
│   ├── Concepts/            # Philosophical principles
│   └── yoga_sutras/         # Patanjali's sutras
│
├── highlights/              # Book & Article Highlights (36 notes)
│   ├── README.md            # Curated index (auto-generated)
│   ├── Books/               # Book summaries
│   └── Articles/            # Article highlights
│
├── books/                   # Book Reviews & Summaries (7 notes)
├── people/                  # Biographical Notes (9 notes)
├── pages/                   # General Concepts (28 notes)
├── Security/                # Security Concepts (2 notes)
├── Statistics/              # Statistical Methods (2 notes)
├── math/                    # Mathematical Concepts (2 notes)
├── india/                   # Indian Culture & History (3 notes)
│
├── docs/                    # Documentation & Guides
│   ├── KNOWLEDGE_FOREST_GUIDE.md
│   ├── SMART_SEARCH_SETUP.md
│   ├── DOCKER_SETUP_GUIDE.md
│   └── API_TROUBLESHOOTING.md
│
├── research/                # Research Papers
│   └── entropy-vikalpa/     # Entropy & Vikalpa research
│
├── artifacts/               # Generated Files (gitignored)
│   ├── data/                # JSON exports
│   ├── visualizations/      # HTML graphs
│   └── temp/                # Temporary files
│
└── templates/               # Note Templates
    └── NOTE_TEMPLATE.md     # YAML frontmatter guide
```

## 🔄 Self-Maintaining System

### Auto-Updating README Files (Fully Automated!)

All README files with note counts are **auto-generated via GitHub Actions**. Never manually edit the counts!

**🤖 Automatic Updates:**
- GitHub Action runs on every push to `main` branch
- Automatically executes `generate_readmes.py`
- Updates `INDEX.md` and all domain `README.md` files
- Auto-commits with descriptive message
- Skips commit if no changes detected

**What it does:**
- ✅ Counts notes in each domain
- ✅ Updates INDEX.md with current statistics
- ✅ Updates domain README files (CSE, sanskrit-lit, highlights)
- ✅ Adds last updated timestamp
- ✅ Maintains consistent formatting

**Manual trigger (if needed):**
```bash
# Only needed for local testing
python generate_readmes.py
```

**Or trigger workflow manually:**
- Go to GitHub Actions tab
- Select "Auto-Update READMEs" workflow
- Click "Run workflow"

### Adding New Notes

**1. Choose the Right Location:**
- **CSE/** - Technical, security, programming
- **sanskrit-lit/** - Vedic texts, yoga, philosophy
- **highlights/** - Book/article summaries
- **books/** - Full book reviews
- **people/** - Biographical notes
- **pages/** - General concepts that don't fit elsewhere

**2. Use the Template:**
```bash
cp templates/NOTE_TEMPLATE.md CSE/Cryptography/new-note.md
```

**3. Fill in YAML Frontmatter:**
```yaml
---
title: "Your Note Title"
date: 2025-12-11
category: "CSE/Cryptography"
tags: [tag1, tag2, tag3]
status: "draft"
---
```

**4. Update READMEs:**
```bash
python generate_readmes.py
```

### YAML Frontmatter Fields

**Required:**
- `title`: Note title (quoted if contains spaces)
- `date`: Creation date (YYYY-MM-DD)

**Recommended:**
- `category`: Domain/Subdomain (e.g., "CSE/Cryptography")
- `tags`: Array of lowercase tags [concept1, concept2]
- `status`: draft | incomplete | complete | archived

**Optional:**
- `source`: Reference if from external material
- `author`: Original author if not you
- `related`: Array of wikilinks to related notes

### Tag Guidelines

Use **lowercase, hyphenated** tags for consistency:
- ✅ `cryptography` not `Cryptography`
- ✅ `design-patterns` not `DesignPatterns`
- ✅ `yoga-sutras` not `YogaSutras`

**Common Tags by Domain:**
- **CSE**: security, cryptography, algorithms, design-patterns, authentication
- **Sanskrit-lit**: vedic, yoga, philosophy, upanishads, sutras, devotional
- **Books**: self-improvement, biography, technical, fiction
- **General**: concept, reference, practice, synthesis

## 🧹 Maintenance Workflows

### Weekly Maintenance

```bash
# 1. Update literature-notes submodule (if using in parent repo)
cd literature-notes
git pull origin main
cd ..
git add literature-notes
git commit -m "Update literature-notes"

# 2. READMEs update automatically via GitHub Action!
#    No manual action needed - they're always current

# 3. Check for broken wikilinks (optional)
python analyze_links.py
```

### Monthly Cleanup

```bash
# Remove stale artifacts
rm -rf artifacts/data/*
rm -rf artifacts/visualizations/*
rm -rf artifacts/temp/*

# Rebuild knowledge base
python zettelkasten.py build
python knowledge_forest.py build

# Verify directory structure
find . -type d -empty  # Should only show .gitignored dirs
```

## 📊 Statistics & Tracking

**Current Stats** (run `python generate_readmes.py` to update):
- **Total Notes**: 187
- **Domains**: 10
- **With Metadata**: Growing (add frontmatter to yours!)

## 🚫 What NOT to Commit

The following are gitignored:
- `artifacts/` (all generated files)
- `*.db` (zettelkasten database)
- `*.pyc`, `__pycache__/` (Python bytecode)
- `.venv/` (virtual environment)
- `*.json` at root (generated exports)

## 🔗 Integration with Digital Garden

This repository integrates with naren-m.github.io via git submodule:

**In naren-m.github.io:**
```bash
# Update to latest literature-notes
git submodule update --remote literature-notes
git commit -am "Update literature-notes submodule"
git push
```

**GitHub Actions automatically:**
1. Checks out submodule
2. Copies domains to `_notes/`
3. Excludes Python files, PDFs, etc.
4. Builds Jekyll site with wikilinks

## ❓ FAQ

**Q: Why are Module directories still there in CSE/Cryptography?**
A: They contain course materials (Python files) excluded from Jekyll build. They're archived for reference.

**Q: Can I manually edit README.md files?**
A: No! They're auto-generated by `generate_readmes.py`. Edit the script if you need changes.

**Q: Where do daily notes go?**
A: Use `daily-notes/` or `journals/` (already exist but excluded from main index).

**Q: How do I add a new domain?**
A: 1) Create directory, 2) Add notes, 3) Update `generate_readmes.py` to include it, 4) Run script.

**Q: What if I want to reorganize further?**
A: Update directory structure, then run `python generate_readmes.py` to reflect changes.

## 📚 Related Documentation

- `INDEX.md` - Main navigation hub
- `templates/NOTE_TEMPLATE.md` - YAML frontmatter guide
- `docs/KNOWLEDGE_FOREST_GUIDE.md` - Semantic navigation
- `docs/SMART_SEARCH_SETUP.md` - Natural language search

## 🎉 Benefits of New Organization

**Before Reorganization:**
- ❌ 57 files cluttering root
- ❌ Generated files mixed with notes
- ❌ Hardcoded note counts that became stale
- ❌ No index files for navigation
- ❌ Inconsistent metadata

**After Reorganization:**
- ✅ Clean root with only essential files
- ✅ Artifacts properly separated and gitignored
- ✅ Auto-updating README files
- ✅ Domain index files for discovery
- ✅ YAML frontmatter template and examples

## 🔧 Troubleshooting

**Issue: README counts don't match actual notes**
```bash
# Solution: Regenerate READMEs
python generate_readmes.py
```

**Issue: New domain not showing in INDEX.md**
```bash
# Solution: Update generate_readmes.py to include new domain
# Then run: python generate_readmes.py
```

**Issue: Wikilinks broken after reorganization**
```bash
# Check for broken links
python analyze_links.py

# Apply suggested fixes (dry-run first)
python apply_links.py --dry-run
```

---

**Maintained by**: generate_readmes.py (auto-generated READMEs)
**Last Reorganization**: 2025-12-11
**Total Notes**: 187 and growing!
