# Capstone Project: Comparative Analysis of Digital Security Methods in Popular Messengers

## Overview
This project is part of a master's thesis focused on analyzing modern digital security methods and digital hygiene among users of popular messengers (Telegram, WhatsApp, Viber).  
The goal is to evaluate how different platforms implement security features and compare their effectiveness using formalized criteria.


## Objectives
- Collect publicly available security information from official documentation and cybersecurity organizations.
- Identify key security criteria (encryption type, metadata protection, key storage, known vulnerabilities).
- Build a comparative matrix of messenger security characteristics.
- Visualize findings and provide recommendations regarding digital hygiene.


## Data Sources
Initial data is based on:
- Technical documentation (Telegram, WhatsApp, Viber)
- CERT-UA security recommendations
- Cyberpolice of Ukraine warnings
- Academic research (Signal Protocol, MTProto, etc.)


## Current Progress (Week 1)
- Defined research problem and significance.
- Formulated project objectives and methodology.
- Built initial MVP with a draft comparison matrix.
- Implemented:
  - YAML-based config for security criteria  
  - CSV table generator  
  - Heatmap visualization  


## Repository Structure

project/
├── config/
│ └── security_data.yaml
│
├── data/
│ ├── security_comparison.csv
│ └── security_comparison_heatmap.png
│
├── src/
│ ├── generate_table.py
│ └── visualize.py
│
├── venv/ # Virtual environment (ignored by git)
│
├── README.md
└── requirements.txt


## Installation & Setup

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## Data Generation
The project uses a config-driven approach (YAML):

config/security_data.yaml

Generate CSV table:

```bash
python src/generate_table.py
```

### Output:

data/security_comparison.csv — raw comparison table


### Visualizations
Generate heatmap and annotated matrix:

```bash
python src/visualize.py
```

This produces:

data/security_comparison_heatmap.png

On-screen heatmap visualization

### Requirements
```bash
pandas
PyYAML
tabulate
matplotlib
seaborn
```

### Next Steps
Expand number of security criteria.

Collect structured data from additional official sources.

Add scoring/weighting model for each messenger.

Introduce metadata analysis and risk scoring.

Build final comparative analytical model.
