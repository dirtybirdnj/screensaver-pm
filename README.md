# screensaver-pm

I screensaver-pm be my pm, by using my screensaver to be reminded of what I should be doing.

Display your PROJECTS.md as a macOS screensaver using WebViewScreenSaver.

## Setup

### 1. Install dependencies

```bash
brew install pandoc
brew install --cask webviewscreensaver
```

### 2. Link your PROJECTS.md

```bash
# Option A: Symlink (recommended - auto-updates)
ln -s /Users/mgilbert/Code/PROJECTS.md /Users/mgilbert/Code/screensaver-pm/PROJECTS.md

# Option B: Copy manually when needed
cp /path/to/your/PROJECTS.md /Users/mgilbert/Code/screensaver-pm/PROJECTS.md
```

### 3. Convert to HTML

```bash
cd /Users/mgilbert/Code/screensaver-pm
chmod +x convert.sh
./convert.sh
```

### 4. Configure screensaver

1. Open **System Preferences → Desktop & Screen Saver → Screen Saver**
2. Select **WebViewScreenSaver**
3. Click **Screen Saver Options...**
4. Enter URL: `file:///Users/mgilbert/Code/screensaver-pm/PROJECTS.html`

### 5. Auto-convert on file change (optional)

Using `fswatch` to auto-regenerate HTML when PROJECTS.md changes:

```bash
brew install fswatch

# Run in background
fswatch -o /Users/mgilbert/Code/PROJECTS.md | xargs -n1 /Users/mgilbert/Code/screensaver-pm/convert.sh &
```

Or add to your shell startup for always-on monitoring.

## Files

- `PROJECTS.md` - Your actual project dashboard (gitignored, local only)
- `PROJECTS.sample.md` - Example file (Godzilla's busy schedule)
- `PROJECTS.html` - Generated output for screensaver (gitignored)
- `convert.sh` - Markdown → HTML converter
- `template.html` - Dark theme template with auto-refresh

## Features

- GitHub dark theme styling
- Auto-refreshes every 60 seconds
- Large, readable fonts for screensaver viewing
- Subtle fade-in animation
