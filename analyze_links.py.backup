#!/usr/bin/env python3
"""
Script to analyze markdown notes and identify missing cross-references.
This performs a dry-run analysis without modifying any files.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

class NoteLinkAnalyzer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.notes = {}  # filename -> content
        self.existing_links = defaultdict(set)  # note -> set of linked notes
        self.concept_map = defaultdict(set)  # concept -> set of notes containing it
        self.potential_links = defaultdict(list)  # note -> list of (target_note, reason, strength)
        
    def load_notes(self):
        """Load all markdown files"""
        for md_file in self.base_path.rglob("*.md"):
            if 'templates' in str(md_file):
                continue
            rel_path = md_file.relative_to(self.base_path)
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.notes[str(rel_path)] = content
                
    def extract_existing_links(self):
        """Extract all existing [[wiki-style]] links"""
        link_pattern = r'\[\[([^\]]+)\]\]'
        
        for note_path, content in self.notes.items():
            matches = re.findall(link_pattern, content)
            self.existing_links[note_path].update(matches)
            
    def build_concept_map(self):
        """Build a map of important concepts to notes containing them"""
        # Key concepts to track
        important_concepts = {
            # Cryptography concepts
            'encryption', 'hash', 'sha-256', 'sha-512', 'hmac', 'entropy', 'cryptograph',
            'signature', 'key', 'cipher', 'authentication', 'integrity', 'confidentiality',
            
            # Security concepts  
            'attack', 'vulnerability', 'security', 'rowhammer', 'cold boot', 'side channel',
            'spoofing', 'tampering', 'denial of service', 'zero-trust',
            
            # Sanskrit/Philosophy
            'yoga', 'sutra', 'sanskrit', 'veda', 'vedanta', 'karma', 'dharma', 'chitta',
            'prana', 'rudra', 'agni', 'panini', 'nirukta', 'brahmana', 'upanishad',
            
            # Ayurveda
            'ayurveda', 'vaagbhata', 'charaka', 'samhita', 'dosha', 'vata', 'pitta', 'kapha',
            
            # Indian history
            'aryan', 'indology', 'muller', 'cunningham', 'angkor wat', 'india',
            
            # Programming
            'python', 'unix', 'testing', 'tdd', 'design pattern', 'decorator', 'algorithm'
        }
        
        for note_path, content in self.notes.items():
            content_lower = content.lower()
            note_name = Path(note_path).stem.lower()
            
            for concept in important_concepts:
                if concept in content_lower or concept in note_name:
                    self.concept_map[concept].add(note_path)
                    
    def find_missing_links(self):
        """Identify potential missing cross-references"""
        
        for note_path, content in self.notes.items():
            content_lower = content.lower()
            note_name = Path(note_path).stem
            
            # Check for mentions of other note titles that aren't linked
            for other_path in self.notes:
                if other_path == note_path:
                    continue
                    
                other_name = Path(other_path).stem
                other_name_lower = other_name.lower()
                
                # Skip if already linked
                if other_name in self.existing_links[note_path]:
                    continue
                    
                # Check if the note name appears in content but isn't linked
                if other_name_lower in content_lower:
                    # Calculate strength based on frequency
                    count = content_lower.count(other_name_lower)
                    self.potential_links[note_path].append((
                        other_path, 
                        f"Mentions '{other_name}' {count} time(s) but not linked",
                        count * 10
                    ))
                    
            # Find notes with related concepts
            for concept, related_notes in self.concept_map.items():
                if concept in content_lower:
                    for related_note in related_notes:
                        if related_note == note_path:
                            continue
                        related_name = Path(related_note).stem
                        if related_name not in self.existing_links[note_path]:
                            # Check if they share multiple concepts for stronger connection
                            shared_concepts = self.get_shared_concepts(note_path, related_note)
                            if len(shared_concepts) > 1:
                                self.potential_links[note_path].append((
                                    related_note,
                                    f"Related via concepts: {', '.join(list(shared_concepts)[:3])}",
                                    len(shared_concepts) * 5
                                ))
                                
    def get_shared_concepts(self, note1, note2):
        """Find concepts shared between two notes"""
        shared = set()
        content1_lower = self.notes[note1].lower()
        content2_lower = self.notes[note2].lower()
        
        for concept, notes in self.concept_map.items():
            if note1 in notes and note2 in notes:
                shared.add(concept)
                
        return shared
        
    def analyze_link_patterns(self):
        """Analyze specific patterns that suggest links should exist"""
        patterns_to_check = [
            # Cryptography chain
            ('Hash Algorithms.md', 'HMAC.md', "HMAC uses hash algorithms"),
            ('Hash Algorithms.md', 'Digital signatures.md', "Digital signatures use hash algorithms"),
            ('Encryption.md', 'Block Cipher.md', "Block ciphers are encryption methods"),
            ('ENTROPY.md', 'Key exchange.md', "Key exchange requires entropy"),
            
            # Security chain
            ('Authentication.md', 'Strong Authentication.md', "Related authentication concepts"),
            ('Spoofing.md', 'Authentication.md', "Spoofing attacks authentication"),
            ('Tampering.md', 'Integrity.md', "Tampering violates integrity"),
            
            # Sanskrit connections
            ('Yoga Sutras.md', 'chitta.md', "Chitta is a key concept in Yoga Sutras"),
            ('karma.md', 'chitta.md', "Karma affects chitta"),
            ('Panini.md', 'Niruktha.md', "Both are Sanskrit grammar texts"),
            ('Rudra.md', 'Prana.md', "Related vedic concepts"),
            
            # Cross-domain
            ('ENTROPY.md', 'Vikalpa.md', "Entropy and uncertainty/alternatives"),
            ('Unix philosophy.md', 'Test Driven Dev.md', "Related development philosophies"),
        ]
        
        for source, target, reason in patterns_to_check:
            # Find matching files
            source_matches = [p for p in self.notes if source in p]
            target_matches = [p for p in self.notes if target in p]
            
            for src in source_matches:
                for tgt in target_matches:
                    tgt_name = Path(tgt).stem
                    if tgt_name not in self.existing_links[src]:
                        self.potential_links[src].append((tgt, reason, 15))
                        
    def generate_report(self):
        """Generate a comprehensive report of missing links"""
        report = []
        report.append("# Missing Cross-Reference Analysis Report\n")
        report.append(f"Analyzed {len(self.notes)} notes\n")
        report.append(f"Found {sum(len(v) for v in self.existing_links.values())} existing links\n\n")
        
        # Sort by number of potential links
        sorted_notes = sorted(self.potential_links.items(), 
                            key=lambda x: sum(link[2] for link in x[1]), 
                            reverse=True)
        
        report.append("## Top Missing Links by Priority\n\n")
        
        total_suggestions = 0
        for note_path, suggestions in sorted_notes[:20]:  # Top 20 notes
            if not suggestions:
                continue
                
            # Sort suggestions by strength
            suggestions.sort(key=lambda x: x[2], reverse=True)
            
            report.append(f"### {note_path}\n")
            for target, reason, strength in suggestions[:5]:  # Top 5 suggestions per note
                report.append(f"- **→ [[{Path(target).stem}]]** (strength: {strength})\n")
                report.append(f"  - Reason: {reason}\n")
                total_suggestions += 1
                
            report.append("\n")
            
        report.append(f"\n## Summary\n")
        report.append(f"- Total notes with missing links: {len(self.potential_links)}\n")
        report.append(f"- Total link suggestions: {total_suggestions}\n")
        
        # Concept network stats
        report.append(f"\n## Concept Network Statistics\n")
        top_concepts = sorted(self.concept_map.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        for concept, notes in top_concepts:
            report.append(f"- **{concept}**: appears in {len(notes)} notes\n")
            
        return "".join(report)
        
    def export_json(self):
        """Export findings as JSON for programmatic use"""
        data = {
            "stats": {
                "total_notes": len(self.notes),
                "total_existing_links": sum(len(v) for v in self.existing_links.values()),
                "notes_with_missing_links": len(self.potential_links)
            },
            "missing_links": {}
        }
        
        for note_path, suggestions in self.potential_links.items():
            if suggestions:
                data["missing_links"][note_path] = [
                    {
                        "target": target,
                        "target_name": Path(target).stem,
                        "reason": reason,
                        "strength": strength
                    }
                    for target, reason, strength in sorted(suggestions, key=lambda x: x[2], reverse=True)[:5]
                ]
                
        return json.dumps(data, indent=2)

def main():
    print("Starting cross-reference analysis...")
    
    analyzer = NoteLinkAnalyzer("/Users/narenmudivarthy/Projects/literature-notes")
    
    print("Loading notes...")
    analyzer.load_notes()
    
    print("Extracting existing links...")
    analyzer.extract_existing_links()
    
    print("Building concept map...")
    analyzer.build_concept_map()
    
    print("Finding missing links...")
    analyzer.find_missing_links()
    
    print("Analyzing link patterns...")
    analyzer.analyze_link_patterns()
    
    print("Generating report...")
    report = analyzer.generate_report()
    
    # Save report
    with open("missing_links_report.md", "w") as f:
        f.write(report)
    print("Report saved to missing_links_report.md")
    
    # Save JSON
    with open("missing_links.json", "w") as f:
        f.write(analyzer.export_json())
    print("JSON data saved to missing_links.json")
    
    print("\nDry run complete! No files were modified.")
    print("Review the report to see suggested cross-references.")

if __name__ == "__main__":
    main()