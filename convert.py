#!/usr/bin/env python3
"""
Convert PROJECTS.md to a reveal.js slideshow HTML file.
Format: - **name** | type | description | action | url
"""

import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "PROJECTS.md")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "PROJECTS.html")

def parse_projects(md_content):
    """Parse markdown into sections with projects."""
    sections = []
    current_section = None
    current_subtitle = None

    for line in md_content.split('\n'):
        # Section header
        if line.startswith('## '):
            title = line[3:].strip()
            # Skip Notes section
            if title == 'Notes':
                break
            current_section = {
                'title': title,
                'subtitle': '',
                'projects': []
            }
            sections.append(current_section)
        # Subtitle (first non-empty line after header)
        elif current_section and not current_section['subtitle'] and line.strip() and not line.startswith('-'):
            current_section['subtitle'] = line.strip()
        # Project line
        elif current_section and line.startswith('- **'):
            match = re.match(r'- \*\*(.+?)\*\* \| (.+?) \| (.+?) \| (.+?) \| (.+)', line)
            if match:
                current_section['projects'].append({
                    'name': match.group(1),
                    'type': match.group(2),
                    'description': match.group(3),
                    'action': match.group(4),
                    'url': match.group(5)
                })

    return sections

def generate_slide_html(section, color):
    """Generate HTML for a single slide."""
    projects_html = ''
    for p in section['projects']:
        projects_html += f'''
            <div class="project-card">
                <h3>
                    <a href="{p['url']}" target="_blank">{p['name']}</a>
                    <span class="type-badge">{p['type']}</span>
                </h3>
                <p class="description">{p['description']}</p>
                <p class="action"><span class="label">Next:</span> {p['action']}</p>
            </div>
'''

    return f'''
        <section data-background-color="{color}">
            <h2>{section['title']}</h2>
            <p class="subtitle">{section['subtitle']}</p>
            <div class="projects">
                {projects_html}
            </div>
        </section>
'''

def generate_html(sections):
    """Generate complete HTML document."""

    colors = {
        'Ship Now': '#1a4d1a',
        'Active Development': '#1a3d5c',
        'On Hold': '#5c4a1a',
        'Future': '#3d1a5c'
    }

    slides_html = ''
    for section in sections:
        color = colors.get(section['title'], '#1a1a2e')
        slides_html += generate_slide_html(section, color)

    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css">
    <style>
        /* ==========================================
           FONT SIZE REFERENCE - adjust these values
           Base: 20px, everything scales from here
           ========================================== */
        .reveal {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 20px;  /* BASE FONT SIZE */
        }}

        /* Slide title */
        .reveal h2 {{
            font-size: 1.8em;  /* ~36px */
            margin-bottom: 0.2em;
            text-transform: none;
        }}

        /* Subtitle under title */
        .reveal .subtitle {{
            font-size: 0.85em;  /* ~17px */
            opacity: 0.7;
            margin-bottom: 0.8em;
        }}

        /* Project cards container */
        .reveal .projects {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 900px;
            margin: 0 auto;
        }}

        /* Individual project card */
        .reveal .project-card {{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 6px;
            padding: 12px 18px;
            text-align: left;
        }}

        /* Project name */
        .reveal .project-card h3 {{
            margin: 0 0 6px 0;
            font-size: 1.05em;  /* ~21px */
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .reveal .project-card h3 a {{
            color: #58a6ff;
            text-decoration: none;
        }}

        /* Type badge (Electron, Game, etc) */
        .reveal .type-badge {{
            font-size: 0.7em;  /* ~14px */
            background: rgba(255, 255, 255, 0.15);
            padding: 3px 10px;
            border-radius: 10px;
            font-weight: normal;
        }}

        /* Project description */
        .reveal .project-card .description {{
            margin: 0 0 6px 0;
            font-size: 0.9em;  /* ~18px */
            opacity: 0.9;
            line-height: 1.4;
        }}

        /* Next action / status */
        .reveal .project-card .action {{
            margin: 0;
            font-size: 0.8em;  /* ~16px */
            opacity: 0.7;
        }}

        .reveal .project-card .action .label {{
            color: #3fb950;
        }}

        /* Progress bar at bottom */
        .reveal .progress {{
            height: 3px;
        }}

        /* Fade transition timing - 3 seconds for smooth effect */
        .reveal .slides section {{
            transition: opacity 3s ease-in-out;
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{slides_html}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
    <script>
        var defined = new URLSearchParams(window.location.search);
        var auto = defined.get('auto') !== 'false';
        var interval = parseInt(defined.get('interval')) || 8000;

        Reveal.initialize({{
            hash: false,
            loop: true,
            autoSlide: auto ? interval : 0,
            transition: 'fade',
            transitionSpeed: 'slow',
            controls: true,
            progress: true,
            center: true
        }});

        // Override transition duration (3 seconds)
        document.documentElement.style.setProperty('--r-transition-duration', '3s');

        // Auto-refresh every 60 seconds
        setTimeout(function() {{ location.reload(); }}, 60000);
    </script>
</body>
</html>
'''

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found")
        print("Create a symlink: ln -s /path/to/PROJECTS.md", INPUT_FILE)
        return 1

    with open(INPUT_FILE, 'r') as f:
        md_content = f.read()

    sections = parse_projects(md_content)
    html = generate_html(sections)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(html)

    print(f"Generated: {OUTPUT_FILE}")
    print(f"Sections: {[s['title'] for s in sections]}")
    return 0

if __name__ == '__main__':
    exit(main())
