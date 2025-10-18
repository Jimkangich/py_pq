"""
    This is a test file for extensions.py
"""

from extensions import file_type_check


def test_correct_filename():
    assert file_type_check("cat.gif") == "image/gif"
    assert file_type_check("cat.pdf") == "application/pdf"
    assert file_type_check("cat.txt") == "text/plain"
    assert file_type_check("cat.jpg") == "image/jpeg"
    assert file_type_check("cat.jpg") == "image/jpeg"
    assert file_type_check("cat.png") == "image/png"
    assert file_type_check("cat.zip") == "application/zip"


def test_wrong_input():
    assert file_type_check("cat") == "application/octet-stream"
    assert file_type_check("12345") == "application/octet-stream"
    assert file_type_check("c12345a.t") == "application/octet-stream"
    assert file_type_check("cat.catjddj") == "application/octet-stream"
    assert file_type_check("___cat.jdjdjd") == "application/octet-stream"
    assert file_type_check("cat.kfkfkk.gif") == "application/octet-stream"
