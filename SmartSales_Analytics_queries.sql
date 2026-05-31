-- SmartSales Analytics SQL Queries
-- Table: sales
-- Columns: order_id, order_date, customer_id, customer_name, region, country, product_category,
--          product_subcategory, product_name, units_sold, unit_price, cost, revenue, profit,
--          order_status, channel, order_month, profit_margin

-- Monthly Revenue Analysis
SELECT
    order_month,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin) * 100, 2) AS average_profit_margin_percentage
FROM sales
GROUP BY order_month
ORDER BY order_month;

-- Top-Selling Products by Revenue
SELECT
    product_name,
    product_category,
    SUM(units_sold) AS units_sold,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM sales
GROUP BY product_name, product_category
ORDER BY total_revenue DESC
LIMIT 10;

-- Region-wise Sales Performance
SELECT
    region,
    country,
    COUNT(DISTINCT customer_id) AS customer_count,
    SUM(units_sold) AS units_sold,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin) * 100, 2) AS avg_profit_margin
FROM sales
GROUP BY region, country
ORDER BY total_revenue DESC;

-- Profit Analysis by Category
SELECT
    product_category,
    SUM(revenue) AS total_revenue,
    SUM(cost) AS total_cost,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin) * 100, 2) AS avg_profit_margin_percentage
FROM sales
GROUP BY product_category
ORDER BY total_profit DESC;

-- Customer Segmentation: revenue bands
SELECT
    CASE
        WHEN SUM(revenue) >= 5000 THEN 'Platinum'
        WHEN SUM(revenue) >= 2500 THEN 'Gold'
        WHEN SUM(revenue) >= 1000 THEN 'Silver'
        ELSE 'Bronze'
    END AS customer_segment,
    COUNT(DISTINCT customer_id) AS customer_count,
    SUM(revenue) AS segment_revenue,
    SUM(profit) AS segment_profit
FROM sales
GROUP BY customer_segment
ORDER BY segment_revenue DESC;

-- KPI Calculations
SELECT
    COUNT(DISTINCT customer_id) AS customer_count,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    ROUND((SUM(profit) / SUM(revenue)) * 100, 2) AS overall_profit_margin_percentage,
    SUM(CASE WHEN order_status = 'Completed' THEN 1 ELSE 0 END) AS completed_orders,
    SUM(units_sold) AS total_units_sold
FROM sales;

-- Loss-Making Products and Categories
SELECT
    product_name,
    product_category,
    SUM(units_sold) AS units_sold,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
FROM sales
GROUP BY product_name, product_category
HAVING SUM(profit) < 0
ORDER BY profit ASC;
