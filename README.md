# SmartSales Analytics

## Overview

SmartSales Analytics is an end-to-end Sales Analytics and Business Intelligence project designed to transform raw sales data into meaningful business insights.

The project demonstrates the complete analytics workflow, including:

* Data Cleaning and Preprocessing using Python
* Exploratory Data Analysis (EDA)
* SQL-Based Business Analytics
* KPI and Performance Analysis
* Power BI Dashboard Design
* Business Insight Reporting

The objective is to help organizations monitor sales performance, identify profitable products, understand customer behavior, and support data-driven decision-making.

---

## Business Problem

Businesses generate large amounts of sales data every day. Without proper analysis, it becomes difficult to identify:

* Revenue growth trends
* High-performing products
* Profitable customer segments
* Regional sales performance
* Business risks and opportunities

This project addresses these challenges by building a complete analytics solution from raw data to executive-level reporting.

---

## Project Objectives

* Clean and standardize raw sales data
* Generate business-ready datasets
* Analyze revenue and profit trends
* Identify top-performing products and categories
* Evaluate regional sales performance
* Perform customer contribution analysis
* Design a Power BI dashboard for management reporting

---

## Technology Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Data Cleaning & Processing |
| Pandas     | Data Manipulation          |
| NumPy      | Numerical Operations       |
| SQL        | Business Analytics Queries |
| Excel      | Data Export                |
| Power BI   | Dashboard Development      |
| GitHub     | Project Version Control    |

---

## Project Architecture

### Data Flow

1. Raw sales data is collected.
2. Python scripts clean and standardize the data.
3. Cleaned datasets are exported to CSV and Excel.
4. SQL queries generate business insights.
5. Power BI uses the cleaned dataset for dashboard creation.
6. Insights are documented for business review.

---

## Project Structure

```text
SmartSales_Analytics/
│
├── data/
│   ├── SmartSales_Sales_Data.csv
│   ├── SmartSales_Sales_Data_Cleaned.csv
│   └── SmartSales_Sales_Data_Cleaned.xlsx
│
├── scripts/
│   ├── data_cleaning.py
│   └── eda.py
│
├── sql/
│   └── SmartSales_Analytics_queries.sql
│
├── docs/
│   ├── project_architecture.md
│   ├── business_insights.md
│   ├── data_dictionary.md
│   ├── eda_report.md
│   ├── powerbi_dashboard_design.md
│   └── project_summary.md
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset Description

The dataset contains retail and e-commerce sales information including:

* Order Details
* Customer Information
* Product Information
* Geographic Data
* Sales Revenue
* Profit Metrics
* Sales Channels
* Order Status

### Key Fields

| Field            | Description             |
| ---------------- | ----------------------- |
| order_id         | Unique order identifier |
| order_date       | Date of purchase        |
| customer_id      | Customer identifier     |
| customer_name    | Customer name           |
| region           | Sales region            |
| country          | Customer country        |
| product_category | Product category        |
| product_name     | Product name            |
| units_sold       | Quantity sold           |
| revenue          | Total revenue           |
| profit           | Total profit            |
| channel          | Sales channel           |
| profit_margin    | Profitability indicator |

---

## Data Cleaning Process

The Python data cleaning pipeline performs:

* Duplicate removal
* Missing value handling
* Date format standardization
* Text standardization
* Revenue recalculation
* Profit recalculation
* Derived field generation

Output files:

* SmartSales_Sales_Data_Cleaned.csv
* SmartSales_Sales_Data_Cleaned.xlsx

---

## Exploratory Data Analysis (EDA)

The EDA process includes:

* Revenue Analysis
* Profit Analysis
* Customer Analysis
* Product Analysis
* Regional Performance Analysis
* Monthly Trend Analysis

Generated outputs are stored in the `reports/` directory.

---

## SQL Analytics

The SQL module includes business-focused queries such as:

* Monthly Revenue Analysis
* Profit Performance
* Top Products
* Top Customers
* Regional Comparison
* Category Performance
* KPI Evaluation

---

## Power BI Dashboard

The dashboard is designed for executive and management-level reporting.

### Dashboard Sections

* Executive Summary
* Revenue Performance
* Profit Analysis
* Regional Performance
* Product Insights
* Customer Insights
* Business Risk & Opportunity Analysis

---

## Dashboard Preview

Add dashboard screenshots here.

Example:

<img width="1352" height="573" alt="Screenshot 2026-05-31 124253" src="https://github.com/user-attachments/assets/cd07f1c0-ad08-4c2c-8130-6cb060284a24" />


<img width="1348" height="570" alt="Screenshot 2026-05-31 124341" src="https://github.com/user-attachments/assets/00ba50b6-20aa-4a74-b4fb-a78021e7d404" />

<img width="1350" height="519" alt="Screenshot 2026-05-31 124417" src="https://github.com/user-attachments/assets/772199a9-35c6-4c5b-b830-c49dca564719" />




---

## Key Business Insights

Some of the insights generated include:

* Monthly revenue growth patterns
* High-profit product categories
* Top revenue-generating customers
* Regional sales performance comparison
* Customer contribution analysis
* Profitability benchmarking

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/yourusername/SmartSales_Analytics.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

### Run EDA

```bash
python scripts/eda.py
```

---

## Outputs

Generated outputs include:

* Cleaned CSV Dataset
* Cleaned Excel Dataset
* EDA Reports
* Charts and Visualizations
* SQL Analytics Results
* Power BI Dashboard

---

## Documentation

Additional project documentation is available in the `docs/` folder:

* Project Architecture
* Data Dictionary
* EDA Report
* Business Insights
* Dashboard Design
* Project Summary

---

## Future Enhancements

* Automated ETL Pipeline
* Real-Time Dashboard Integration
* Sales Forecasting using Machine Learning
* Customer Segmentation Models
* Advanced KPI Monitoring

---

## Author

**Rithika L**

BE (Computer Science)

Sales Analytics | Business Intelligence | Data Analytics Projects
