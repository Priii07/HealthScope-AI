---
title: "Setup Guide"
linkTitle: "Setup"
weight: 30
description: "Complete setup instructions for HealthScope AI development environment"
---

# HealthScope AI Setup Guide

This guide walks you through setting up the complete HealthScope AI development environment, including Hugo documentation site, Docsy theme, and API integrations.

## Prerequisites

Before starting, ensure you have:

- **Node.js** (v18 or higher)
- **Hugo Extended** (v0.110 or higher)
- **Git** (latest version)
- **Python** 3.8+ (for API testing)
- **Code Editor** (VS Code recommended)

## Step 1: Environment Setup

### Install Hugo Extended

{{< tabpane >}}
{{< tab header="macOS" >}}
```bash
# Using Homebrew
brew install hugo

# Verify installation
hugo version
```
{{< /tab >}}
{{< tab header="Windows" >}}
```bash
# Using Chocolatey
choco install hugo-extended

# Or download from GitHub releases
# https://github.com/gohugoio/hugo/releases
```
{{< /tab >}}
{{< tab header="Linux" >}}
```bash
# Using Snap
snap install hugo --channel=extended

# Or download binary from GitHub releases
```
{{< /tab >}}
{{< /tabpane >}}

### Install Node.js

Download and install from [nodejs.org](https://nodejs.org/) or use a package manager:

```bash
# Verify installation
node --version
npm --version
```

## Step 2: Project Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/HealthScope-AI.git
cd HealthScope-AI
```

### Initialize Hugo Modules

```bash
# Initialize Hugo modules for dependency management
hugo mod init github.com/yourusername/HealthScope-AI
```

### Install Docsy Theme

```bash
# Add Docsy theme as Hugo module
hugo mod get github.com/google/docsy@v0.7.1
hugo mod get github.com/google/docsy/dependencies@v0.7.1
```

### Install Node Dependencies

```bash
# Install required Node.js packages for Docsy
npm install
```

## Step 3: Configuration

### Hugo Configuration

The `hugo.toml` file contains the main site configuration:

```toml
baseURL = 'http://localhost:1313/'
languageCode = 'en-us'
title = 'HealthScope AI'

[module]
  proxy = "direct"
  [[module.imports]]
    path = "github.com/google/docsy"
    disable = false
  [[module.imports]]
    path = "github.com/google/docsy/dependencies"
    disable = false

[params]
  github_repo = 'https://github.com/yourusername/HealthScope-AI'
  github_branch = 'main'
  
  # Healthcare-focused styling
  navbar_logo = false
  offlineSearch = true
  prism_syntax_highlighting = true

[params.ui]
  breadcrumb_disable = false
  sidebar_search_disable = false
  navbar_logo = false
  footer_about_disable = false

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.highlight]
    style = "github"
    lineNos = true

# Navigation menu
[menu]
  [[menu.main]]
    name = "Documentation"
    url = "/docs/"
    weight = 10
  [[menu.main]]
    name = "Setup Guide"
    url = "/docs/setup/"
    weight = 20
```

### Custom Styling

The custom healthcare styling is in `assets/scss/_variables_project.scss`:

```scss
// Healthcare-focused color palette
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

$google_font_name: "Inter";
$google_font_family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

// Professional healthcare colors
$primary: #1e40af;    // Muted professional blue
$secondary: #64748b;  // Neutral gray
$success: #059669;    // Healthcare green
$info: #0f766e;       // Muted teal
$warning: #d97706;    // Orange
$danger: #dc2626;     // Red
```

## Step 4: Development Server

### Start Hugo Server

```bash
# Start development server with live reload
hugo server

# Or with drafts and future content
hugo server -D -F
```

Visit `http://localhost:1313` to view your site.

### Development Workflow

1. **Edit Content**: Modify files in `content/` directory
2. **Auto Reload**: Hugo automatically rebuilds and refreshes browser
3. **Check Console**: Monitor for build errors or warnings
4. **Test Locally**: Verify all features work before deployment

## Step 5: API Testing

### Python Environment

```bash
# Install required Python packages
pip install requests json

# Or create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install requests
```

### Test FDA API

```bash
# Run FDA API test
python test_fda.py
```

Expected output:
```
🧪 Testing FDA API...
✅ FDA API works!
📊 Found drug data
Brand: Lipitor
Generic: atorvastatin
```

### Test Pricing Structure

```bash
# Run pricing data test
python test_pricing.py
```

This creates sample pricing data structure for development.

## Step 6: Content Structure

### Understanding the Layout

```
content/
├── _index.html          # Homepage (HTML template)
├── docs/
│   ├── _index.md        # Main documentation
│   ├── setup/           # This setup guide
│   └── api/             # API documentation (future)
```

### Adding New Content

```bash
# Create new documentation page
hugo new docs/new-page/_index.md

# Create new blog post
hugo new blog/my-post.md
```

## Step 7: Customization

### Modify Homepage

Edit `content/_index.html` to customize:
- Hero section messaging
- Feature blocks
- Call-to-action buttons
- Healthcare disclaimers

### Update Navigation

Modify `hugo.toml` menu section to add/remove navigation items.

### Custom CSS

Add custom styles to `assets/scss/_variables_project.scss` or create new SCSS files.

## Step 8: Deployment Preparation

### Build Static Site

```bash
# Build production site
hugo

# Output will be in public/ directory
```

### GitHub Pages Setup

1. Create GitHub repository
2. Push code to `main` branch
3. Enable GitHub Pages in repository settings
4. Choose source: GitHub Actions or `docs/` folder

## Troubleshooting

### Common Issues

**Hugo Module Errors**:
```bash
# Clear module cache
hugo mod clean
hugo mod get -u
```

**Node Package Issues**:
```bash
# Clear npm cache
npm cache clean --force
rm -rf node_modules
npm install
```

**Build Errors**:
- Check Hugo version (must be Extended)
- Verify all required files are present
- Check for syntax errors in configuration

### Getting Help

- **Hugo Documentation**: https://gohugo.io/documentation/
- **Docsy Theme Docs**: https://www.docsy.dev/docs/
- **GitHub Issues**: Report problems in project repository

## Next Steps

Once setup is complete:

1. **Explore Documentation**: Review all sections of the site
2. **Test API Integrations**: Verify FDA and pricing API access
3. **Plan Flowise Integration**: Prepare for conversational AI setup
4. **Customize Content**: Adapt documentation to your needs

---

**Setup complete!** You now have a fully functional HealthScope AI documentation site ready for development.
