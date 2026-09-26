"""
test_farmhelper.py - Simple demo/test script for the FarmHelper library.
"""

from datetime import date, timedelta
from farmhelper import (
    acres_to_hectares,
    hectares_to_acres,
    plots_to_hectares,
    estimate_yield,
    fertilizer_needed,
    days_to_harvest,
)

# Land conversion
print("2 acres in hectares:", round(acres_to_hectares(2), 3))
print("1 hectare in acres:", round(hectares_to_acres(1), 3))
print("5 plots in hectares:", plots_to_hectares(5))

# Yield estimation
print("Estimated yield (3 ha, 15 bags/ha):", estimate_yield(3, 15), "bags")

# Fertilizer calculation
print("Fertilizer needed (2 ha, 50kg/ha):", fertilizer_needed(2, 50), "kg")

# Harvest countdown
planted = date.today() - timedelta(days=30)
print("Days to harvest (planted 30 days ago, 90-day crop):",
      days_to_harvest(planted, 90))
