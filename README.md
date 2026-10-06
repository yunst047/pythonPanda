# pythonPanda

A small [pandas](https://pandas.pydata.org/) sample. It loads a sales CSV and shows common operations:

- `read_csv` with date parsing and a computed `revenue` column
- `groupby` totals per region, sorted
- top-N products with `nlargest`
- monthly totals with `resample`
- a region × product `pivot_table`

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python panda_sample.py
```

This prints each result and writes `output/summary.csv` (revenue by region).

## Test

```bash
python -m pytest -q
```

## Layout

| Path | Purpose |
|------|---------|
| `panda_sample.py` | The analysis functions and `main()` |
| `data/sales.csv` | Sample data (20 rows) |
| `tests/test_panda_sample.py` | pytest checks on a small in-memory dataset |
