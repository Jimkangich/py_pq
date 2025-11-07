"""


"""


from follower_prediction import get_follower_prediction


def test_correct_input():
    assert get_follower_prediction(10, "fitness", 2) == 160
    assert get_follower_prediction(10, "fitness", 1) == 40
    assert get_follower_prediction(10, "fitness", 2) == 160
    assert get_follower_prediction(12, "cosmetic", 4) == 972


def test_other_correct_input():
    assert get_follower_prediction(15, "business", 4) == 240
    assert get_follower_prediction(10, "fitness", 5) == 10240
    assert get_follower_prediction(10, "fitness", 6) == 40960
    assert get_follower_prediction(10, "fitness", 7) == 163840
    assert get_follower_prediction(10, "fitness", 8) == 655360
    assert get_follower_prediction(10, "tech", 9) == 5120
