"""

"""

from possible_orders import num_possible_orders


def test_correct_input():
    assert num_possible_orders(1) == 1
    assert num_possible_orders(6) == 720
    assert num_possible_orders(7) == 5040
    assert num_possible_orders(8) == 40320
    assert num_possible_orders(9) == 362880
    assert num_possible_orders(11) == 39916800
