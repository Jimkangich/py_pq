"""
    This program is a test for meal.py
"""

from meal import convert
from meal import meal_for_current_time


def test_time_converted():
    assert convert("7.00") == 7.00
    assert convert("12.00") == 12.00
    assert convert("18.00") == 18.00
    assert convert("10.00") == 10.00
    assert convert("17.00") == 17.00
    assert convert("7.40") == 7.40


def test_meal_for_current_time():
    assert meal_for_current_time(7.00) == "breakfast time"
    assert meal_for_current_time(12.00) == "lunch time"
    assert meal_for_current_time(13.00) == "lunch time"
    assert meal_for_current_time(12.43) == "lunch time"
    assert meal_for_current_time(18.30) == "dinner time"
    assert meal_for_current_time(19.00) == "dinner time"
    assert meal_for_current_time(18.00) == "dinner time"
    assert meal_for_current_time(7.59) == "breakfast time"
    assert meal_for_current_time(8.00) == "breakfast time"
    assert meal_for_current_time(7.00) == "breakfast time"
