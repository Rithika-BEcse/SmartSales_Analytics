# Project Architecture

## Folder Structure
- `data/`
  - Raw and cleaned datasets
- `scripts/`
  - Python data cleaning and export script
- `sql/`
  - SQL analytics query definitions
- `docs/`
  - Project documentation, insights, and dashboard design

## Data Flow
1. Raw data is available in `data/SmartSales_Sales_Data.csv`.
2. The Python script `scripts/data_cleaning.py` performs data cleaning:
   - removes duplicates
   - standardizes date formats
   - handles missing values
   - standardizes text fields
   - recalculates revenue and profit when needed
3. Cleaned output is written as CSV and Excel for easy analytics.
4. SQL queries in `sql/SmartSales_Analytics_queries.sql` analyze the cleaned dataset.
5. Power BI imports the cleaned Excel file and uses the dashboard design defined in documentation.

## Dataset Explanation
- `order_id`: Unique order identifier.
- `order_date`: Date of purchase in mixed formats.
- `customer_id`: Unique customer code.
- `customer_name`: Customer or company name.
- `region`, `country`: Geographic market.
- `product_category`, `product_subcategory`, `product_name`: Product hierarchy.
- `units_sold`: Number of units sold.
- `unit_price`: Sales price per unit.
- `cost`: Cost of goods sold for the order.
- `revenue`: Sales revenue; may require recalculation after cleaning.
- `profit`: Revenue minus cost.
- `order_status`: Order completion state.
- `channel`: Sales channel such as Online or Offline.
- `order_month`: Derived field used for monthly reporting.
- `profit_margin`: Derived metric indicating profitability.

## Business Analytics Scope
- Monthly revenue and profit trends
- Region performance and customer distribution
- Product category and top product analysis
- Customer segmentation by revenue contribution
- KPI benchmarking for business review
