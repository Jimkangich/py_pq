"""
    This is a test programs for deep.py
"""


from deep import answer_determiner
from deep import get_str_input


def test_correct_answers():
    assert answer_determiner("42") == "Yes"
    assert answer_determiner("forty-two") == "Yes"
    assert answer_determiner("forty two") == "Yes"


def test_wrong_answers():
    assert answer_determiner("40") == "No"
    assert answer_determiner("10000") == "No"
