# screensaver-pm

I screensaver-pm be my pm, by using my screensaver to be reminded of what I should be doing.

Display your PROJECTS.md as a macOS screensaver using WebViewScreenSaver.

## Setup

### 1. Install dependencies

```bash
brew install --cask webviewscreensaver
```

### 2. Link your PROJECTS.md

```bash
# Symlink (recommended - auto-updates)
ln -s /path/to/your/PROJECTS.md /path/to/screensaver-pm/PROJECTS.md
```

### 3. Convert to HTML

```bash
cd /path/to/screensaver-pm
python3 convert.py
```

### 4. Configure screensaver

1. Open **System Settings → Screen Saver**
2. Select **WebViewScreenSaver**
3. Click **Options...**
4. Enter URL:
   ```
   file:///path/to/screensaver-pm/PROJECTS.html
   ```

#### URL Parameters

| Param | Default | Description |
|-------|---------|-------------|
| `auto` | `true` | Auto-advance slides (`false` to disable) |
| `interval` | `8000` | Slide duration in ms (e.g., `10000` for 10s) |

**Examples:**
- Auto slideshow: `PROJECTS.html`
- Manual navigation: `PROJECTS.html?auto=false`
- Slower slides: `PROJECTS.html?interval=12000`

## PROJECTS.md Format

Use pipe-delimited format for each project:

```markdown
## Ship Now

Projects ready for release.

- **project-name** | Type | Description text | Next action | https://github.com/user/repo
```

Sections: `Ship Now`, `Active Development`, `On Hold`, `Future`

## Files

- `PROJECTS.md` - Your actual project dashboard (gitignored, local only)
- `PROJECTS.sample.md` - Example file (Godzilla's busy schedule)
- `PROJECTS.html` - Generated slideshow (gitignored)
- `convert.py` - Python script to generate HTML

## Features

- **Reveal.js slideshow**: Smooth transitions, auto-advance, keyboard navigation
- **4 color-coded slides**: Ship Now (green), Active (blue), On Hold (yellow), Future (purple)
- **Auto-refreshes** every 60 seconds
- **Keyboard navigation**: Arrow keys, space bar
