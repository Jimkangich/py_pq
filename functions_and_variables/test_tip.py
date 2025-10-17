
from tip import dollars_to_float
from tip import percent_to_float


def test_correct_input_dollar():
    assert dollars_to_float("$100.00") == 100.00
    assert dollars_to_float("$50.00") == 50.00
    assert dollars_to_float("$10.00") == 10.00
    assert dollars_to_float("$10.00") == 10.00


def test_wrong_input_dollar():
    assert dollars_to_float("$1$0$0.0$0") == 100.00
    assert dollars_to_float("2$5$.00") == 25.00


def test_correct_percent_input():
    assert percent_to_float("50%") == 50.00
    assert percent_to_float("100%") == 100.00
    assert percent_to_float("15%") == 15.00
    assert percent_to_float("18%") == 18.00


def test_wrong_input_percent():
    assert dollars_to_float("%100.00") == 0
