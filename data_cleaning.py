"""SmartSales Analytics - Data Cleaning Script
This script loads the raw sales dataset, applies cleaning and standardization, and exports cleaned CSV and Excel files.
"""

import argparse
import pandas as pd
import re
import sys
from pathlib import Path

RAW_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "SmartSales_Sales_Data.csv"
CLEANED_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "SmartSales_Sales_Data_Cleaned.csv"
EXCEL_OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "SmartSales_Sales_Data_Cleaned.xlsx"

REQUIRED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "region",
    "country",
    "product_category",
    "product_subcategory",
    "product_name",
    "units_sold",
    "unit_price",
    "cost",
    "revenue",
    "profit",
    "order_status",
    "channel",
]


def normalize_column_name(column_name: str) -> str:
    normalized = column_name.strip()
    normalized = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', normalized)
    normalized = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', normalized)
    normalized = normalized.replace(' ', '_').replace('-', '_').lower()
    normalized = re.sub(r'__+', '_', normalized)
    return normalized


def parse_order_date(value):
    if pd.isna(value):
        return pd.NaT
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return pd.to_datetime(value, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.to_datetime(value, errors='coerce')


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names
    df.columns = [normalize_column_name(col) for col in df.columns]

    # Parse and standardize dates
    df['order_date'] = df['order_date'].apply(parse_order_date)

    # Remove exact duplicates
    df = df.drop_duplicates()

    # Fill missing values for text columns
    text_columns = ['customer_name', 'region', 'country', 'product_category', 'product_subcategory', 'product_name', 'order_status', 'channel']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown').astype(str).str.title()

    # Numeric conversions
    numeric_columns = ['units_sold', 'unit_price', 'cost', 'revenue', 'profit']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fix negative or missing financials with recalculation rules
    df['units_sold'] = df['units_sold'].fillna(0).astype(int)
    df['unit_price'] = df['unit_price'].fillna(0.0)
    df['cost'] = df['cost'].fillna(0.0)
    df['revenue'] = df.apply(lambda row: row['units_sold'] * row['unit_price'] if pd.isna(row['revenue']) or row['revenue'] <= 0 else row['revenue'], axis=1)
    df['profit'] = df.apply(lambda row: row['revenue'] - row['cost'] if pd.isna(row['profit']) or row['profit'] == 0 else row['profit'], axis=1)

    # Standardize order status values
    df['order_status'] = df['order_status'].str.capitalize().replace({'Pending': 'Pending', 'Completed': 'Completed', 'Cancelled': 'Cancelled', 'Unknown': 'Unknown'})

    # Standardize region and country casing
    df['region'] = df['region'].str.title()
    df['country'] = df['country'].str.title()

    # Add derived fields for analytics
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    df['profit_margin'] = (df['profit'] / df['revenue']).replace([float('inf'), -float('inf')], 0).fillna(0).round(4)

    return df


def main():
    print(f"Loading raw dataset from {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    cleaned_df = clean_sales_data(df)

    print(f"Writing cleaned CSV to {CLEANED_DATA_PATH}")
    cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)

    args = parse_args()
    input_path = Path(args.input)
    output_csv_path = Path(args.output_csv)
    output_excel_path = Path(args.output_xlsx)

    print(f"Loading raw dataset from {input_path}")
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(input_path)
    cleaned_df = clean_sales_data(df)

    print("Validating required columns")
    validate_columns(cleaned_df)

    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    output_excel_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Writing cleaned CSV to {output_csv_path}")
    cleaned_df.to_csv(output_csv_path, index=False)

    print(f"Exporting cleaned Excel workbook to {output_excel_path}")
    cleaned_df.to_excel(output_excel_path, index=False, sheet_name='CleanedSalesData')

    print("Cleaning complete. Key stats:")
    print(cleaned_df[["order_date", "region", "product_category", "revenue", "profit"]].describe(include='all'))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Load, clean, and export SmartSales sales data."
    )
    parser.add_argument(
        "--input",
        default=RAW_DATA_PATH,
        help="Path to raw sales CSV input file.",
    )
    parser.add_argument(
        "--output-csv",
        default=CLEANED_DATA_PATH,
        help="Path to cleaned CSV output file.",
    )
    parser.add_argument(
        "--output-xlsx",
        default=EXCEL_OUTPUT_PATH,
        help="Path to cleaned Excel output file.",
    )
    return parser.parse_args()


def validate_columns(df: pd.DataFrame) -> None:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns after normalization: {', '.join(missing)}"
        )


if __name__ == '__main__':
    main()
