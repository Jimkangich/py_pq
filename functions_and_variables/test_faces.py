"""
    This is a test for the program faces.py
"""
from faces import face_convert


def test_hello():
    assert face_convert("Hello :)") == "Hello \U0001F642"
    assert face_convert("Hello :(") == "Hello \U0001F641"


def test_hello_and_goodbye():
    assert face_convert(
        "Hello :) Goodbye :(") == "Hello \U0001F642 Goodbye \U0001F641"
