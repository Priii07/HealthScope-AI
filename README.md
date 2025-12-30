# HealthScope AI

**Drug Price & FDA Data Research Platform**

A healthcare information research platform that combines drug pricing data with FDA safety information, powered by Flowise AI for conversational queries.

## 🎯 Mission

Make healthcare data accessible through intelligent research tools that combine drug pricing transparency with FDA safety information for educational purposes.

*Always consult your healthcare provider for medical decisions.*

## 🚀 Features

### Interactive Analytics Dashboard (Evidence.dev)
- SQL-based data exploration and visualization
- Real-time drug data analysis with interactive charts
- Manufacturer distribution and route analysis
- Embedded analytics within documentation site

### Drug Price Research
- Compare medication prices across pharmacies
- Find generic alternatives and cost differences
- Research pricing trends and variations

### FDA Safety Data Access
- Access FDA adverse event reports (FAERS database)
- View drug recalls and safety communications
- Research drug safety profiles

### Conversational Interface (Flowise AI)
- Natural language queries: "What's the price of metformin in NYC?"
- Combined research: "Show me pricing and safety info for Lipitor"
- Educational summaries and comparisons

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│           Hugo Documentation Site (GitHub Pages)         │
│                                                          │
│  ┌────────────────┐         ┌──────────────────────┐   │
│  │  Documentation │         │  Evidence Analytics  │   │
│  │     Pages      │◄────────┤    Dashboard         │   │
│  │   (Docsy)      │         │  (/analytics/)       │   │
│  └────────────────┘         └──────────────────────┘   │
│                                       ▲                  │
│                                       │                  │
└───────────────────────────────────────┼──────────────────┘
                                        │
                    ┌───────────────────┴───────────────────┐
                    │       Data Pipeline (Python)          │
                    │                                       │
                    │  ┌─────────────┐    ┌─────────────┐ │
                    │  │ FDA API     │───▶│  DuckDB     │ │
                    │  │ fetch_drug_ │    │  Database   │ │
                    │  │ data.py     │    │             │ │
                    │  └─────────────┘    └─────────────┘ │
                    │                            │         │
                    │                            ▼         │
                    │                     ┌─────────────┐ │
                    │                     │  Evidence   │ │
                    │                     │  Sources    │ │
                    │                     └─────────────┘ │
                    └───────────────────────────────────────┘
                                        ▲
                                        │
                    ┌───────────────────┴───────────────────┐
                    │         External Data Sources         │
                    │                                       │
                    │  • FDA OpenFDA API (drug labels)     │
                    │  • Drug Pricing APIs (planned)       │
                    │  • Flowise AI (planned)              │
                    └───────────────────────────────────────┘
```

### Components:

- **Documentation Hub** (Hugo + Docsy): Project info, research guides, setup instructions
- **Analytics Layer** (Evidence.dev): SQL-based BI tool for interactive data visualization
- **Data Pipeline** (Python): Automated FDA data fetching and DuckDB database management
- **Data Storage** (DuckDB): Embedded analytics database for fast queries
- **Conversational AI** (Flowise): Chat interface for drug research queries (planned)
- **Data Sources**: FDA OpenAPI (free) + drug pricing APIs (planned)

## 🛠️ Technology Stack

### Documentation & Frontend
- **Hugo Extended** (v0.110+): Static site generator
- **Docsy Theme**: Professional documentation theme
- **GitHub Pages**: Static site hosting

### Analytics & Visualization
- **Evidence.dev**: SQL-based BI and data visualization framework
- **DuckDB**: Embedded analytical database (OLAP)
- **Parquet**: Columnar data storage format

### Data Pipeline
- **Python 3.8+**: Data fetching and processing
- **FDA OpenFDA API**: Drug label and safety data source
- **JSON/CSV**: Data interchange formats

### Planned Integrations
- **Flowise AI**: Conversational interface for natural language queries
- **GoodRx API**: Drug pricing data source
- **Pharmacy APIs**: Price comparison sources

## 📋 Setup Instructions

### Prerequisites
- Node.js (v18+)
- Hugo Extended (v0.110+)
- Git
- Python 3.8+ (for API testing)

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/HealthScope-AI.git
cd HealthScope-AI
```

### 2. Hugo Site Setup

#### Install Hugo Extended
```bash
# macOS
brew install hugo

# Windows
choco install hugo-extended

# Linux
snap install hugo --channel=extended
```

#### Install Docsy Theme
```bash
# Initialize Hugo modules
hugo mod init github.com/yourusername/HealthScope-AI

# Install Docsy theme
hugo mod get github.com/google/docsy@v0.7.1
hugo mod get github.com/google/docsy/dependencies@v0.7.1
```

#### Install Node Dependencies
```bash
npm install
```

#### Run Development Server
```bash
hugo server
```

Visit `http://localhost:1313` to view the documentation site.

### 3. Evidence Analytics Setup

#### Install Evidence Dependencies
```bash
cd evidence
npm install
cd ..
```

#### Build Analytics Data Pipeline
```bash
# Install Python dependencies
pip install requests duckdb

# Fetch FDA drug data
python fetch_drug_data.py

# Load data into DuckDB
python load_to_duckdb.py
```

#### Run Evidence Dev Server
```bash
cd evidence
npm run dev
# Opens at http://localhost:3000
```

#### Build Evidence for Production
```bash
cd evidence
npm run sources  # Process data sources
npm run build    # Build static site
cd ..

# Sync to Hugo static directory
rsync -av --delete evidence/build/ static/analytics/
```

### 4. Build Complete Site
```bash
# Build Hugo site with embedded Evidence analytics
hugo

# Preview production build
hugo server
```

### 5. Automated Build Script
Use the convenience script to rebuild everything:
```bash
chmod +x build-analytics.sh
./build-analytics.sh
```

### 6. Flowise AI Setup (Coming Soon)
- Install Flowise locally or use Flowise Cloud
- Configure healthcare data workflows
- Connect to FDA and pricing APIs
- Embed chat interface in Hugo site

## 📁 Project Structure

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
└── README.md                   # This file
```

## 🔌 API Integration

### FDA OpenAPI
- **Endpoint**: `https://api.fda.gov/drug/`
- **Authentication**: None required
- **Rate Limits**: 240 requests per minute, 1000 per hour
- **Documentation**: https://open.fda.gov/apis/

### Drug Pricing APIs
- **GoodRx API**: Free tier (1000 calls/month)
- **Pharmacy Websites**: Web scraping for price comparison
- **Medicare Data**: Public pricing databases

## 🎓 Learning Objectives

This project focuses on:
- **Healthcare Data Integration**: Working with FDA and pricing APIs
- **Data Pipeline Development**: Python-based ETL for healthcare data
- **Analytics & BI**: SQL-based data analysis with Evidence.dev
- **Embedded Databases**: Using DuckDB for analytical workloads
- **No-Code AI Development**: Using Flowise for conversational interfaces
- **Documentation Best Practices**: Professional Hugo site with Docsy
- **Static Site Generation**: Building fast, secure documentation sites
- **Compliance Awareness**: Healthcare data handling and disclaimers


## ⚠️ Important Disclaimers

- **Educational Purpose**: This platform is for research and educational use only
- **Not Medical Advice**: Always consult qualified healthcare professionals for medical decisions
- **Data Accuracy**: Information accuracy depends on source databases
- **Privacy**: No personal health information is collected or stored

## 📄 License

MIT License - Built for learning and community benefit.

## 🔗 Links

- **Documentation**: [GitHub Pages Site]
- **FDA OpenAPI**: https://open.fda.gov/apis/
- **Flowise AI**: https://flowiseai.com/
- **Hugo Docsy Theme**: https://www.docsy.dev/

---

**Ready to research drug pricing and FDA safety data with AI?**
