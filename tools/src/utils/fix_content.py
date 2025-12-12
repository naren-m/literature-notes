#!/usr/bin/env python3
"""
Fix content issues for Jekyll/GitHub Pages compatibility
"""

import os
import re
from pathlib import Path


def fix_yaml_frontmatter(content):
    """Fix YAML frontmatter issues."""
    lines = content.split('\n')
    
    # Fix the f*ck issue in title
    for i, line in enumerate(lines):
        if line.startswith('title:') and 'F\\*ck' in line:
            # Escape the backslash properly for YAML
            lines[i] = line.replace('F\\*ck', 'F*ck')
        elif line.startswith('title:') and 'F*ck' in line:
            # Quote the title properly
            title_content = line.split('title:', 1)[1].strip()
            if not (title_content.startswith('"') and title_content.endswith('"')):
                lines[i] = f'title: "{title_content}"'
    
    return '\n'.join(lines)


def fix_liquid_syntax(content):
    """Fix Liquid template syntax issues."""
    # Fix {{video ...}} syntax - escape it as text
    content = re.sub(r'\{\{video\s+([^}]+)\}\}', r'`{{video \1}}`', content)
    
    # Fix {{youtube-timestamp ...}} syntax
    content = re.sub(r'\{\{youtube-timestamp\s+(\d+)\}\}', r'`{{youtube-timestamp \1}}`', content)
    
    # Fix {{embed ...}} syntax 
    content = re.sub(r'\{\{embed([^}]*)\}\}', r'`{{embed\1}}`', content)
    
    # Fix any unclosed {{ variables
    content = re.sub(r'\{\{([^}]*(?!\}\}))', r'`{{\1`', content)
    
    return content


def fix_control_characters(content):
    """Remove control characters that YAML doesn't like."""
    # Remove null bytes and other control characters
    content = ''.join(char for char in content if ord(char) >= 32 or char in '\t\n\r')
    return content


def process_file(file_path):
    """Process a single file to fix issues."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Apply fixes
        content = fix_control_characters(content)
        content = fix_yaml_frontmatter(content)
        content = fix_liquid_syntax(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Fix all markdown files."""
    root_dir = Path('.')
    fixed_count = 0
    total_count = 0
    
    # Find all markdown files
    for md_file in root_dir.rglob('*.md'):
        # Skip files in docs directory (duplicates)
        if 'docs/' in str(md_file):
            continue
            
        total_count += 1
        if process_file(md_file):
            fixed_count += 1
        
        if total_count % 100 == 0:
            print(f"Processed {total_count} files...")
    
    print(f"✅ Processed {total_count} files, fixed {fixed_count}")


if __name__ == "__main__":
    main()