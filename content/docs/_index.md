---
title: "HealthScope AI Platform"
linkTitle: "Documentation"
weight: 20
menu:
  main:
    weight: 20
---

## Overview

HealthScope AI is a drug price and FDA data research platform that helps users access medication pricing information alongside FDA safety data for educational purposes.

<!-- **Target Users**: Patients, caregivers, researchers seeking to compare drug prices and access FDA safety information -->
## Core Research Areas

### 1. Drug Price Research
**Purpose**: Compare medication pricing across different sources
**Features**: 
- Pharmacy price comparisons
- Generic alternative identification
- Cost difference analysis
**Data Sources**: GoodRx API, pharmacy websites, public pricing databases

### 2. FDA Safety Data Access
**Purpose**: Access official FDA safety information
**Features**:
- Adverse event reports (FAERS database)
- Drug recall notifications
- FDA safety communications
**Data Sources**: FDA OpenAPI, official FDA databases

### 3. Combined Research
**Purpose**: Search both pricing and safety data together
**Features**:
- Natural language queries across both data types
- Comprehensive medication information compilation
- Educational research summaries

## Architecture

### System Overview

```plantuml
@startuml
!theme plain

actor User
participant "Hugo Docs" as Docs
participant "Evidence Analytics" as Evidence
database "DuckDB" as DuckDB
participant "Flowise AI" as Flowise
participant "FDA OpenAPI" as FDA
participant "Pricing APIs" as Pricing
database "Chat Memory" as Memory

User -> Docs: View platform documentation
User -> Evidence: Explore interactive analytics
Evidence -> DuckDB: Query drug data
DuckDB -> Evidence: Return analysis results
Evidence -> User: Interactive visualizations

User -> Flowise: "Research metformin pricing and safety"

Flowise -> FDA: Query drug safety data
FDA -> Flowise: Adverse events, recalls
Flowise -> Pricing: Query drug prices
Pricing -> Flowise: Price comparisons
Flowise -> Memory: Store conversation context
Flowise -> User: Combined research summary

FDA -> DuckDB: Data pipeline loads drug data

note right of Evidence
  Analytics Dashboard:
  - SQL-based data exploration
  - Interactive charts
  - Manufacturer distribution
  - Route analysis
end note

note right of Flowise
  Conversational AI:
  - Natural language processing
  - Multi-source data integration
  - Educational summaries
  - Chat memory & context
end note

@enduml
```

## Components

### 1. Hugo Documentation Hub
- **Purpose**: Platform information and research guides
- **Technology**: Hugo Extended + Docsy Theme
- **Features**:
  - Research methodology documentation
  - Data source explanations
  - Embedded analytics dashboard
  - Educational resources
  - Setup and configuration guides

### 2. Evidence Analytics Dashboard
- **Purpose**: Interactive data exploration and visualization
- **Technology**: Evidence.dev (SQL-based BI framework)
- **Features**:
  - SQL-based data exploration
  - Real-time drug data analysis with interactive charts
  - Manufacturer distribution and route analysis
  - Embedded analytics within documentation site
- **Access**: Available at `/analytics/` route

### 3. DuckDB Database
- **Purpose**: Embedded analytical database for fast queries
- **Technology**: DuckDB (OLAP database)
- **Features**:
  - Fast analytical queries
  - Columnar Parquet storage format
  - No server infrastructure needed
  - In-process SQL analytics
- **Data**: FDA drug labels, manufacturer info, route data

### 4. Data Pipeline
- **Purpose**: Automated FDA data fetching and processing
- **Technology**: Python 3.8+
- **Components**:
  - `fetch_drug_data.py`: FDA API data fetcher
  - `load_to_duckdb.py`: DuckDB data loader
  - `build-analytics.sh`: Automated build script
- **Functions**:
  - Fetch data from FDA OpenFDA API
  - Transform and load into DuckDB
  - Export data for Evidence.dev

### 5. Flowise AI Engine (Planned)
- **Purpose**: Conversational interface for drug research queries
- **Technology Stack**:
  - **Platform**: Flowise AI (no-code LLM workflows)
  - **LLM Integration**: OpenAI GPT or other models
  - **Workflow Builder**: Visual drag-and-drop interface
- **Core Functions**:
  - Natural language query processing
  - Multi-source API orchestration
  - Conversational memory and context
  - Educational response formatting

### 6. Data Sources

#### FDA OpenAPI (Primary Safety Data)
- **FAERS Database**: Adverse event reports
- **Drug Recalls**: Safety alerts and recalls
- **Safety Communications**: FDA announcements
- **Drug Labels**: Official prescribing information

#### Pricing Data Sources
- **GoodRx API**: Pharmacy price comparisons
- **Public Databases**: Medicare pricing data
- **Pharmacy Websites**: Direct price information

## Research Examples

### Interactive Analytics Dashboard
```
Use Case: "Explore FDA drug database visually"

Process:
1. Navigate to /analytics/ dashboard
2. View interactive charts and tables
3. Analyze manufacturer distribution
4. Explore route of administration patterns
5. Filter and drill down into specific drugs
6. Export insights for research
```

### SQL-Based Data Exploration
```sql
-- Example queries in Evidence dashboard

-- Top manufacturers by drug count
SELECT manufacturer_name, COUNT(*) as drug_count
FROM fda_drugs
GROUP BY manufacturer_name
ORDER BY drug_count DESC
LIMIT 10;

-- Routes of administration distribution
SELECT route, COUNT(*) as count
FROM fda_drugs
GROUP BY route
ORDER BY count DESC;
```

### Drug Price Research (Planned)
```
Query: "Compare metformin prices in New York"

Process:
1. Search pricing databases for metformin
2. Compare prices across different pharmacies
3. Identify generic vs brand pricing
4. Format results for research purposes
```

### FDA Safety Data Research (Planned)
```
Query: "FDA safety information for Lipitor"

Process:
1. Search FAERS database for adverse events
2. Check for recent recalls or safety alerts
3. Retrieve FDA safety communications
4. Compile educational summary
```

### Combined Research (Planned)
```
User: "Research insulin options - pricing and safety"

Flowise Workflow:
1. Parse natural language query for drug type (insulin)
2. Trigger FDA API workflow for safety data
3. Trigger pricing API workflow for cost comparison
4. Combine results using LLM reasoning
5. Format educational summary for user
6. Store conversation context for follow-up questions
```

<!-- ## Current Development Status

- **Phase**: 1 - Data Foundation Setup
- **Focus**: FDA OpenAPI integration and pricing data access
- **Goal**: Educational research platform for medication information -->

## Data Handling

### Privacy & Compliance
- **No Personal Health Information**: Platform does not collect or store personal medical data
- **Public Data Only**: All information from publicly available sources
- **Educational Purpose**: All data provided for research and educational use only
- **Disclaimers**: Clear statements that information is not medical advice

### Data Sources Documentation
- **FDA OpenAPI**: Free access, no authentication required
- **Pricing APIs**: Rate-limited access to public pricing information
- **Data Freshness**: Regular updates from source APIs
- **Data Accuracy**: Information accuracy dependent on source databases

## Getting Started

1. **Understand the Platform**: Review this documentation
2. **Explore Analytics Dashboard**: Visit `/analytics/` to explore interactive drug data visualizations
3. **Learn SQL Queries**: Try SQL-based data exploration in Evidence dashboard
4. **Review Data Sources**: Understand FDA data structure and limitations
5. **Set Up Local Environment**: Follow setup guide to run platform locally
6. **Educational Use**: Use information for research and learning only
7. **Verify Information**: Always consult healthcare providers for medical decisions

## Technical Implementation

### Hugo + Evidence Integration
- **Static Site Generation**: Hugo builds documentation and embeds Evidence analytics
- **Build Process**: Evidence builds to `/static/analytics/` for seamless integration
- **Automated Pipeline**: `build-analytics.sh` orchestrates complete build process
- **Development Workflow**: Separate dev servers for Hugo (1313) and Evidence (3000)

### Data Pipeline Architecture
- **Data Fetching**: Python scripts query FDA OpenFDA API
- **Data Storage**: DuckDB embedded database with Parquet format
- **Data Processing**: Transform JSON to structured tables
- **Evidence Integration**: DuckDB serves as data source for Evidence queries

### Evidence Analytics
- **SQL-Based Exploration**: Direct SQL queries against DuckDB
- **Interactive Visualizations**: Charts, tables, and dashboards
- **Embedded Dashboard**: Seamlessly integrated into Hugo documentation
- **Real-Time Analysis**: Fast analytical queries on drug data

### Flowise AI Architecture (Planned)
- **Workflow Builder**: Visual interface for creating LLM chains
- **API Integrations**: Custom nodes for FDA and pricing APIs
- **LLM Integration**: OpenAI GPT-4 or alternative models
- **Memory Management**: Conversation context and user sessions
- **Response Formatting**: Educational summaries with proper disclaimers

### Deployment
- **Documentation**: Static Hugo site (GitHub Pages)
- **Analytics Dashboard**: Evidence.dev embedded in `/analytics/` route
- **Database**: DuckDB file included in repository
- **Data Pipeline**: Python scripts for data updates
- **Flowise Platform**: Self-hosted or Flowise Cloud (planned)
- **API Connections**: Direct integration with FDA OpenAPI and pricing sources
- **Chat Interface**: Embedded Flowise chat widget in Hugo site (planned)

<!-- ## Contributing

This learning project welcomes contributions from:
- Healthcare data researchers
- API integration developers
- Documentation writers
- Healthcare professionals (for guidance on appropriate use) -->

## Important Disclaimers

- **Not Medical Advice**: All information for educational research only
- **Consult Healthcare Providers**: Always discuss findings with qualified medical professionals
- **Data Limitations**: Information accuracy depends on source databases
- **Educational Purpose**: Platform designed for learning and research, not clinical use

---

<!-- **Ready to research medication pricing and FDA safety data?** -->
<!-- [**🔍 Start Research →**](https://api.healthscope-ai.com) -->
