# HealthScope AI

**Drug Price & FDA Data Research Platform**

A healthcare information research platform that combines drug pricing data with FDA safety information, powered by Flowise AI for conversational queries.

## 🎯 Mission

Make healthcare data accessible through intelligent research tools that combine drug pricing transparency with FDA safety information for educational purposes.

*Always consult your healthcare provider for medical decisions.*

## 🚀 Features

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
Hugo Documentation Site ←→ Flowise AI Chat Interface
                              ↓
                         FDA OpenAPI + Pricing APIs
```

- **Documentation Hub** (Hugo + Docsy): Project info, research guides, setup instructions
- **Conversational AI** (Flowise): Chat interface for drug research queries
- **Data Sources**: FDA OpenAPI (free) + drug pricing APIs

## 🛠️ Technology Stack

- **Frontend**: Hugo static site with Docsy theme
- **AI Interface**: Flowise AI for conversational queries
- **APIs**: FDA OpenAPI, GoodRx API, pharmacy pricing sources
- **Deployment**: GitHub Pages (docs) + Flowise Cloud/Self-hosted

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

### 3. Test FDA API Access
```bash
# Install Python dependencies
pip install requests

# Test FDA API connection
python test_fda.py
```

### 4. Flowise AI Setup (Coming Soon)
- Install Flowise locally or use Flowise Cloud
- Configure healthcare data workflows
- Connect to FDA and pricing APIs
- Embed chat interface in Hugo site

## 📁 Project Structure

```
HealthScope-AI/
├── content/                 # Hugo content
│   ├── docs/               # Documentation pages
│   ├── project-plan/       # Development roadmap
│   └── _index.html         # Homepage
├── assets/                 # Custom CSS/SCSS
├── static/                 # Static files
├── test_fda.py            # FDA API testing script
├── test_pricing.py        # Pricing data testing script
├── sample_pricing.json    # Sample pricing data structure
├── hugo.toml              # Hugo configuration
└── README.md              # This file
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
- **No-Code AI Development**: Using Flowise for conversational interfaces
- **Documentation Best Practices**: Professional Hugo site with Docsy
- **API Design**: RESTful endpoints for healthcare data
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
