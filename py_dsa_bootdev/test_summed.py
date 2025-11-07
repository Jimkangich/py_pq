"""

"""


from spread import get_estimated_spread


def test_correct_outcomes():
    assert get_estimated_spread([7, 4, 3, 100, 765, 2344, 1, 2, 32]) == 5056
