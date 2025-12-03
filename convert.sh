#!/bin/bash
# Convert PROJECTS.md to styled HTML for screensaver display

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT="$SCRIPT_DIR/PROJECTS.md"
OUTPUT="$SCRIPT_DIR/PROJECTS.html"

# Check if PROJECTS.md exists
if [ ! -f "$INPUT" ]; then
    echo "Error: PROJECTS.md not found at $INPUT"
    echo "Copy your PROJECTS.md file here or create a symlink:"
    echo "  ln -s /Users/mgilbert/Code/PROJECTS.md $INPUT"
    exit 1
fi

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc not installed. Run: brew install pandoc"
    exit 1
fi

# Convert with GitHub-style CSS embedded
pandoc "$INPUT" \
    --standalone \
    --metadata title="Project Dashboard" \
    --css="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-dark.min.css" \
    --template="$SCRIPT_DIR/template.html" \
    -o "$OUTPUT"

echo "Converted: $OUTPUT"
echo "Last updated: $(date)"
