#!/usr/bin/env python3
"""
Knowledge Synthesis Tool for Literature Notes
Automatically generates summaries and surfaces connections between notes
"""

import json
import sqlite3
import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Set
from collections import defaultdict, Counter
import re
import os

class KnowledgeSynthesizer:
    """Synthesizes knowledge from notes to create insights and connections"""
    
    def __init__(self, db_path: str = "zettelkasten.db"):
        self.db_path = db_path
        
    def generate_domain_summary(self, domain: str, max_notes: int = 10) -> Dict:
        """Generate a summary of knowledge in a specific domain"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # Find notes related to the domain
        cursor = conn.execute("""
            SELECT path, title, content, tags, word_count
            FROM notes
            WHERE content LIKE ? OR title LIKE ? OR tags LIKE ?
            ORDER BY word_count DESC
            LIMIT ?
        """, (f'%{domain}%', f'%{domain}%', f'%{domain}%', max_notes))
        
        notes = [dict(row) for row in cursor]
        
        if not notes:
            conn.close()
            return {'domain': domain, 'summary': 'No notes found for this domain'}
        
        # Extract key concepts
        concepts = self._extract_key_concepts(notes)
        
        # Find connections between notes
        connections = self._find_note_connections(conn, [n['path'] for n in notes])
        
        # Generate summary
        summary = {
            'domain': domain,
            'note_count': len(notes),
            'total_words': sum(n['word_count'] for n in notes),
            'key_concepts': concepts[:10],
            'main_topics': self._extract_main_topics(notes),
            'connections': connections,
            'top_notes': [{'title': n['title'], 'path': n['path']} for n in notes[:5]]
        }
        
        conn.close()
        return summary
    
    def generate_daily_synthesis(self, num_notes: int = 5) -> Dict:
        """Generate a daily synthesis of related notes"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # Get recently accessed or random notes as seeds
        cursor = conn.execute("""
            SELECT path, title, tags, wikilinks
            FROM notes
            ORDER BY RANDOM()
            LIMIT ?
        """, (num_notes,))
        
        seed_notes = [dict(row) for row in cursor]
        
        # Build synthesis groups
        synthesis_groups = []
        used_notes = set()
        
        for seed in seed_notes:
            if seed['path'] in used_notes:
                continue
                
            group = self._build_synthesis_group(conn, seed, used_notes)
            if len(group) > 1:  # Only include groups with connections
                synthesis_groups.append(group)
        
        # Create daily synthesis
        synthesis = {
            'date': datetime.now().isoformat(),
            'groups': synthesis_groups,
            'insights': self._generate_insights(conn, synthesis_groups),
            'suggested_explorations': self._suggest_explorations(conn, synthesis_groups)
        }
        
        conn.close()
        return synthesis
    
    def find_cross_domain_insights(self, domain1: str, domain2: str) -> Dict:
        """Find insights connecting two different domains"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        
        # Get notes from each domain
        domain1_notes = self._get_domain_notes(conn, domain1)
        domain2_notes = self._get_domain_notes(conn, domain2)
        
        # Find bridge notes (notes that reference both domains)
        bridge_notes = []
        for note in domain1_notes:
            content_lower = note['content'].lower()
            if any(term in content_lower for term in [domain2.lower()] + self._get_related_terms(domain2)):
                bridge_notes.append(note)
        
        # Find conceptual bridges
        domain1_concepts = self._extract_key_concepts(domain1_notes)
        domain2_concepts = self._extract_key_concepts(domain2_notes)
        
        # Find shared concepts
        shared_concepts = set(c[0] for c in domain1_concepts) & set(c[0] for c in domain2_concepts)
        
        insights = {
            'domain1': domain1,
            'domain2': domain2,
            'bridge_notes': [{'title': n['title'], 'path': n['path']} for n in bridge_notes[:5]],
            'shared_concepts': list(shared_concepts)[:10],
            'potential_connections': self._suggest_connections(domain1_concepts, domain2_concepts),
            'synthesis': self._generate_cross_domain_synthesis(domain1, domain2, bridge_notes)
        }
        
        conn.close()
        return insights
    
    def _extract_key_concepts(self, notes: List[Dict]) -> List[Tuple[str, int]]:
        """Extract key concepts from a collection of notes"""
        # Combine all content
        all_content = ' '.join(n['content'] for n in notes).lower()
        
        # Remove common words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'is', 'are', 'was', 'were', 'been', 'being', 'have',
            'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'them', 'their'
        }
        
        # Extract words (alphanumeric, length > 3)
        words = re.findall(r'\b[a-z]{4,}\b', all_content)
        
        # Count frequencies
        word_freq = Counter(word for word in words if word not in stop_words)
        
        # Also extract capitalized terms (likely important concepts)
        capitalized = re.findall(r'\b[A-Z][a-z]+\b', ' '.join(n['content'] for n in notes))
        for term in capitalized:
            word_freq[term.lower()] += 2  # Boost capitalized terms
        
        return word_freq.most_common(20)
    
    def _extract_main_topics(self, notes: List[Dict]) -> List[str]:
        """Extract main topics from notes based on titles and tags"""
        topics = []
        
        # Extract from titles
        title_words = []
        for note in notes:
            title_words.extend(note['title'].lower().split())
        
        # Extract from tags
        all_tags = []
        for note in notes:
            if note['tags']:
                tags = json.loads(note['tags']) if isinstance(note['tags'], str) else note['tags']
                all_tags.extend(tags)
        
        # Combine and count
        topic_counter = Counter(title_words + all_tags)
        
        # Filter out common words and return top topics
        return [topic for topic, count in topic_counter.most_common(10) 
                if len(topic) > 3 and count > 1]
    
    def _find_note_connections(self, conn, note_paths: List[str]) -> List[Dict]:
        """Find connections between a set of notes"""
        connections = []
        
        # Query for links between these notes
        placeholders = ','.join('?' * len(note_paths))
        cursor = conn.execute(f"""
            SELECT l.source_path, l.target_path, 
                   n1.title as source_title, n2.title as target_title
            FROM links l
            JOIN notes n1 ON l.source_path = n1.path
            JOIN notes n2 ON l.target_path = n2.path
            WHERE l.source_path IN ({placeholders}) 
              AND l.target_path IN ({placeholders})
        """, note_paths + note_paths)
        
        for row in cursor:
            connections.append({
                'from': row['source_title'],
                'to': row['target_title'],
                'type': 'direct_link'
            })
        
        return connections[:10]  # Limit to top 10 connections
    
    def _build_synthesis_group(self, conn, seed_note: Dict, used_notes: Set[str]) -> Dict:
        """Build a synthesis group starting from a seed note"""
        group = {
            'theme': seed_note['title'],
            'notes': [seed_note],
            'connections': []
        }
        
        used_notes.add(seed_note['path'])
        
        # Get connected notes
        if seed_note['wikilinks']:
            links = json.loads(seed_note['wikilinks']) if isinstance(seed_note['wikilinks'], str) else seed_note['wikilinks']
            
            for link in links[:3]:  # Limit to 3 connections
                if link in used_notes:
                    continue
                    
                cursor = conn.execute("""
                    SELECT path, title, content, tags
                    FROM notes
                    WHERE title LIKE ? OR path LIKE ?
                    LIMIT 1
                """, (f'%{link}%', f'%{link}%'))
                
                linked_note = cursor.fetchone()
                if linked_note and linked_note['path'] not in used_notes:
                    group['notes'].append(dict(linked_note))
                    used_notes.add(linked_note['path'])
                    group['connections'].append({
                        'from': seed_note['title'],
                        'to': linked_note['title']
                    })
        
        # Extract common theme
        if len(group['notes']) > 1:
            concepts = self._extract_key_concepts(group['notes'])
            if concepts:
                group['theme'] = f"{seed_note['title']} - {concepts[0][0]}"
        
        return group
    
    def _generate_insights(self, conn, synthesis_groups: List[Dict]) -> List[str]:
        """Generate insights from synthesis groups"""
        insights = []
        
        for group in synthesis_groups:
            if len(group['notes']) > 2:
                # Pattern: Multiple notes on same topic
                insights.append(f"You have {len(group['notes'])} interconnected notes about {group['theme']}. Consider creating a summary note.")
            
            # Look for cross-domain connections
            tags_set = set()
            for note in group['notes']:
                if note.get('tags'):
                    tags = json.loads(note['tags']) if isinstance(note['tags'], str) else note['tags']
                    tags_set.update(tags)
            
            if len(tags_set) > 3:
                insights.append(f"The topic '{group['theme']}' spans multiple areas: {', '.join(list(tags_set)[:3])}")
        
        return insights[:5]  # Limit insights
    
    def _suggest_explorations(self, conn, synthesis_groups: List[Dict]) -> List[str]:
        """Suggest areas for further exploration"""
        suggestions = []
        
        # Find gaps in connections
        all_notes = []
        for group in synthesis_groups:
            all_notes.extend(group['notes'])
        
        # Extract all mentioned but non-linked concepts
        mentioned_concepts = set()
        linked_titles = {n['title'].lower() for n in all_notes}
        
        for note in all_notes:
            # Find [[wikilinks]] in content
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', note['content'])
            for link in wikilinks:
                if link.lower() not in linked_titles:
                    mentioned_concepts.add(link)
        
        if mentioned_concepts:
            suggestions.append(f"Consider exploring: {', '.join(list(mentioned_concepts)[:3])}")
        
        # Suggest cross-domain explorations
        domains = defaultdict(int)
        for note in all_notes:
            if note.get('tags'):
                tags = json.loads(note['tags']) if isinstance(note['tags'], str) else note['tags']
                for tag in tags:
                    domains[tag] += 1
        
        if len(domains) > 1:
            top_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)[:2]
            suggestions.append(f"Explore connections between {top_domains[0][0]} and {top_domains[1][0]}")
        
        return suggestions[:3]
    
    def _get_domain_notes(self, conn, domain: str, limit: int = 20) -> List[Dict]:
        """Get notes related to a domain"""
        cursor = conn.execute("""
            SELECT path, title, content, tags
            FROM notes
            WHERE content LIKE ? OR title LIKE ? OR tags LIKE ?
            LIMIT ?
        """, (f'%{domain}%', f'%{domain}%', f'%{domain}%', limit))
        
        return [dict(row) for row in cursor]
    
    def _get_related_terms(self, domain: str) -> List[str]:
        """Get terms related to a domain"""
        related_terms = {
            'ayurveda': ['health', 'wellness', 'medicine', 'dosha', 'vata', 'pitta'],
            'programming': ['code', 'software', 'algorithm', 'function', 'variable'],
            'sanskrit': ['vedic', 'mantra', 'sutra', 'shloka', 'dharma'],
            'cryptography': ['encryption', 'security', 'hash', 'cipher', 'key'],
            'leadership': ['management', 'team', 'vision', 'strategy', 'influence']
        }
        
        return related_terms.get(domain.lower(), [])
    
    def _suggest_connections(self, concepts1: List[Tuple[str, int]], 
                           concepts2: List[Tuple[str, int]]) -> List[str]:
        """Suggest potential connections between two sets of concepts"""
        suggestions = []
        
        # Look for conceptual similarities
        concept_mappings = {
            ('algorithm', 'sutra'): 'Both represent systematic procedures',
            ('encryption', 'mantra'): 'Both involve transformation of information',
            ('function', 'karma'): 'Both represent action-result relationships',
            ('pattern', 'yantra'): 'Both are structured representations',
            ('memory', 'smriti'): 'Both relate to retention and recall'
        }
        
        c1_words = {c[0] for c in concepts1[:10]}
        c2_words = {c[0] for c in concepts2[:10]}
        
        for (word1, word2), connection in concept_mappings.items():
            if word1 in c1_words and word2 in c2_words:
                suggestions.append(connection)
        
        return suggestions[:3]
    
    def _generate_cross_domain_synthesis(self, domain1: str, domain2: str, 
                                       bridge_notes: List[Dict]) -> str:
        """Generate a synthesis connecting two domains"""
        if not bridge_notes:
            return f"No direct connections found between {domain1} and {domain2}. Consider exploring parallel concepts."
        
        return f"Found {len(bridge_notes)} notes connecting {domain1} and {domain2}. " \
               f"Key bridge concept: '{bridge_notes[0]['title']}'. " \
               f"This suggests an interdisciplinary understanding spanning both domains."


def generate_synthesis_report(synthesis: Dict) -> str:
    """Generate a markdown report from synthesis data"""
    report = f"""# Daily Knowledge Synthesis
Generated: {synthesis['date']}

## Discovered Connections

"""
    
    for i, group in enumerate(synthesis['groups'], 1):
        report += f"### {i}. {group['theme']}\n\n"
        report += "**Connected Notes:**\n"
        for note in group['notes']:
            report += f"- {note['title']}\n"
        
        if group['connections']:
            report += "\n**Connections:**\n"
            for conn in group['connections']:
                report += f"- {conn['from']} → {conn['to']}\n"
        report += "\n"
    
    if synthesis['insights']:
        report += "## Insights\n\n"
        for insight in synthesis['insights']:
            report += f"- {insight}\n"
        report += "\n"
    
    if synthesis['suggested_explorations']:
        report += "## Suggested Explorations\n\n"
        for suggestion in synthesis['suggested_explorations']:
            report += f"- {suggestion}\n"
    
    return report


# Command-line interface
if __name__ == "__main__":
    import sys
    
    synthesizer = KnowledgeSynthesizer()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "daily":
            # Generate daily synthesis
            synthesis = synthesizer.generate_daily_synthesis()
            report = generate_synthesis_report(synthesis)
            
            # Save to file with date
            filename = f"synthesis_{datetime.now().strftime('%Y-%m-%d')}.md"
            with open(filename, 'w') as f:
                f.write(report)
            
            print(f"Daily synthesis generated: {filename}")
            print("\nPreview:")
            print(report[:500] + "...")
            
        elif command == "domain" and len(sys.argv) > 2:
            # Generate domain summary
            domain = sys.argv[2]
            summary = synthesizer.generate_domain_summary(domain)
            
            print(f"\nDomain Summary: {domain}")
            print(f"Notes: {summary['note_count']}")
            print(f"Total words: {summary['total_words']}")
            print(f"\nKey concepts: {', '.join(c[0] for c in summary['key_concepts'][:5])}")
            print(f"Main topics: {', '.join(summary['main_topics'][:5])}")
            
        elif command == "connect" and len(sys.argv) > 3:
            # Find cross-domain insights
            domain1 = sys.argv[2]
            domain2 = sys.argv[3]
            insights = synthesizer.find_cross_domain_insights(domain1, domain2)
            
            print(f"\nCross-Domain Insights: {domain1} ↔ {domain2}")
            print(f"\nBridge notes: {len(insights['bridge_notes'])}")
            for note in insights['bridge_notes'][:3]:
                print(f"  - {note['title']}")
            
            print(f"\nShared concepts: {', '.join(insights['shared_concepts'][:5])}")
            print(f"\nSynthesis: {insights['synthesis']}")
            
    else:
        print("Knowledge Synthesis Tool")
        print("\nUsage:")
        print("  python knowledge_synthesis.py daily                    # Generate daily synthesis")
        print("  python knowledge_synthesis.py domain <domain>          # Summarize a domain")
        print("  python knowledge_synthesis.py connect <domain1> <domain2>  # Find cross-domain insights")
        print("\nExamples:")
        print("  python knowledge_synthesis.py daily")
        print("  python knowledge_synthesis.py domain ayurveda")
        print("  python knowledge_synthesis.py connect sanskrit programming")