# Portfolio Analytics Platform

A data-driven framework for assessing and ranking residential real estate investment opportunities across Los Angeles County.

## Overview

This Streamlit application allows real estate investors and analysts to upload property data, calculate key performance indicators (KPIs), and visualize portfolio performance through interactive dashboards.

## Features

- **Data Upload** - Import property data from Excel (.xlsx, .xls) or CSV files
- **KPI Calculations** - Automatically calculates:
  - Net Operating Income (NOI)
  - Occupancy Rate
  - Revenue per Unit
  - Expense Ratio
- **Filtering** - Filter properties by type and submarket
- **Portfolio Summary** - View aggregate metrics across your portfolio
- **Trend Analysis** - Visualize KPI trends over time with interactive charts

## Installation

1. Clone the repository:
```bash
git clone https://github.com/justinw4558-sys/Jaden-Path-and-Justin-Wang---Capstone-Project.git
cd Jaden-Path-and-Justin-Wang---Capstone-Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Data Format

Upload a spreadsheet with the following columns:

| Column | Description |
|--------|-------------|
| `property_name` | Property identifier |
| `property_type` | e.g., Multifamily, Office, Retail |
| `submarket` | Geographic area |
| `total_units` | Number of units |
| `occupied_units` | Currently occupied units |
| `revenue` | Total revenue |
| `operating_expenses` | Total operating expenses |
| `date` | Period date (optional, for trends) |

A sample data file (`sample_data.csv`) is included for testing.

## Tech Stack

- **Python 3.11**
- **Streamlit** - Web application framework
- **Pandas** - Data processing
- **Plotly** - Interactive charts
- **OpenPyXL** - Excel file support

## Authors

- Justin Wang - Co-lead Analyst
- Jaden Path - Co-lead Analyst

## Documentation

See [PRD.md](PRD.md) for the full Product Requirements Document.
