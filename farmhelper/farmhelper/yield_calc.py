"""
yield_calc.py - Crop yield estimation utilities.
"""


def estimate_yield(area_hectares, yield_per_hectare):
    """
    Estimate total crop yield based on farm size and expected productivity.

    Args:
        area_hectares (float): Size of the farm in hectares.
        yield_per_hectare (float): Expected yield per hectare
            (e.g., in bags, kg, or tonnes - unit is up to the user).

    Returns:
        float: Estimated total yield, in the same unit as yield_per_hectare.
    """
    if area_hectares < 0:
        raise ValueError("Area cannot be negative.")
    if yield_per_hectare < 0:
        raise ValueError("Yield per hectare cannot be negative.")
    return area_hectares * yield_per_hectare
