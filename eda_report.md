# Exploratory Data Analysis Report

This report summarizes the newly added EDA workflow for the SmartSales Analytics project. The EDA script processes the cleaned sales dataset and generates summary metrics, tables, and charts in the `reports/` folder.

## Key Findings
- Total orders: 50
- Unique customers: 30
- Total revenue: $146,212.00
- Total profit: $49,262.00
- Average profit margin: 34.4%
- Top revenue region: Asia
- Top revenue category: Technology

## Generated Artifacts
The EDA script creates the following files in `reports/`:
- `eda_summary.txt` — text summary of core metrics
- `eda_summary_tables.csv` — summary tables for monthly trends
- `monthly_revenue_trend.png` — monthly revenue line chart
- `top_products_revenue.png` — top 10 products by revenue
- `top_regions_revenue.png` — top regions by revenue
- `profit_margin_distribution.png` — profit margin distribution histogram
- `channel_share.png` — sales channel share pie chart

## Usage
Run the EDA script from the project root:
```powershell
python scripts\eda.py
```

If the cleaned dataset is not already available, the script will clean the raw source data first.

## Notes
- The EDA report is intentionally light and focused on business-facing metrics.
- This workflow is useful for making the project stronger for a data analyst portfolio by demonstrating analysis, summary charts, and actionable insights.
