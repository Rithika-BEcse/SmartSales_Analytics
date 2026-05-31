# SmartSales Analytics

SmartSales Analytics is a sales performance and business insights project for retail and e-commerce data. It includes a data cleaning script, SQL analytics queries, and Power BI dashboard design documentation.

## Project Contents
- `data/` - raw and cleaned datasets
- `scripts/` - Python data cleaning script
- `sql/` - SQL queries for analytics
- `docs/` - project documentation and dashboard design

## Getting Started
1. Install Python 3.9+.
2. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install project dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Run the cleaning script:
   ```powershell
   python scripts\data_cleaning.py
   ```
   Or use optional path arguments:
   ```powershell
   python scripts\data_cleaning.py --input data\SmartSales_Sales_Data.csv --output-csv data\SmartSales_Sales_Data_Cleaned.csv --output-xlsx data\SmartSales_Sales_Data_Cleaned.xlsx
   ```
5. Perform exploratory data analysis:
   ```powershell
   python scripts\eda.py
   ```
   This generates summary tables and charts in the `reports/` folder.

## Outputs
- `data/SmartSales_Sales_Data_Cleaned.csv`
- `data/SmartSales_Sales_Data_Cleaned.xlsx`

## Dashboard Design
- The project includes a Power BI dashboard design in `docs/powerbi_dashboard_design.md`.
- It defines an executive summary page, regional and category performance visuals, customer/product insights, and business risk/opportunity analysis.

## Live Demo
This project was executed successfully using `scripts/data_cleaning.py` and `scripts/eda.py`. The current run generated cleaned dataset outputs and EDA artifacts in the `reports/` folder.

## Local Dashboard Website
Open `reports/index.html` in your browser to view the static dashboard website with a navigation panel and multiple pages.

## Documentation
- See `docs/README.md` for full project overview and usage.
- See `docs/project_architecture.md` for architecture and data flow.
- See `docs/powerbi_dashboard_design.md` for dashboard planning.
- See `docs/business_insights.md` for business insights.
- See `docs/eda_report.md` for exploratory data analysis findings.
- See `docs/data_dictionary.md` for dataset definitions.
- See `docs/project_summary.md` for the project story and business value.

## Development and Testing
- Install dev dependencies:
  ```powershell
  python -m pip install -r requirements-dev.txt
  ```
- Run unit tests:
  ```powershell
  pytest tests
  ```
