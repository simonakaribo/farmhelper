# FarmHelper

FarmHelper is a lightweight Python library that provides simple utility functions for smallholder farmers and agriculture students. It helps convert land area units (acres, hectares, plots), estimate crop yield based on farm size and expected productivity, calculate fertilizer requirements per hectare, and track the number of days remaining until harvest. Designed as an educational project, it demonstrates clean function design, docstrings, and modular Python packaging for beginners.

## Installation

Clone this repository and import the `farmhelper` package directly:

```bash
git clone https://github.com/simonakaribo/farmhelper.git
cd farmhelper
python3 test_farmhelper.py
```

## Usage

```python
from farmhelper import acres_to_hectares, estimate_yield, fertilizer_needed, days_to_harvest
from datetime import date, timedelta

# Convert 2 acres to hectares
print(acres_to_hectares(2))

# Estimate yield for a 3-hectare farm at 15 bags/hectare
print(estimate_yield(3, 15))

# Calculate fertilizer needed for a 2-hectare farm at 50kg/hectare
print(fertilizer_needed(2, 50))

# Days remaining until harvest (planted 30 days ago, 90-day crop)
print(days_to_harvest(date.today() - timedelta(days=30), 90))
```

**Example output:**

```
0.809
45
100
60
```

## Modules

- `land.py` — Land area conversions (acres, hectares, plots)
- `yield_calc.py` — Crop yield estimation
- `fertilizer.py` — Fertilizer requirement calculation
- `harvest.py` — Harvest countdown tracking

## License

MIT License — free to use for educational purposes.
