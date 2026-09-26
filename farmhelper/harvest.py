"""
harvest.py - Harvest date tracking utilities.
"""

from datetime import date


def days_to_harvest(planting_date, growth_period_days):
    """
    Calculate the number of days remaining until harvest.

    Args:
        planting_date (datetime.date): The date the crop was planted.
        growth_period_days (int): Number of days the crop takes to mature.

    Returns:
        int: Number of days remaining until harvest. Negative if the
            harvest date has already passed.
    """
    if growth_period_days < 0:
        raise ValueError("Growth period cannot be negative.")

    harvest_date = date.fromordinal(
        planting_date.toordinal() + growth_period_days
    )
    today = date.today()
    remaining = (harvest_date - today).days
    return remaining
