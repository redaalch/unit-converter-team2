"""Convert temperatures between Celsius, Fahrenheit, and Kelvin."""

from math import isfinite


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a finite numeric value using the unit codes C, F, and K.

    Raise ValueError for unsupported units, invalid values, temperatures
    below absolute zero, or results too large to represent as a float.
    """
    minimums = {"C": -273.15, "F": -459.67, "K": 0.0}

    if not isinstance(from_unit, str) or from_unit not in minimums:
        raise ValueError("Source unit must be C, F, or K.")
    if not isinstance(to_unit, str) or to_unit not in minimums:
        raise ValueError("Target unit must be C, F, or K.")

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a finite number.")
    try:
        value = float(value)
    except OverflowError:
        raise ValueError("Temperature must be a finite number.") from None
    if not isfinite(value):
        raise ValueError("Temperature must be a finite number.")
    if value < minimums[from_unit]:
        raise ValueError("Temperature cannot be below absolute zero.")

    if from_unit == to_unit:
        return value

    # Use Kelvin as the intermediate unit so every conversion shares one path.
    if from_unit == "C":
        kelvin = value + 273.15
    elif from_unit == "F":
        kelvin = (value + 459.67) * (5 / 9)
    else:
        kelvin = value

    if to_unit == "C":
        result = kelvin - 273.15
    elif to_unit == "F":
        result = kelvin * (9 / 5) - 459.67
    else:
        result = kelvin

    if not isfinite(result):
        raise ValueError("Converted temperature is too large.")
    return result
