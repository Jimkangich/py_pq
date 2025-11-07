"""


"""

import math


def main():
    influencer1_followers: int = 200
    avg_eng_per_inf1: int = 0.8
    print(get_influencer_score(influencer1_followers, avg_eng_per_inf1))
    influencer2_followers: int = 1
    avg_eng_per_inf2: int = 1
    print(get_influencer_score(influencer2_followers, avg_eng_per_inf2))


def get_influencer_score(num_followers: int,
                         average_engagement_percentage: int) -> int:
    # NB: log 16 base 2 = math(16, 2) logarithm base 2 of 16
    # Formula influencer_score =
    #   average_engagement_percentage * math.log(num_followers, 2)
    return round(average_engagement_percentage * math.log(num_followers, 2))


if __name__ == "__main__":
    main()
