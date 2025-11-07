"""

"""

from influencer_score import get_influencer_score


def test_correct_input():
    assert get_influencer_score(1, 1) == 0
    assert get_influencer_score(200, 0.8) == 6
    assert get_influencer_score(300000, 0.5) == 9
    assert get_influencer_score(500000, 0.2) == 4
    assert get_influencer_score(750000, 0.7) == 14
