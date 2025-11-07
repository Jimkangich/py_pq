"""

"""


def main():
    influencer1_num_posts: int = 5
    influencer2_num_posts: int = 0
    influencer3_num_posts: int = 6
    influencer4_num_posts: int = 10
    influencer5_num_posts: int = 20

    print(num_possible_orders(influencer1_num_posts))
    print(num_possible_orders(influencer2_num_posts))
    print(num_possible_orders(influencer3_num_posts))
    print(num_possible_orders(influencer4_num_posts))
    print(num_possible_orders(influencer5_num_posts))


def num_possible_orders(num_posts: int) -> int:
    no_possible_orders = 1

    if num_posts == 0:
        return 1

    for i in range(2, num_posts + 1):
        no_possible_orders *= i

    return no_possible_orders


if __name__ == "__main__":
    main()
