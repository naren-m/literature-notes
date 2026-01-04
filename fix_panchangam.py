import re
import sys

file_path = 'pages/UNDERSTANDING_PANCHANGAM.md'

def fix_file():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    new_lines = []
    dedent_mode = False

    for line in lines:
        original_line = line
        
        # Check for Logseq bullet
        is_bullet = line.startswith('- ')
        
        # Also check for lines that are just "-" or "- " and nothing else
        if line.strip() == '-':
            # This is an empty bullet that wasn't caught by startswith('- ') if it has no space
            # or it's just a dash.
            # Convert to empty line (or remove it? Empty line is safer for spacing)
            line = '\n'
            new_lines.append(line)
            continue
            
        content = line[2:] if is_bullet else line
        
        strip_bullet = False
        
        if is_bullet:
            # Check if it's a structural element we want to debullet
            # Headers, Images, Code blocks, Empty lines
            stripped_content = content.lstrip()
            if (stripped_content.startswith('#') or 
                stripped_content.startswith('![') or 
                stripped_content.startswith('```') or 
                content.strip() == ''):
                
                strip_bullet = True
                dedent_mode = True
                line = content # Remove the '- ' prefix
            else:
                # It's a regular list item (likely). Keep the bullet.
                # Stop dedenting because we are now in a new structure
                dedent_mode = False
        else:
            # Not a bullet line. 
            # If we are in dedent_mode (following a header/structure), remove indentation
            if dedent_mode:
                if line.startswith('  '):
                    line = line[2:]
                # If line doesn't start with 2 spaces, it's either empty or weirdly formatted.
                # Just keep it as is (dedent 0 spaces).
        
        # Image transformation
        # Pattern: ![alt](assets/url) -> <img src="../assets/url" alt="alt" width="100%" />
        # We need to handle cases where url might already be relative or absolute?
        # The file has `(assets/...)`.
        
        def img_repl(match):
            alt = match.group(1)
            url = match.group(2)
            
            # Fix path if it starts with assets/
            if url.startswith('assets/'):
                url = '../' + url
            
            return f'<img src="{url}" alt="{alt}" width="100%" />'
        
        # Regex for markdown image
        # Note: We replaced `![` in the bullet check, but the line string still contains it.
        # So we just regex replace on the modified line.
        line = re.sub(r'!\[(.*?)\]\((.*?)\)', img_repl, line)
        
        new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Successfully processed {file_path}")

if __name__ == '__main__':
    fix_file()
