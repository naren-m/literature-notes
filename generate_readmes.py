#!/usr/bin/env python3
"""
Generate/update README files with dynamic note counts and statistics.
Run this script whenever you want to update domain README files.

Usage:
    python generate_readmes.py
"""

from pathlib import Path
from collections import defaultdict
import re
from datetime import datetime

# Exclude these directories from note counting
EXCLUDE_DIRS = {
    '.git', '.obsidian', '.venv', '__pycache__', 'logseq', 'graph',
    'api', 'journals', 'daily-notes', 'video', 'podcast', '_layouts',
    '.foam', '.github', 'docs', 'research', 'artifacts', 'templates'
}

def count_notes(base_path):
    """Count markdown notes in each domain, excluding system directories."""
    domain_counts = defaultdict(int)
    all_notes = []

    base = Path(base_path)
    for md_file in base.rglob("*.md"):
        # Skip README files
        if md_file.name == "README.md":
            continue

        # Skip excluded directories
        if any(ex in md_file.parts for ex in EXCLUDE_DIRS):
            continue

        # Get relative path from base
        try:
            rel_path = md_file.relative_to(base)
            parts = rel_path.parts

            # Get domain (first directory in relative path)
            if len(parts) > 1:
                domain = parts[0]
                domain_counts[domain] += 1
                all_notes.append(md_file)
        except ValueError:
            # File is not relative to base, skip it
            continue

    return domain_counts, all_notes

def get_note_titles(directory):
    """Extract note titles from markdown files in directory."""
    titles = []
    for md_file in Path(directory).glob("*.md"):
        if md_file.name == "README.md":
            continue
        # Try to extract title from front matter or filename
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check for YAML front matter title
            if content.startswith('---'):
                match = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', content)
                if match:
                    titles.append(match.group(1))
                    continue
            # Fall back to first heading or filename
            heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if heading_match:
                titles.append(heading_match.group(1))
            else:
                titles.append(md_file.stem.replace('-', ' ').replace('_', ' ').title())
    return sorted(titles)

def generate_main_index(domain_counts, total_notes):
    """Generate main INDEX.md with current statistics."""
    template = f"""# Literature Notes - Complete Index

> A comprehensive Zettelkasten knowledge management system covering computer science, Sanskrit literature, book highlights, and more.

## 🗺️ Quick Navigation

### Main Domains

- **[[CSE/README|Computer Science & Engineering]]** - Cryptography, algorithms, design patterns ({domain_counts.get('CSE', 0)} notes)
- **[[sanskrit-lit/README|Sanskrit Literature]]** - Vedic texts, philosophy, yoga sutras ({domain_counts.get('sanskrit-lit', 0)} notes)
- **[[highlights/README|Highlights]]** - Curated book & article summaries ({domain_counts.get('highlights', 0)} notes)
- **[[books/README|Books]]** - Book reviews and summaries ({domain_counts.get('books', 0)} notes)
- **[[people/README|People]]** - Notable figures & biographies ({domain_counts.get('people', 0)} notes)

### Specialized Areas

- **[[Security]]** - Security concepts and vulnerabilities ({domain_counts.get('Security', 0)} notes)
- **[[Statistics]]** - Statistical methods and concepts ({domain_counts.get('Statistics', 0)} notes)
- **[[math]]** - Mathematical concepts ({domain_counts.get('math', 0)} notes)
- **[[india]]** - Indian culture and history ({domain_counts.get('india', 0)} notes)

## 📊 Browse by Topic

### Computer Science
- [[Cryptography]] - Encryption, hashing, algorithms
- [[Design Patterns]] - Software architecture patterns
- [[Token Authentication]] - Authentication systems
- [[Zero Day Attack]] - Security vulnerabilities

### Sanskrit & Philosophy
- [[Yogasutras]] - Patanjali's Yoga Sutras
- [[Krishna]] - Jagath Guru teachings
- [[Dharma]] - Universal principles
- [[Karma]] - Action and consequence
- [[Upanishads]] - Vedic philosophy

### Book Highlights
- [[Atomic Habits]] - James Clear
- Books by various authors in highlights/Books/

## 🔍 Documentation & Guides

- [[docs/KNOWLEDGE_FOREST_GUIDE|Knowledge Forest Guide]] - Navigate the semantic network
- [[docs/SMART_SEARCH_SETUP|Smart Search]] - Natural language search setup
- [[docs/DOCKER_SETUP_GUIDE|Docker Setup]] - Containerized development
- [[docs/API_TROUBLESHOOTING|API Troubleshooting]] - Fix common issues

## 📁 Project Structure

```
literature-notes/
├── CSE/                # Computer Science & Engineering
├── sanskrit-lit/       # Sanskrit texts & philosophy
├── highlights/         # Book & article highlights
├── books/             # Book reviews & summaries
├── people/            # Biographical notes
├── pages/             # General notes & concepts
├── docs/              # Documentation & guides
├── research/          # Research papers
└── artifacts/         # Generated files (gitignored)
```

## 🏷️ Common Tags

`#security` `#cryptography` `#philosophy` `#yoga` `#sanskrit` `#design-patterns` `#algorithms` `#authentication` `#vedic` `#upanishads`

## 🔗 Cross-Domain Connections

This knowledge base emphasizes interconnections across domains:

- **Entropy & Vikalpa** - Connections between information theory and Vedic philosophy
- **Design Patterns & Dharma** - Universal patterns in code and life
- **Cryptography & Ancient Wisdom** - Security principles across time

## 🚀 Getting Started

1. **New to the system?** Start with [[docs/KNOWLEDGE_FOREST_GUIDE]]
2. **Looking for specific topics?** Browse domain README files above
3. **Want to search?** Use [[docs/SMART_SEARCH_SETUP]] for natural language queries
4. **Adding notes?** Follow the YAML frontmatter template

## 📈 Statistics

- **Total Notes**: {total_notes}
- **Domains**: {len([d for d in domain_counts if domain_counts[d] > 0])} major areas
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 🔄 Maintenance

This index is auto-generated. To update with current note counts:

```bash
python generate_readmes.py
```

---

*This is a living document. The knowledge graph evolves continuously through new notes and connections.*
"""
    return template

def generate_cse_readme(cse_count, crypto_count):
    """Generate CSE/README.md with current counts."""
    template = f"""# Computer Science & Engineering

> Technical notes covering cryptography, security, algorithms, design patterns, and software engineering concepts.

## 📚 Overview

This domain contains **{cse_count} notes** across three main areas:
- **Cryptography** - Security, encryption, hashing (~{crypto_count} notes)
- **Coding** - Algorithms and programming concepts
- **Design Patterns** - Software architecture patterns

## 🔐 Cryptography

### Core Concepts
- [[Cryptography/Cryptography]] - Overview and fundamentals
- [[Cryptography/Hashing]] - Hash functions and algorithms
- [[Cryptography/Block Cipher]] - Block cipher encryption
- [[Cryptography/Public Key]] - Asymmetric cryptography
- [[Cryptography/Digital signatures]] - Authentication and integrity

### Security Principles
- [[Cryptography/CIA Triad]] - Confidentiality, Integrity, Availability
  - [[Cryptography/Confidentiality]] - Keeping secrets
  - [[Cryptography/Integrity]] - Data trustworthiness
  - [[Cryptography/Availability]] - Resource accessibility

### Threat Models & Attacks
- [[Cryptography/STRIDE]] - Threat categorization framework
  - Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- [[Cryptography/Zero Day Attack]] - Unknown vulnerabilities
- [[Cryptography/Side Channel Attack]] - Non-traditional attack vectors
- [[Cryptography/Buffer Overflows]] - Memory exploitation
- [[Cryptography/Cold Boot]] - RAM-based attacks
- [[Cryptography/DLL Preloading Attack]] - Library hijacking

### Algorithms & Methods
- [[Cryptography/Hash Algorithms]] - SHA, MD5, etc.
- [[Cryptography/Checksum]] - Data integrity verification
- [[Cryptography/ENTROPY]] - Randomness and information theory
- [[Cryptography/Cache prefetching]] - Performance optimization

### Authentication & Authorization
- [[Cryptography/Token Authentication]] - Session management
- [[Cryptography/Zero-Trust]] - Security architecture
- [[Cryptography/Data Sensitivity]] - Classification and handling

### Standards & Formats
- [[Cryptography/JSON]] - Data interchange format
- [[Cryptography/ECC memory]] - Error-correcting code

## 💻 Coding & Algorithms

- [[coding/Coding]] - Programming fundamentals
- [[coding/Dynamic Programming]] - Optimization technique
- Additional algorithm notes

## 🏗️ Design Patterns

- [[design_patterns/Design Patterns]] - Software architecture
- [[design_patterns/Leaky abstraction]] - Abstraction failures
- [[design_patterns/Designing Distributed Systems]] - Scalability patterns

## 🎯 Learning Paths

### Beginner → Intermediate
1. Start with [[Cryptography/Cryptography]] for overview
2. Understand [[Cryptography/CIA Triad]] security principles
3. Learn [[Cryptography/Hashing]] basics
4. Explore [[Cryptography/Token Authentication]]

### Intermediate → Advanced
1. Study [[Cryptography/STRIDE]] threat modeling
2. Understand [[Cryptography/Side Channel Attack]]
3. Deep dive into [[Cryptography/ENTROPY]]
4. Research [[Cryptography/Zero-Trust]] architecture

### Security Focus
1. [[Cryptography/STRIDE]] - Threat categorization
2. [[Cryptography/Zero Day Attack]] - Vulnerability research
3. [[Cryptography/Buffer Overflows]] - Exploitation techniques
4. [[Cryptography/Cold Boot]] - Physical security

## 🔗 Cross-Domain Connections

- **Entropy & Vikalpa** - Information theory meets Vedic philosophy (see [[../research/entropy-vikalpa]])
- **Security & Trust** - Technical and philosophical dimensions
- **Design Patterns & Dharma** - Universal patterns across domains

## 🏷️ Common Tags

`#security` `#cryptography` `#hashing` `#encryption` `#authentication` `#vulnerabilities` `#algorithms` `#design-patterns`

## 📊 Statistics

- **Total Notes**: {cse_count}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 🔄 Maintenance

This README is auto-generated. To update counts: `python ../generate_readmes.py`

---

[← Back to Main Index](../INDEX.md)
"""
    return template

def generate_sanskrit_readme(sanskrit_count):
    """Generate sanskrit-lit/README.md with current counts."""
    template = f"""# Sanskrit Literature & Philosophy

> Vedic texts, yoga philosophy, Sanskrit language, and ancient Indian wisdom traditions.

## 📚 Overview

This domain contains **{sanskrit_count} notes** covering:
- **Vedic Texts** - Vedas, Upanishads, Puranas
- **Yoga Philosophy** - Sutras, practices, concepts
- **Sanskrit Language** - Grammar, phonetics, literature
- **Concepts** - Philosophical and spiritual principles
- **Deities & Figures** - Krishna, Rudra, Agni, Hanuman

## 🕉️ Core Texts

### Yoga & Meditation
- [[yoga_sutras]] - Patanjali's foundational text
- [[Yogasutras]] - Detailed sutras and commentary
- [[NirvanaShatakam]] - Adi Shankaracharya's composition
- [[HanumaStuthi]] - Devotional hymns
- [[Hanuman Chalisa]] - Popular devotional text

### Upanishads & Philosophy
- [[Upanishads]] - Vedantic philosophy
- [[Vaiseshika Darshanam]] - Atomic theory school
- [[VaishshikaSutra]] - Foundational sutras
- [[NyayaSutra]] - Logic and epistemology

### Vedas & Brahmanas
- [[Atharvanaveda]] - Fourth Veda
- [[Itheriya brahmana]] - Ritual commentary

### Puranas
- [[mathsya purana]] - Fish incarnation mythology

### Devotional Literature
- [[VishnuSahasranamam]] - Thousand names of Vishnu
- [[VishnuSahasranamamByDusyanthSridhar]] - Commentary by Dushyanth Sridhar
- [[SivaSurta]] - Shiva compositions

## 🎵 Music & Arts

- [[Sangitaratnakaram]] - Classical music treatise
- [[Amarakosham]] - Sanskrit thesaurus
- [[Brihadesi]] - Music theory

## 📖 Language & Grammar

- [[Ashtadhyayi]] - Panini's Sanskrit grammar
- [[Sutra]] - Aphoristic style
- [[Niruktha]] - Etymology and semantics
- [[Sulba Sutras]] - Geometric mathematics

## 🌿 Ayurveda & Wellness

- [[Ayurvedam]] - Traditional medicine
- [[AyurvedicRemedies]] - Healing practices

## 🔑 Key Concepts

### Philosophical Principles
- [[Dharma]] - Universal law and duty
- [[Karma]] - Action and consequence
- [[Manas]] - Mind and consciousness
- [[chitta]] - Mental modifications
- [[Vikalpa]] - Conceptual thought

### Elements & Energy
- [[Agni]] - Fire element
- [[Vayu]] - Air/wind element
- [[Prana]] - Life force
- [[Concepts/PanchaVayu]] - Five vital airs
- [[Nada]] - Cosmic sound

### Language & Expression
- [[Akshara]] - Imperishable syllable
- [[kavi]] - Poet, seer
- [[speech]] - Power of sound
- [[acharya]] - Spiritual teacher

### Deities & Divine Forms
- [[krishna]] - Jagath Guru, dark-complexioned
- [[Rudra]] - Fierce form of Shiva

### Perception & Knowledge
- [[eye]] - Organ of perception
- Vision and insight

### Time & Astronomy
- [[tithi]] - Lunar day

## 🎯 Reading Paths

### Beginner's Journey
1. Start with [[Yogasutras]] for practical philosophy
2. Read [[Dharma]] and [[Karma]] for ethical foundations
3. Explore [[krishna]] and [[VishnuSahasranamam]] for devotional context
4. Study [[Upanishads]] for deeper philosophy

### Yoga Practitioner
1. [[yoga_sutras]] - Foundation
2. [[chitta]] - Understanding mind
3. [[Prana]] and [[Concepts/PanchaVayu]] - Energy systems
4. [[NirvanaShatakam]] - Non-dual realization

### Language Scholar
1. [[Ashtadhyayi]] - Grammar foundation
2. [[Niruktha]] - Etymology
3. [[Sutra]] - Aphoristic style
4. [[Amarakosham]] - Vocabulary

### Philosophy Student
1. [[Upanishads]] - Vedantic foundation
2. [[NyayaSutra]] - Logic and reasoning
3. [[Vaiseshika Darshanam]] - Atomic theory
4. [[Dharma]] and [[Karma]] - Ethical philosophy

## 🔗 Cross-Domain Connections

- **Entropy & Vikalpa** - Information theory meets conceptual thought (see [[../research/entropy-vikalpa]])
- **Cryptography & Sutras** - Conciseness and precision across domains
- **Design Patterns & Dharma** - Universal patterns in code and cosmos

## 🏷️ Common Tags

`#vedic` `#yoga` `#philosophy` `#sanskrit` `#upanishads` `#sutras` `#ayurveda` `#devotional` `#grammar` `#music`

## 📊 Statistics

- **Total Notes**: {sanskrit_count}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 🔄 Maintenance

This README is auto-generated. To update counts: `python ../generate_readmes.py`

---

[← Back to Main Index](../INDEX.md)
"""
    return template

def generate_highlights_readme(highlights_count):
    """Generate highlights/README.md with current counts."""
    template = f"""# Book & Article Highlights

> Curated highlights and summaries from books, articles, and other reading materials.

## 📚 Overview

This domain contains **{highlights_count} highlights** organized by source type:
- **Books/** - Book highlights and key takeaways
- **Articles/** - Article summaries and insights

## 📖 Book Highlights

### Self-Improvement
- [[Books/Atomic Habits]] - James Clear on habit formation
- One percent rule and aggregation of marginal gains

### Biography
- [[Books/Elon Musk]] - Ashlee Vance biography (if present)

### Additional Books
Browse `Books/` directory for complete collection.

## 📰 Article Highlights

Browse `Articles/` directory for curated article summaries.

## 🎯 How to Use

1. **Quick Reference** - Find key insights from books you've read
2. **Discovery** - Browse highlights to find books worth reading
3. **Connection** - See wikilinks to related concepts across domains
4. **Review** - Revisit key ideas and refresh memory

## 🔗 Cross-Domain Connections

Book highlights often connect to:
- **CSE** - Technical concepts and algorithms
- **Sanskrit-lit** - Philosophy and wisdom traditions
- **pages/** - Concept notes derived from reading

## 📊 Statistics

- **Total Highlights**: {highlights_count}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 🔄 Maintenance

This README is auto-generated. To update counts: `python ../generate_readmes.py`

---

[← Back to Main Index](../INDEX.md)
"""
    return template

def main():
    """Main function to generate all README files."""
    base_path = Path(__file__).parent

    print("📊 Counting notes across domains...")
    domain_counts, all_notes = count_notes(base_path)
    total_notes = len(all_notes)

    print(f"✅ Found {total_notes} total notes")
    for domain, count in sorted(domain_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {count:3d} notes - {domain}")

    # Generate main INDEX.md
    print("\n📝 Generating INDEX.md...")
    index_content = generate_main_index(domain_counts, total_notes)
    (base_path / "INDEX.md").write_text(index_content)
    print("✅ INDEX.md updated")

    # Generate CSE/README.md
    if domain_counts.get('CSE', 0) > 0:
        print("\n📝 Generating CSE/README.md...")
        crypto_count = len(list((base_path / "CSE" / "Cryptography").glob("*.md")))
        cse_content = generate_cse_readme(domain_counts['CSE'], crypto_count)
        (base_path / "CSE" / "README.md").write_text(cse_content)
        print("✅ CSE/README.md updated")

    # Generate sanskrit-lit/README.md
    if domain_counts.get('sanskrit-lit', 0) > 0:
        print("\n📝 Generating sanskrit-lit/README.md...")
        sanskrit_content = generate_sanskrit_readme(domain_counts['sanskrit-lit'])
        (base_path / "sanskrit-lit" / "README.md").write_text(sanskrit_content)
        print("✅ sanskrit-lit/README.md updated")

    # Generate highlights/README.md
    if domain_counts.get('highlights', 0) > 0:
        print("\n📝 Generating highlights/README.md...")
        highlights_content = generate_highlights_readme(domain_counts['highlights'])
        (base_path / "highlights" / "README.md").write_text(highlights_content)
        print("✅ highlights/README.md updated")

    print(f"\n🎉 All README files updated with current counts!")
    print(f"📈 Total: {total_notes} notes across {len([d for d in domain_counts if domain_counts[d] > 0])} domains")

if __name__ == "__main__":
    main()
