"""Tests for Reda's temperature conversion feature."""

import sys

import pytest

from unit_converter.temperature import convert_temperature


@pytest.mark.parametrize(
    "value,from_unit,to_unit,expected",
    [
        (0, "C", "F", 32),
        (32, "F", "C", 0),
        (0, "C", "K", 273.15),
        (273.15, "K", "C", 0),
        (32, "F", "K", 273.15),
        (273.15, "K", "F", 32),
        (-40, "C", "F", -40),
    ],
)
def test_known_conversions(value, from_unit, to_unit, expected):
    assert convert_temperature(value, from_unit, to_unit) == pytest.approx(expected)


@pytest.mark.parametrize("unit", ["C", "F", "K"])
def test_same_unit_preserves_value(unit):
    assert convert_temperature(100, unit, unit) == 100


@pytest.mark.parametrize(
    "value,from_unit,to_unit,expected",
    [
        (-273.15, "C", "K", 0),
        (-459.67, "F", "K", 0),
        (0, "K", "C", -273.15),
        (0, "K", "F", -459.67),
    ],
)
def test_absolute_zero_boundary(value, from_unit, to_unit, expected):
    assert convert_temperature(value, from_unit, to_unit) == pytest.approx(expected)


@pytest.mark.parametrize("value,unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_rejects_temperature_below_absolute_zero(value, unit):
    with pytest.raises(ValueError, match="below absolute zero"):
        convert_temperature(value, unit, "K")


@pytest.mark.parametrize("from_unit,to_unit", [("X", "C"), ("C", "X"), (None, "K"), ("K", None)])
def test_rejects_unsupported_units(from_unit, to_unit):
    with pytest.raises(ValueError, match="unit must be C, F, or K"):
        convert_temperature(0, from_unit, to_unit)


@pytest.mark.parametrize("value", ["warm", None, True, float("nan"), float("inf"), -float("inf"), 10**1000])
def test_rejects_invalid_numeric_input(value):
    with pytest.raises(ValueError, match="finite number"):
        convert_temperature(value, "C", "F")


def test_rejects_conversion_that_overflows():
    with pytest.raises(ValueError, match="too large"):
        convert_temperature(sys.float_info.max, "C", "F")
