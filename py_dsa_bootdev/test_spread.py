"""

"""


from spread import get_estimated_spread


def test_correct_outcomes():
    assert get_estimated_spread([7, 4, 3, 100, 765, 2344, 1, 2, 32]) == 5056
    assert get_estimated_spread([12, 12, 12]) == 45


"""
def test_correctish_outcomes():
    assert get_estimated_spread([10, 200, 3000, 5000, 4]) == 11334
    assert get_estimated_spread([]) == 0
    assert get_estimated_spread([1, 1, 1]) == 4
    assert get_estimated_spread([100]) == 100
    assert get_estimated_spread([50, 60, 70, 80, 90]) == 483
    assert get_estimated_spread(
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 872
    assert get_estimated_spread(
        [
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ]) == 1912
"""
