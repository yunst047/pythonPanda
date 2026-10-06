"""Small pandas sample: load a CSV, then groupby, resample and pivot it."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent


def load_sales(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df["revenue"] = df["units"] * df["unit_price"]
    return df


def revenue_by_region(df):
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


def top_products(df, n=3):
    return df.groupby("product")["revenue"].sum().nlargest(n)


def monthly_revenue(df):
    return df.resample("MS", on="date")["revenue"].sum()


def pivot_region_product(df):
    return df.pivot_table(
        index="region", columns="product", values="units", aggfunc="sum", fill_value=0
    )


def main():
    df = load_sales(ROOT / "data" / "sales.csv")

    sections = {
        "First rows": df.head(),
        "Summary statistics": df.describe(),
        "Revenue by region": revenue_by_region(df),
        "Top 3 products": top_products(df),
        "Monthly revenue": monthly_revenue(df),
        "Units: region x product": pivot_region_product(df),
    }
    for title, result in sections.items():
        print(f"\n=== {title} ===")
        print(result)

    out_dir = ROOT / "output"
    out_dir.mkdir(exist_ok=True)
    revenue_by_region(df).to_csv(out_dir / "summary.csv")
    print(f"\nWrote {out_dir / 'summary.csv'}")


if __name__ == "__main__":
    main()
