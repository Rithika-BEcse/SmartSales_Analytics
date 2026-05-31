"""SmartSales Analytics - Exploratory Data Analysis
This script generates summary metrics and charts from the cleaned sales dataset.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data_cleaning import clean_sales_data

DEFAULT_CLEANED_INPUT = Path(__file__).resolve().parent.parent / "data" / "SmartSales_Sales_Data_Cleaned.csv"
DEFAULT_RAW_INPUT = Path(__file__).resolve().parent.parent / "data" / "SmartSales_Sales_Data.csv"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent.parent / "reports"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run exploratory data analysis for SmartSales Analytics."
    )
    parser.add_argument(
        "--input",
        default=DEFAULT_CLEANED_INPUT,
        help="Path to the cleaned sales data CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where summary reports and charts will be saved.",
    )
    return parser.parse_args()


def load_sales_data(input_path: Path) -> pd.DataFrame:
    if input_path.exists():
        return pd.read_csv(input_path)

    if DEFAULT_RAW_INPUT.exists():
        raw_df = pd.read_csv(DEFAULT_RAW_INPUT)
        return clean_sales_data(raw_df)

    raise FileNotFoundError(
        f"Could not find input file at {input_path} or raw data at {DEFAULT_RAW_INPUT}."
    )


def save_plot(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def create_reports(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["order_month"] = pd.to_datetime(df["order_month"], errors="coerce").dt.to_period("M").astype(str)

    summary = {
        "total_orders": len(df),
        "unique_customers": int(df["customer_id"].nunique()),
        "total_revenue": float(df["revenue"].sum()),
        "total_profit": float(df["profit"].sum()),
        "average_profit_margin": float(df["profit_margin"].mean()),
        "top_region": df.groupby("region")["revenue"].sum().idxmax(),
        "top_category": df.groupby("product_category")["revenue"].sum().idxmax(),
    }

    summary_path = output_dir / "eda_summary.txt"
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write("SmartSales EDA Summary\n")
        handle.write("======================\n\n")
        for key, value in summary.items():
            handle.write(f"{key.replace('_', ' ').title()}: {value}\n")

    monthly = df.groupby("order_month").agg(
        total_revenue=("revenue", "sum"),
        total_profit=("profit", "sum"),
        avg_margin=("profit_margin", "mean"),
    ).reset_index()

    top_products = (
        df.groupby(["product_name", "product_category"])
        .agg(total_revenue=("revenue", "sum"), total_profit=("profit", "sum"))
        .reset_index()
        .sort_values("total_revenue", ascending=False)
        .head(10)
    )

    region_perf = (
        df.groupby(["region", "country"])
        .agg(total_revenue=("revenue", "sum"), total_profit=("profit", "sum"))
        .reset_index()
        .sort_values("total_revenue", ascending=False)
        .head(10)
    )

    channel_share = df["channel"].value_counts(normalize=True).mul(100).round(1)

    summary_csv_path = output_dir / "eda_summary_tables.csv"
    monthly.to_csv(summary_csv_path, index=False)

    save_plot(
        sns.lineplot(data=monthly, x="order_month", y="total_revenue", marker="o").get_figure(),
        output_dir / "monthly_revenue_trend.png",
    )

    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=top_products, x="total_revenue", y="product_name", color="#4c72b0")
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    save_plot(fig, output_dir / "top_products_revenue.png")

    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=region_perf, x="total_revenue", y="region", color="#dd8452")
    plt.title("Top Regions by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Region")
    save_plot(fig, output_dir / "top_regions_revenue.png")

    fig = plt.figure(figsize=(8, 6))
    sns.histplot(df["profit_margin"].dropna(), kde=True, color="#2a9d8f")
    plt.title("Profit Margin Distribution")
    plt.xlabel("Profit Margin")
    save_plot(fig, output_dir / "profit_margin_distribution.png")

    fig = plt.figure(figsize=(6, 6))
    channel_share.plot(kind="pie", autopct="%1.1f%%", startangle=140, ylabel="")
    plt.title("Sales Channel Share")
    save_plot(fig, output_dir / "channel_share.png")

    print(f"EDA artifacts generated in {output_dir}")


def main():
    sns.set_theme(style="whitegrid")
    args = parse_args()
    df = load_sales_data(Path(args.input))
    create_reports(df, Path(args.output_dir))


if __name__ == "__main__":
    main()
