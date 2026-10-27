
"""Convert lengths between meters, kilometers, and miles."""

from math import isfinite


def convert_length(value, from_unit, to_unit):
    """Convert a finite, non-negative length between m, km, and mi."""
    conversion_factors = {
        "m": 1,
        "km": 1000,
        "mi": 1609.344,
    }

    if not isfinite(value):
        raise ValueError("Length must be a finite number")

    if value < 0:
        raise ValueError("Length cannot be negative")

    if from_unit not in conversion_factors:
        raise ValueError(f"Invalid source unit: {from_unit}")

    if to_unit not in conversion_factors:
        raise ValueError(f"Invalid target unit: {to_unit}")

    meters = value * conversion_factors[from_unit]
    return meters / conversion_factors[to_unit]
