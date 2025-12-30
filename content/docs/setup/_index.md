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

- **Node.js** (v18+)
- **Hugo Extended** (v0.110+)
- **Git**
- **Python** 3.8+ (for API testing)

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

## Step 2: Hugo Site Setup

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

### Run Development Server

```bash
hugo server
```

Visit `http://localhost:1313` to view the documentation site.

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

## Step 3: Evidence Analytics Setup

### Install Evidence Dependencies

```bash
cd evidence
npm install
cd ..
```

### Build Analytics Data Pipeline

```bash
# Install Python dependencies
pip install requests duckdb

# Fetch FDA drug data
python fetch_drug_data.py

# Load data into DuckDB
python load_to_duckdb.py
```

### Run Evidence Dev Server

```bash
cd evidence
npm run dev
# Opens at http://localhost:3000
```

### Build Evidence for Production

```bash
cd evidence
npm run sources  # Process data sources
npm run build    # Build static site
cd ..

# Sync to Hugo static directory
rsync -av --delete evidence/build/ static/analytics/
```

## Step 4: Build Complete Site

### Build Hugo Site

```bash
# Build Hugo site with embedded Evidence analytics
hugo

# Preview production build
hugo server
```

### Automated Build Script

Use the convenience script to rebuild everything:

```bash
chmod +x build-analytics.sh
./build-analytics.sh
```

## Step 5: Flowise AI Setup (Coming Soon)

- Install Flowise locally or use Flowise Cloud
- Configure healthcare data workflows
- Connect to FDA and pricing APIs
- Embed chat interface in Hugo site

## Project Structure

```
HealthScope-AI/
├── content/                    # Hugo content
│   └── docs/                   # Documentation pages
│       ├── analytics/          # Analytics documentation
│       ├── drug-data/          # Drug data docs
│       ├── flowise/            # Flowise integration docs
│       └── setup/              # Setup guides
│
├── evidence/                   # Evidence.dev analytics project
│   ├── pages/                  # Evidence markdown pages
│   │   ├── index.md            # Analytics home
│   │   └── fda-drugs.md        # FDA drug dashboard
│   ├── sources/                # Data source connections
│   │   ├── fda_data/           # FDA data source
│   │   │   ├── connection.yaml # CSV connection config
│   │   │   ├── fda_drugs.csv   # Drug data CSV
│   │   │   └── healthcare.duckdb # DuckDB database
│   ├── build/                  # Built Evidence site (gitignored)
│   ├── node_modules/           # Evidence dependencies (gitignored)
│   ├── package.json            # Evidence dependencies
│   └── evidence.config.yaml   # Evidence configuration
│
├── static/                     # Hugo static files
│   └── analytics/              # Built Evidence dashboard (synced from evidence/build)
│
├── layouts/                    # Custom Hugo layouts
│   └── shortcodes/             # Custom Hugo shortcodes
│       ├── evidence-dashboard.html
│       ├── drug-table.html
│       └── flowise.html
│
├── data/                       # Hugo data files (Evidence exports)
│   ├── fda_data/               # FDA drug data (parquet)
│   └── manifest.json           # Data manifest
│
├── fetch_drug_data.py          # FDA API data fetcher
├── load_to_duckdb.py           # DuckDB data loader
├── build-analytics.sh          # Automated build script
├── export-charts.js            # Chart export utility
├── fda_drug_data.json          # Downloaded FDA data
│
├── hugo.toml                   # Hugo configuration
├── package.json                # Node.js dependencies (Hugo)
└── README.md                   # Project documentation
```

## API Integration

### FDA OpenAPI

- **Endpoint**: `https://api.fda.gov/drug/`
- **Authentication**: None required
- **Rate Limits**: 240 requests per minute, 1000 per hour
- **Documentation**: https://open.fda.gov/apis/

### Drug Pricing APIs

- **GoodRx API**: Free tier (1000 calls/month)
- **Pharmacy Websites**: Web scraping for price comparison
- **Medicare Data**: Public pricing databases

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

## Learning Objectives

This project focuses on:

- **Healthcare Data Integration**: Working with FDA and pricing APIs
- **Data Pipeline Development**: Python-based ETL for healthcare data
- **Analytics & BI**: SQL-based data analysis with Evidence.dev
- **Embedded Databases**: Using DuckDB for analytical workloads
- **No-Code AI Development**: Using Flowise for conversational interfaces
- **Documentation Best Practices**: Professional Hugo site with Docsy
- **Static Site Generation**: Building fast, secure documentation sites
- **Compliance Awareness**: Healthcare data handling and disclaimers

## Next Steps

Once setup is complete:

1. **Explore Documentation**: Review all sections of the site
2. **Test API Integrations**: Verify FDA and pricing API access
3. **Plan Flowise Integration**: Prepare for conversational AI setup
4. **Customize Content**: Adapt documentation to your needs

---

**Setup complete!** You now have a fully functional HealthScope AI documentation site with integrated analytics ready for development.
