"""
    This is a test for playback.test
"""
from playback import spaces_to_elipsis


def test_this_is_sth():
    assert spaces_to_elipsis("This is CS50") == "This...is...CS50"
    assert spaces_to_elipsis(
        "This is our week on functions") == "This...is...our...week...on...functions"


def test_lets_do_sth():
    assert spaces_to_elipsis(
        "Let's implement a function called hello") == "Let's...implement...a...function...called...hello"
