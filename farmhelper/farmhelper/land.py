"""
land.py - Land area conversion utilities for farmers.
"""

# In Ghana, a common informal land unit is the "plot", roughly 0.02 hectares (100ft x 100ft)
HECTARES_PER_PLOT = 0.02
ACRES_PER_HECTARE = 2.47105


def acres_to_hectares(acres):
    """
    Convert acres to hectares.

    Args:
        acres (float): Land area in acres.

    Returns:
        float: Equivalent land area in hectares.
    """
    if acres < 0:
        raise ValueError("Acres cannot be negative.")
    return acres / ACRES_PER_HECTARE


def hectares_to_acres(hectares):
    """
    Convert hectares to acres.

    Args:
        hectares (float): Land area in hectares.

    Returns:
        float: Equivalent land area in acres.
    """
    if hectares < 0:
        raise ValueError("Hectares cannot be negative.")
    return hectares * ACRES_PER_HECTARE


def plots_to_hectares(plots):
    """
    Convert number of standard plots to hectares.

    Args:
        plots (float): Number of plots (1 plot = 0.02 hectares).

    Returns:
        float: Equivalent land area in hectares.
    """
    if plots < 0:
        raise ValueError("Number of plots cannot be negative.")
    return plots * HECTARES_PER_PLOT
