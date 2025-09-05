#!/usr/bin/env python3
"""
Script to apply missing cross-references to markdown notes.
This can be run in dry-run mode or actual update mode.
"""

import os
import re
import json
from pathlib import Path
import shutil
from datetime import datetime

class LinkApplicator:
    def __init__(self, base_path, dry_run=True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup_dir = self.base_path / "backups" / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.changes_made = []
        
    def load_suggestions(self):
        """Load the missing links suggestions from JSON"""
        json_path = self.base_path / "missing_links.json"
        if not json_path.exists():
            print("Error: missing_links.json not found. Run analyze_links.py first.")
            return None
            
        with open(json_path, 'r') as f:
            return json.load(f)
            
    def create_backup(self, file_path):
        """Create a backup of the file before modifying"""
        if self.dry_run:
            return
            
        if not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True)
            
        rel_path = Path(file_path).relative_to(self.base_path)
        backup_path = self.backup_dir / rel_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_path)
        
    def add_link(self, content, target_name, context_size=50):
        """Add wiki-style links around unlinked mentions of target"""
        # Escape special regex characters in target_name
        escaped_target = re.escape(target_name)
        
        # Pattern to find unlinked mentions (not already in [[...]])
        # Look for the target that's not already within double brackets
        pattern = r'(?<!\[\[)(?<!\[\[[\w\s]*)\b(' + escaped_target + r')\b(?![\w\s]*\]\])'
        
        # Count how many replacements we'll make
        matches = re.finditer(pattern, content, re.IGNORECASE)
        count = 0
        
        # Replace unlinked mentions with linked versions
        def replace_match(match):
            nonlocal count
            count += 1
            # Only replace first 3 occurrences to avoid over-linking
            if count <= 3:
                return f"[[{match.group(1)}]]"
            return match.group(0)
            
        new_content = re.sub(pattern, replace_match, content, flags=re.IGNORECASE)
        
        return new_content, count
        
    def apply_links_to_file(self, note_path, suggestions, max_links=3):
        """Apply suggested links to a single file"""
        file_path = self.base_path / note_path
        
        if not file_path.exists():
            print(f"Warning: File not found: {note_path}")
            return 0
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        links_added = 0
        changes = []
        
        # Sort suggestions by strength and apply top ones
        sorted_suggestions = sorted(suggestions, key=lambda x: x['strength'], reverse=True)
        
        for suggestion in sorted_suggestions[:max_links]:
            target_name = suggestion['target_name']
            
            # Skip if already linked
            if f"[[{target_name}]]" in content:
                continue
                
            # Try to add the link
            new_content, count = self.add_link(content, target_name)
            
            if count > 0:
                content = new_content
                links_added += count
                changes.append({
                    "target": target_name,
                    "count": count,
                    "reason": suggestion['reason']
                })
                
        if links_added > 0:
            if not self.dry_run:
                self.create_backup(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            self.changes_made.append({
                "file": note_path,
                "links_added": links_added,
                "changes": changes
            })
            
        return links_added
        
    def apply_all(self, max_files=10):
        """Apply links to multiple files"""
        suggestions = self.load_suggestions()
        if not suggestions:
            return
            
        print(f"\n{'DRY RUN - ' if self.dry_run else ''}Applying missing links...")
        print(f"Processing up to {max_files} files with highest priority links\n")
        
        total_links = 0
        files_processed = 0
        
        # Sort files by total strength of suggestions
        sorted_files = sorted(
            suggestions['missing_links'].items(),
            key=lambda x: sum(s['strength'] for s in x[1]),
            reverse=True
        )
        
        for note_path, file_suggestions in sorted_files[:max_files]:
            links_added = self.apply_links_to_file(note_path, file_suggestions)
            if links_added > 0:
                total_links += links_added
                files_processed += 1
                print(f"{'[DRY RUN] ' if self.dry_run else ''}Modified {note_path}: {links_added} links added")
                
        print(f"\n{'DRY RUN ' if self.dry_run else ''}Summary:")
        print(f"- Files processed: {files_processed}")
        print(f"- Total links added: {total_links}")
        
        if not self.dry_run:
            print(f"- Backups created in: {self.backup_dir}")
            
        # Save detailed change log
        self.save_change_log()
        
    def save_change_log(self):
        """Save a detailed log of all changes"""
        log_path = "link_changes.json" if not self.dry_run else "link_changes_dryrun.json"
        
        with open(log_path, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "dry_run": self.dry_run,
                "changes": self.changes_made
            }, f, indent=2)
            
        print(f"- Change log saved to: {log_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Apply missing cross-references to notes')
    parser.add_argument('--apply', action='store_true', 
                       help='Actually apply changes (default is dry-run)')
    parser.add_argument('--max-files', type=int, default=10,
                       help='Maximum number of files to process (default: 10)')
    
    args = parser.parse_args()
    
    applicator = LinkApplicator(
        base_path="/Users/narenmudivarthy/Projects/literature-notes",
        dry_run=not args.apply
    )
    
    if args.apply:
        response = input("WARNING: This will modify your files. Backups will be created. Continue? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
            
    applicator.apply_all(max_files=args.max_files)

if __name__ == "__main__":
    main()