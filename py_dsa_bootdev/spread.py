"""


"""


def main():
    audiences_followers: list = [2, 3, 2, 19]
    print(get_estimated_spread(audiences_followers))


def get_estimated_spread(audiences_followers: list) -> int:
    average_audience_followers: int = 0
    if len(audiences_followers) <= 0:
        return 0
    num_followers = len(audiences_followers)
    total_followers: int = 0

    for followers in audiences_followers:
        total_followers += followers

    average_audience_followers: float = total_followers / num_followers
    return round(average_audience_followers * (num_followers ** 1.2))


if __name__ == "__main__":
    main()
