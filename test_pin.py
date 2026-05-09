import pytest
from utils import pin_generator


def test_generate_4_digit_pin():
    pin = pin_generator.generate_pin(4)
    assert len(pin) == 4
    assert pin.isdigit()


def test_generate_6_digit_pin():
    pin = pin_generator.generate_pin(6)
    assert len(pin) == 6
    assert pin.isdigit()


def test_invalid_pin_length_raises_error():
    with pytest.raises(ValueError, match="The argument must be 4 or 6."):
        pin_generator.generate_pin(3)
