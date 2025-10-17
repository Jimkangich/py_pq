"""
    This is a test for the program einstein.py
"""
from einstein import energy_calculation


def test_integers():
    assert energy_calculation(50) == 4500000000000000000
    assert energy_calculation(1) == 90000000000000000
    assert energy_calculation(14) == 1260000000000000000
