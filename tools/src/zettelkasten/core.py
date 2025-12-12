#!/usr/bin/env python3
"""
Zettelkasten Note Management System
Indexes, searches, and connects markdown notes for a knowledge management system.
"""

import os
import re
import json
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Optional, Tuple
import sqlite3
from datetime import datetime


@dataclass
class Note:
    """Represents a single note in the Zettelkasten system."""
    path: str
    title: str
    content: str
    tags: List[str]
    wikilinks: List[str]
    backlinks: List[str]
    created: datetime
    modified: datetime
    word_count: int


class ZettelkastenDB:
    """Database manager for the Zettelkasten system."""
    
    def __init__(self, db_path: str = "zettelkasten.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()
    
    def _create_tables(self):
        """Create database tables if they don't exist."""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT NOT NULL,
                wikilinks TEXT NOT NULL,
                backlinks TEXT NOT NULL,
                created TEXT NOT NULL,
                modified TEXT NOT NULL,
                word_count INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_path TEXT NOT NULL,
                target_path TEXT NOT NULL,
                link_type TEXT NOT NULL,
                FOREIGN KEY (source_path) REFERENCES notes (path),
                FOREIGN KEY (target_path) REFERENCES notes (path)
            );
            
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag TEXT NOT NULL,
                note_path TEXT NOT NULL,
                FOREIGN KEY (note_path) REFERENCES notes (path)
            );
            
            CREATE INDEX IF NOT EXISTS idx_notes_title ON notes(title);
            CREATE INDEX IF NOT EXISTS idx_notes_path ON notes(path);
            CREATE INDEX IF NOT EXISTS idx_links_source ON links(source_path);
            CREATE INDEX IF NOT EXISTS idx_links_target ON links(target_path);
            CREATE INDEX IF NOT EXISTS idx_tags_tag ON tags(tag);
        """)
        self.conn.commit()
    
    def save_note(self, note: Note):
        """Save a note to the database."""
        self.conn.execute("""
            INSERT OR REPLACE INTO notes 
            (path, title, content, tags, wikilinks, backlinks, created, modified, word_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            note.path, note.title, note.content,
            json.dumps(note.tags), json.dumps(note.wikilinks), json.dumps(note.backlinks),
            note.created.isoformat(), note.modified.isoformat(), note.word_count
        ))
        
        # Save tags
        self.conn.execute("DELETE FROM tags WHERE note_path = ?", (note.path,))
        for tag in note.tags:
            self.conn.execute("INSERT INTO tags (tag, note_path) VALUES (?, ?)", (tag, note.path))
        
        self.conn.commit()
    
    def get_note(self, path: str) -> Optional[Note]:
        """Get a note by path."""
        row = self.conn.execute("SELECT * FROM notes WHERE path = ?", (path,)).fetchone()
        if not row:
            return None
        
        return Note(
            path=row['path'],
            title=row['title'],
            content=row['content'],
            tags=json.loads(row['tags']),
            wikilinks=json.loads(row['wikilinks']),
            backlinks=json.loads(row['backlinks']),
            created=datetime.fromisoformat(row['created']),
            modified=datetime.fromisoformat(row['modified']),
            word_count=row['word_count']
        )
    
    def search_notes(self, query: str, limit: int = 20) -> List[Note]:
        """Search notes by content or title."""
        rows = self.conn.execute("""
            SELECT * FROM notes 
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY 
                CASE WHEN title LIKE ? THEN 1 ELSE 2 END,
                word_count DESC
            LIMIT ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%", limit)).fetchall()
        
        return [self._row_to_note(row) for row in rows]
    
    def get_notes_by_tag(self, tag: str) -> List[Note]:
        """Get all notes with a specific tag."""
        rows = self.conn.execute("""
            SELECT n.* FROM notes n
            JOIN tags t ON n.path = t.note_path
            WHERE t.tag = ?
            ORDER BY n.title
        """, (tag,)).fetchall()
        
        return [self._row_to_note(row) for row in rows]
    
    def get_all_tags(self) -> List[Tuple[str, int]]:
        """Get all tags with their counts."""
        rows = self.conn.execute("""
            SELECT tag, COUNT(*) as count 
            FROM tags 
            GROUP BY tag 
            ORDER BY count DESC, tag
        """).fetchall()
        
        return [(row['tag'], row['count']) for row in rows]
    
    def get_linked_notes(self, path: str) -> List[Note]:
        """Get all notes linked from the given note."""
        rows = self.conn.execute("""
            SELECT n.* FROM notes n
            JOIN links l ON n.path = l.target_path
            WHERE l.source_path = ?
        """, (path,)).fetchall()
        
        return [self._row_to_note(row) for row in rows]
    
    def get_backlinked_notes(self, path: str) -> List[Note]:
        """Get all notes that link to the given note."""
        rows = self.conn.execute("""
            SELECT n.* FROM notes n
            JOIN links l ON n.path = l.source_path
            WHERE l.target_path = ?
        """, (path,)).fetchall()
        
        return [self._row_to_note(row) for row in rows]
    
    def _row_to_note(self, row) -> Note:
        """Convert database row to Note object."""
        return Note(
            path=row['path'],
            title=row['title'],
            content=row['content'],
            tags=json.loads(row['tags']),
            wikilinks=json.loads(row['wikilinks']),
            backlinks=json.loads(row['backlinks']),
            created=datetime.fromisoformat(row['created']),
            modified=datetime.fromisoformat(row['modified']),
            word_count=row['word_count']
        )
    
    def close(self):
        """Close database connection."""
        self.conn.close()


class ZettelkastenIndexer:
    """Indexes markdown files and builds the knowledge graph."""
    
    def __init__(self, root_path: str, db: ZettelkastenDB):
        self.root_path = Path(root_path)
        self.db = db
        self.notes_cache = {}
        
    def index_all_notes(self):
        """Index all markdown files in the directory tree."""
        print("Indexing notes...")
        
        # Find all markdown files
        md_files = list(self.root_path.rglob("*.md"))
        print(f"Found {len(md_files)} markdown files")
        
        # First pass: index all notes
        for md_file in md_files:
            try:
                note = self._parse_note(md_file)
                if note:
                    self.notes_cache[note.path] = note
                    self.db.save_note(note)
            except Exception as e:
                print(f"Error indexing {md_file}: {e}")
        
        # Second pass: build link relationships
        print("Building link relationships...")
        self._build_link_relationships()
        
        print(f"Indexed {len(self.notes_cache)} notes successfully")
    
    def _parse_note(self, file_path: Path) -> Optional[Note]:
        """Parse a markdown file into a Note object."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
        
        # Extract title (first heading or filename)
        title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else file_path.stem
        
        # Extract tags (both #hashtags and #word format)
        tags = re.findall(r'#(\w+)', content)
        tags = list(set(tags))  # Remove duplicates
        
        # Extract wikilinks [[link]]
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        wikilinks = list(set(wikilinks))  # Remove duplicates
        
        # Get file stats
        stat = file_path.stat()
        created = datetime.fromtimestamp(stat.st_ctime)
        modified = datetime.fromtimestamp(stat.st_mtime)
        
        # Count words
        word_count = len(re.findall(r'\b\w+\b', content))
        
        # Convert path to relative path from root
        rel_path = str(file_path.relative_to(self.root_path))
        
        return Note(
            path=rel_path,
            title=title,
            content=content,
            tags=tags,
            wikilinks=wikilinks,
            backlinks=[],  # Will be populated in second pass
            created=created,
            modified=modified,
            word_count=word_count
        )
    
    def _build_link_relationships(self):
        """Build backlinks and save link relationships to database."""
        # Clear existing links
        self.db.conn.execute("DELETE FROM links")
        
        # Build backlinks map
        backlinks_map = defaultdict(list)
        
        for note in self.notes_cache.values():
            for wikilink in note.wikilinks:
                # Find matching notes for this wikilink
                matching_notes = self._find_matching_notes(wikilink)
                
                for target_path in matching_notes:
                    # Save link to database
                    self.db.conn.execute(
                        "INSERT INTO links (source_path, target_path, link_type) VALUES (?, ?, ?)",
                        (note.path, target_path, 'wikilink')
                    )
                    
                    # Add to backlinks map
                    backlinks_map[target_path].append(note.path)
        
        # Update notes with backlinks
        for note_path, backlink_paths in backlinks_map.items():
            if note_path in self.notes_cache:
                self.notes_cache[note_path].backlinks = backlink_paths
                self.db.save_note(self.notes_cache[note_path])
        
        self.db.conn.commit()
    
    def _find_matching_notes(self, wikilink: str) -> List[str]:
        """Find notes that match a wikilink."""
        matching_paths = []
        
        for note_path, note in self.notes_cache.items():
            # Check if title matches (case insensitive)
            if note.title.lower() == wikilink.lower():
                matching_paths.append(note_path)
            # Check if filename matches (without extension)
            elif Path(note_path).stem.lower() == wikilink.lower():
                matching_paths.append(note_path)
        
        return matching_paths


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description="Zettelkasten Note Management System")
    parser.add_argument("--root", default=".", help="Root directory of notes")
    parser.add_argument("--db", default="zettelkasten.db", help="Database file path")
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Index command
    index_parser = subparsers.add_parser('index', help='Index all notes')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search notes')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--limit', type=int, default=10, help='Number of results')
    
    # Tags command
    tags_parser = subparsers.add_parser('tags', help='List all tags')
    tags_parser.add_argument('--tag', help='Show notes with specific tag')
    
    # Links command
    links_parser = subparsers.add_parser('links', help='Show links for a note')
    links_parser.add_argument('note_path', help='Path to note')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show system statistics')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize database
    db = ZettelkastenDB(args.db)
    
    try:
        if args.command == 'index':
            indexer = ZettelkastenIndexer(args.root, db)
            indexer.index_all_notes()
            
        elif args.command == 'search':
            results = db.search_notes(args.query, args.limit)
            if results:
                print(f"Found {len(results)} results for '{args.query}':\n")
                for note in results:
                    print(f"📄 {note.title}")
                    print(f"   Path: {note.path}")
                    print(f"   Tags: {', '.join(note.tags) if note.tags else 'None'}")
                    print(f"   Words: {note.word_count}")
                    if note.wikilinks:
                        print(f"   Links: {', '.join(note.wikilinks[:3])}{'...' if len(note.wikilinks) > 3 else ''}")
                    print()
            else:
                print(f"No results found for '{args.query}'")
                
        elif args.command == 'tags':
            if args.tag:
                notes = db.get_notes_by_tag(args.tag)
                print(f"Notes tagged with '{args.tag}' ({len(notes)}):\n")
                for note in notes:
                    print(f"📄 {note.title} ({note.path})")
            else:
                tags = db.get_all_tags()
                print(f"All tags ({len(tags)}):\n")
                for tag, count in tags:
                    print(f"#{tag} ({count})")
                    
        elif args.command == 'links':
            note = db.get_note(args.note_path)
            if not note:
                print(f"Note not found: {args.note_path}")
                return
                
            print(f"Links for '{note.title}':\n")
            
            # Outgoing links
            linked_notes = db.get_linked_notes(args.note_path)
            if linked_notes:
                print("📤 Outgoing links:")
                for linked_note in linked_notes:
                    print(f"  → {linked_note.title} ({linked_note.path})")
                print()
            
            # Backlinks
            backlinked_notes = db.get_backlinked_notes(args.note_path)
            if backlinked_notes:
                print("📥 Backlinks:")
                for backlinked_note in backlinked_notes:
                    print(f"  ← {backlinked_note.title} ({backlinked_note.path})")
                print()
            
            if not linked_notes and not backlinked_notes:
                print("No links found.")
                
        elif args.command == 'stats':
            # Get basic stats
            total_notes = db.conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
            total_links = db.conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
            total_tags = db.conn.execute("SELECT COUNT(DISTINCT tag) FROM tags").fetchone()[0]
            
            # Get top tags
            top_tags = db.conn.execute("""
                SELECT tag, COUNT(*) as count 
                FROM tags 
                GROUP BY tag 
                ORDER BY count DESC 
                LIMIT 10
            """).fetchall()
            
            # Get most linked notes
            most_linked = db.conn.execute("""
                SELECT n.title, n.path, COUNT(l.target_path) as link_count
                FROM notes n
                LEFT JOIN links l ON n.path = l.target_path
                GROUP BY n.path
                ORDER BY link_count DESC
                LIMIT 10
            """).fetchall()
            
            print("📊 Zettelkasten Statistics\n")
            print(f"Total notes: {total_notes}")
            print(f"Total links: {total_links}")
            print(f"Total tags: {total_tags}")
            print(f"Average links per note: {total_links / total_notes:.1f}" if total_notes > 0 else "")
            print()
            
            if top_tags:
                print("🏷️  Top tags:")
                for tag, count in top_tags:
                    print(f"  #{tag} ({count})")
                print()
            
            if most_linked:
                print("🔗 Most linked notes:")
                for title, path, count in most_linked:
                    if count > 0:
                        print(f"  {title} ({count} links)")
                print()
    
    finally:
        db.close()


if __name__ == "__main__":
    main()