"""
    This is a test of twttr.py
"""

from twttr import remove_vowels


def test_correct_output():
    assert remove_vowels("haeioubeforefoes") == "hbfrfs"
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("Twitter") == "Twttr"
    assert remove_vowels("What's your name?") == "Wht's yr nm?"
    assert remove_vowels("CS50") == "CS50"


def test_incorrect_output():
    assert remove_vowels("123456789") == "123456789"
