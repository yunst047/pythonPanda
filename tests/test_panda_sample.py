import io
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from panda_sample import (  # noqa: E402
    load_sales,
    monthly_revenue,
    pivot_region_product,
    revenue_by_region,
    top_products,
)

CSV = """date,region,product,units,unit_price
2026-01-05,North,Widget,10,2.00
2026-01-20,South,Gadget,3,10.00
2026-02-03,North,Gadget,1,10.00
2026-02-14,South,Widget,5,2.00
"""


@pytest.fixture
def df():
    return load_sales(io.StringIO(CSV))


def test_load_parses_dates_and_revenue(df):
    assert pd.api.types.is_datetime64_any_dtype(df["date"])
    assert df["revenue"].tolist() == [20.0, 30.0, 10.0, 10.0]


def test_revenue_by_region_sorted_desc(df):
    result = revenue_by_region(df)
    assert result.index.tolist() == ["South", "North"]
    assert result.tolist() == [40.0, 30.0]


def test_top_products(df):
    result = top_products(df, n=1)
    assert result.to_dict() == {"Gadget": 40.0}


def test_monthly_revenue(df):
    result = monthly_revenue(df)
    assert result.tolist() == [50.0, 20.0]
    assert [d.month for d in result.index] == [1, 2]


def test_pivot_region_product(df):
    result = pivot_region_product(df)
    assert result.shape == (2, 2)
    assert result.loc["North", "Widget"] == 10
    assert result.loc["South", "Gadget"] == 3
