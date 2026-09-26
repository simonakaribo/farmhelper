"""
FarmHelper - A simple Python library for smallholder farming calculations.
"""

from .land import acres_to_hectares, hectares_to_acres, plots_to_hectares
from .yield_calc import estimate_yield
from .fertilizer import fertilizer_needed
from .harvest import days_to_harvest

__all__ = [
    "acres_to_hectares",
    "hectares_to_acres",
    "plots_to_hectares",
    "estimate_yield",
    "fertilizer_needed",
    "days_to_harvest",
]

__version__ = "0.1.0"
