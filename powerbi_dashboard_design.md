# Power BI Dashboard Design

## Dashboard Title
SmartSales Analytics – Sales Performance & Business Insights

## Data Source
- `data/SmartSales_Sales_Data_Cleaned.xlsx`
- Alternative: `data/SmartSales_Sales_Data_Cleaned.csv`

## Dashboard Pages
1. **Executive Summary**
   - KPI cards: Total Revenue, Total Profit, Profit Margin, Customer Count, Completed Orders, Total Units Sold
   - Trend line: Monthly Sales Revenue
   - Bar chart: Revenue by Region
   - Donut chart: Product Category Share
   - Slicer panel: Region, Product Category, Order Status, Channel, Customer Segment

2. **Regional & Category Performance**
   - Map visual: Revenue by Country/Region
   - Clustered bar chart: Profit by Region and Product Category
   - Table: Top 10 regions by revenue and profit margin

3. **Customer & Product Insights**
   - Bar chart: Top Customers by Revenue
   - Matrix: Product Category, Product Name, Revenue, Profit, Units Sold
   - KPI card: Average Order Value (Revenue / Orders)
   - Stacked column chart: Customer segment revenue distribution

4. **Business Risk & Opportunity**
   - Table: Loss-making products and categories
   - Line chart: Seasonal trend of revenue and profit across months
   - Card: Highest growth region, best-selling category, largest customer segment

## Visual Elements
- Line charts for time series and trend analysis
- Bar charts for product and region comparisons
- Pie and donut charts for category distribution
- Map visual for geography-based performance
- KPI cards for business metrics
- Slicers for dynamic filtering across visuals
- Tables for detailed product/customer listings

## Recommended Interactivity
- Dynamic filters for region, product category, order status, channel, and customer segment
- Drill-through from summary to product/customer detail pages
- Tooltips showing revenue, profit, profit margin, and units sold
- Conditional formatting for positive/negative profit trends

## Dashboard Goals
- Enable business stakeholders to identify best-performing regions and categories
- Reveal seasonal sales patterns for planning promotions
- Surface revenue-driving customers and product lines
- Highlight loss-making items for corrective action

## Suggested KPI Definitions
- Total Revenue = SUM(revenue)
- Total Profit = SUM(profit)
- Profit Margin = SUM(profit) / SUM(revenue)
- Customer Count = DISTINCTCOUNT(customer_id)
- Average Order Value = SUM(revenue) / COUNT(order_id)
