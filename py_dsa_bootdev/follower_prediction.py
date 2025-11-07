"""



"""


def main():
    follower_count1: int = 10
    influencer1_type: str = "fitness"
    num_months1: int = 2

    follower_count2: int = 10
    influencer2_type: str = "cosmetic"
    num_months2: int = 2

    follower_count3: int = 10
    influencer3_type: str = "other"
    num_months3: int = 2

    print(get_follower_prediction(follower_count1,
                                  influencer1_type,
                                  num_months1))
    print(get_follower_prediction(follower_count2,
                                  influencer2_type,
                                  num_months2))
    print(get_follower_prediction(follower_count3,
                                  influencer3_type,
                                  num_months3))


def get_follower_prediction(follower_count: int,
                            influencer_type: str,
                            num_months: int) -> int:
    # Formula total = a1 * r ** n
    # predicted_followers =
    #           follower_count * influencer_type_number ** num_months - 1

    if influencer_type == "fitness":
        return (follower_count * (4 ** num_months))
    elif influencer_type == "cosmetic":
        return (follower_count * (3 ** num_months))
    else:
        return (follower_count * (2 ** num_months))


if __name__ == "__main__":
    main()
