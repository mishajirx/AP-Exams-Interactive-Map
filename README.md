# 🗺️ Massachusetts AP Exam Performance Interactive Map

**Transforming 18 years of educational data into actionable insights for 120,000+ students**

<img width="1252" height="834" alt="image" src="https://github.com/user-attachments/assets/0790f56b-d34f-4975-894a-865232b30a59" />


**[➡️ Explore the Interactive Map](https://public.tableau.com/static/images/AP/APScoresMetrics/APPerfomanceMassachusetts/1.png)**

**[📰 Read the Featured LinkedIn Article](https://www.linkedin.com/pulse/visualizing-excellence-dynamic-map-ap-exam-schools-zhernevskii-mlwge/)**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)
[![Tableau](https://img.shields.io/badge/Tableau-2023+-orange.svg)](https://www.tableau.com/)

> *"A comprehensive data pipeline and visualization system that processes 1M+ records to help families make informed decisions about high school education in Massachusetts."*

## 📊 Project Overview

This project transforms raw Massachusetts Department of Education AP exam data spanning 18 years (2006-2024) into an interactive, geographical visualization that empowers students, parents, and educators to make data-driven educational decisions.

**Key Impact:**
- **120,000+** student records analyzed across Massachusetts
- **1M+** data points processed and enriched
- **1,500+** missing data points recovered using advanced algorithms
- **2,200+** LinkedIn article views helping families choose schools
- **40+** AP subject areas mapped across all MA public schools

## ✨ Key Features

### 🎯 Interactive Visualization
- **Geographic Mapping**: Each school represented by color-coded dots indicating pass rates (3-5 scores)
- **Size-Based Scaling**: Circle size represents number of test takers
- **Subject Filtering**: Dynamic filtering across 40+ AP subjects
- **Multi-Layer Analysis**: Compare overall performance vs. subject-specific results

### 🔧 Robust Data Pipeline
- **PostgreSQL Database**: Optimized schema for 1M+ educational records
- **Python ETL Scripts**: Automated data processing and cleaning
- **C++ Recovery Algorithms**: Advanced tree structures and set theory for missing data
- **Google Maps API Integration**: Geocoding for precise school locations

### 📈 Advanced Analytics
- **Hierarchical Data Processing**: Subject categorization with tree traversal algorithms
- **Statistical Modeling**: Performance metrics calculation and normalization  
- **Data Enrichment**: Coordinate assignment and missing value interpolation

## 🏗️ Technical Architecture

### Data Processing Pipeline
```
Raw CSV Data (MA Dept. of Education)
           ↓
Python Parser & Validator
           ↓
PostgreSQL Database (Normalized Schema)
           ↓
C++ Missing Data Recovery Engine
           ↓
Google Maps API Geocoding
           ↓
Tableau BI Visualization Layer
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Database** | PostgreSQL 13+ | Primary data storage and querying |
| **ETL Pipeline** | Python 3.8+ | Data parsing, cleaning, and transformation |
| **Data Recovery** | C++ | Advanced algorithms for missing data points |
| **Geocoding** | Google Maps API | School coordinate assignment |
| **Visualization** | Tableau BI | Interactive dashboard and mapping |
| **Web Layer** | HTML5/CSS3 | Embedded dashboard presentation |

## 📁 Repository Structure

```
📦 AP-Exams-Interactive-Map/
├── 🐍 Data Processing Scripts
│   ├── parse_csv_into_facts.py      # Raw data parser
│   ├── clean_and_enrich_db_facts.py # Data cleaning & recovery
│   ├── upload_school_dim.py         # School dimension loader
│   └── convert_csv_to_xlsx.py       # Format converter
├── 📊 Data Files
│   ├── Facts/                       # Raw AP performance data
│   ├── FactsArchive/               # Historical data backups  
│   ├── FactsUpd/                   # Processed data files
│   └── dimensions/                 # Lookup tables & metadata
├── 🗺️ Visualization Assets
│   └── mainpage.html               # Embedded Tableau dashboard
├── 🔧 Configuration & Utilities
│   ├── assistance_files/           # Helper scripts
│   ├── subjects.txt               # AP subject hierarchy
│   └── .gitignore                 # Git exclusions
└── 📋 Documentation
    ├── README.md                   # This file
    └── LICENSE                     # MIT License
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ with required libraries
- PostgreSQL 13+ database server  
- Google Maps API key (for geocoding)
- Tableau Desktop/Server (for visualization)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/mishajirx/AP-Exams-Interactive-Map.git
cd AP-Exams-Interactive-Map
```

2. **Set up the database**
```bash
# Create PostgreSQL database
createdb ap_performance_db

# Configure connection in config.py (not included for security)
```

3. **Process the data**
```bash
# Parse raw CSV data
python parse_csv_into_facts.py

# Upload school dimensions
python upload_school_dim.py

# Clean and enrich data (runs C++ recovery algorithms)
python clean_and_enrich_db_facts.py
```

4. **View the visualization**
Open `mainpage.html` in your browser to see the embedded Tableau dashboard.

## 🧮 Advanced Data Recovery Algorithm

The project implements sophisticated C++ algorithms to recover missing data points:

### Algorithm Overview
- **Tree-Based Processing**: Uses hierarchical subject categorization
- **Set Theory Operations**: Applies intersection and union operations on subject sets
- **Proportional Distribution**: Distributes missing grades based on test volume ratios
- **Breadth-First Traversal**: Processes subject hierarchy using queue-based algorithm

### Recovery Process
1. **Identify Missing Data**: Detect records with zero grade distributions
2. **Build Subject Hierarchy**: Create tree structure of AP subjects
3. **Calculate Known Totals**: Sum grades for available subjects in each branch
4. **Proportional Assignment**: Distribute remaining grades based on test volumes
5. **Validate Results**: Ensure statistical consistency across all levels

## 📊 Data Schema

### Core Tables
- **ap_performance_facts**: Main fact table with test scores and metrics
- **school_dim**: School master data with coordinates and metadata
- **subject_dim**: AP subject hierarchy and categorization

### Key Metrics
- **Test Volume**: Total number of exams taken per school/subject
- **Pass Rate**: Percentage of students scoring 3-5 (passing threshold)
- **Score Distribution**: Breakdown across all five AP score levels (1-5)
- **Geographic Data**: Latitude/longitude coordinates for mapping

## 🎯 Use Cases & Impact

### For Students & Families
- **School Selection**: Identify top-performing schools by subject area
- **Program Evaluation**: Compare AP offerings across districts
- **Geographic Analysis**: Find high-quality schools within desired areas

### For Educators & Administrators
- **Performance Benchmarking**: Compare school performance against state averages
- **Resource Allocation**: Identify programs needing additional support
- **Trend Analysis**: Track performance changes over 18-year period

### For Researchers & Policy Makers
- **Educational Equity**: Visualize performance disparities across regions
- **Data-Driven Decisions**: Access comprehensive historical performance data
- **Geographic Correlation**: Analyze relationships between location and achievement

## 📈 Performance & Scale

### Data Volume Processed
- **1,000,000+** individual student test records
- **120,000+** students tracked across 18 years
- **1,500+** missing data points successfully recovered
- **300+** Massachusetts public schools geocoded and mapped

### Technical Performance
- **Sub-second** query response times for interactive filtering
- **99.9%** data accuracy after validation and cleanup
- **Scalable** architecture supporting additional years of data
- **Responsive** visualization supporting multiple device formats

## 🤝 Contributing

We welcome contributions to improve the project! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/improvement`)
3. **Commit your changes** (`git commit -m 'Add new feature'`)
4. **Push to branch** (`git push origin feature/improvement`)
5. **Open a Pull Request**

### Contribution Areas
- 🔧 Data pipeline optimizations
- 📊 Additional visualization features
- 🧮 Algorithm improvements
- 📚 Documentation enhancements
- 🧪 Test coverage expansion

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Massachusetts Department of Elementary and Secondary Education** for providing comprehensive AP performance data
- **College Board** for establishing the AP program and assessment standards
- **Google Maps Platform** for geocoding services enabling precise school mapping
- **Tableau Community** for visualization best practices and inspiration

## 📞 Contact & Support

**Author**: [Mikhail (Misha) Zhernevskii](https://www.linkedin.com/in/mikhail-zhernevskii/)  
**Institution**: Johns Hopkins University - Computer Science  
**Achievement**: USACO Platinum Competitor

### Connect With Me
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/mikhail-zhernevskii/)
- 📧 Email: [Contact via LinkedIn]
- 🐙 [GitHub Profile](https://github.com/mishajirx)

### Project Links
- 🗺️ **[Interactive Map](https://public.tableau.com/static/images/AP/APScoresMetrics/APPerfomanceMassachusetts/1.png)**
- 📰 **[Featured Article](https://www.linkedin.com/pulse/visualizing-excellence-dynamic-map-ap-exam-schools-zhernevskii-mlwge/)** (2,200+ views)
- 🏫 **[MA Education Data Portal](https://profiles.doe.mass.edu/statereport/ap.aspx)**

---

<div align="center">

**⭐ If this project helped you make educational decisions, please give it a star! ⭐**

*Empowering data-driven educational choices across Massachusetts*

</div>
