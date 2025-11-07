

from find_minimum import find_minimum


def test_integer_values():
    assert find_minimum([5, 4, 1, 3, 2, 6]) == 1
    assert find_minimum([7, 4, 3, 100, 2343243, 343434, 1, 2, 32]) == 1
    assert find_minimum([12, 12, 12]) == 12
    assert find_minimum([10, 200, 3000, 5000, 4]) == 4
