"""
    This program is a test for interpreter.py
"""

from interpreter import arithmetic_operations


def test_addition():
    assert arithmetic_operations("1 + 1") == 2.0
    assert arithmetic_operations("89 + 100") == 189.0
    assert arithmetic_operations("87 + 1") == 88.0
    assert arithmetic_operations("1.56 + 3.33") == 4.9
    assert arithmetic_operations("44 + 99") == 143.0


def test_subtraction():
    assert arithmetic_operations("839 - 11") == 828.0
    assert arithmetic_operations("77.65 - 11") == 66.7
    assert arithmetic_operations("39 - 11") == 28.0
    assert arithmetic_operations("89 - 991") == -902.0
    assert arithmetic_operations("9.456 - 8.333") == 1.1


def test_division():
    assert arithmetic_operations("1 / 1") == 1.0
    assert arithmetic_operations("121 / 21") == 5.8
    assert arithmetic_operations("27 / 9") == 3.0
    assert arithmetic_operations("55 / 5") == 11.0
    assert arithmetic_operations("15 / 4") == 3.8
    assert arithmetic_operations("89 / 4") == 22.2


def test_multiplication():
    assert arithmetic_operations("1 * 1") == 1.0
    assert arithmetic_operations("11 * 11") == 121.0
    assert arithmetic_operations("999 * 1") == 999.0
    assert arithmetic_operations("0 * 1") == 0.0
    assert arithmetic_operations("8.999 * 1") == 9.0


def test_division_by_zero():
    assert arithmetic_operations("890 / 0") == "Can't divide by zero."
    assert arithmetic_operations("767 / 0") == "Can't divide by zero."
    assert arithmetic_operations("83.33 % 0") == "Can't divide by zero."
    assert arithmetic_operations("76.32 / 0") == "Can't divide by zero."
    assert arithmetic_operations("32 % 0") == "Can't divide by zero."


def test_modulous():
    assert arithmetic_operations("9 % 2") == 1.0
    assert arithmetic_operations("8 % 2") == 0.0
    assert arithmetic_operations("76 % 1") == 0.0
    assert arithmetic_operations("111 % 3") == 0.0
    assert arithmetic_operations("1 % 1") == 0.0
    assert arithmetic_operations("55 % 6") == 1.0


def test_division_by_negative_numbers():
    assert arithmetic_operations("-9 % -2") == -1.0
    assert arithmetic_operations("111 % -3") == 0.0
    assert arithmetic_operations("55 % -6") == -5.0
    assert arithmetic_operations("121 / -21") == -5.8
    assert arithmetic_operations("27 / -9") == -3.0
