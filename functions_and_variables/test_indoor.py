"""
    This is a test for the program indoor.py.
"""
from indoor import set_text_to_lower


def test_hello():
    assert set_text_to_lower("HELLO, WORLD") == "hello, world"
    assert set_text_to_lower("HELLO, JIMKANGICH") == "hello, jimkangich"
    assert set_text_to_lower("HELLO, PYTHON") == "hello, python"


def test_this():
    assert set_text_to_lower("THIS IS CS50") == "this is cs50"


def test_numbers():
    assert set_text_to_lower("50") == "50"
