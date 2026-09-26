"""
fertilizer.py - Fertilizer requirement calculation utilities.
"""


def fertilizer_needed(area_hectares, rate_kg_per_hectare):
    """
    Calculate the total amount of fertilizer needed for a farm.

    Args:
        area_hectares (float): Size of the farm in hectares.
        rate_kg_per_hectare (float): Recommended fertilizer application
            rate in kilograms per hectare.

    Returns:
        float: Total fertilizer needed, in kilograms.
    """
    if area_hectares < 0:
        raise ValueError("Area cannot be negative.")
    if rate_kg_per_hectare < 0:
        raise ValueError("Application rate cannot be negative.")
    return area_hectares * rate_kg_per_hectare
