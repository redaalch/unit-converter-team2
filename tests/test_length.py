
import pytest

from unit_converter.length import convert_length


def test_miles_to_meters():
    assert convert_length(1, "mi", "m") == pytest.approx(1609.344)


def test_kilometers_to_meters():
    assert convert_length(1, "km", "m") == pytest.approx(1000)


def test_meters_to_kilometers():
    assert convert_length(1000, "m", "km") == pytest.approx(1)


def test_zero_length():
    assert convert_length(0, "mi", "km") == pytest.approx(0)


def test_negative_length_raises_error():
    with pytest.raises(ValueError):
        convert_length(-5, "m", "km")


def test_invalid_source_unit_raises_error():
    with pytest.raises(ValueError):
        convert_length(10, "yd", "m")


def test_same_unit_returns_same_value():
    assert convert_length(42, "km", "km") == pytest.approx(42)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_length_raises_error(value):
    with pytest.raises(ValueError, match="finite"):
        convert_length(value, "m", "km")
