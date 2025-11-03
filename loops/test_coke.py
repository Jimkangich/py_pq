"""
    Test for coke.py program.
"""
# THIS TEST DOES NOT WORK!! TBD

from coke import get_coin_inserted


def test_coin_input():
    assert get_coin_inserted("25") == 25
    assert get_coin_inserted("5") == 5
    assert get_coin_inserted("10") == 10
