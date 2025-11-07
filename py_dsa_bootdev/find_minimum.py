"""
    Find minimum algorithm.
    It accepts a list of integers nums and returns the smallest
    number in the list.
"""


def main():
    follower_count: list = [32, 44, 89, 21, 44, 52, 84, 90, 110]
    print(find_minimum(follower_count))


def find_minimum(nums: list) -> int:
    # Check whether the list is empty. Empty list has a truth value of false.
    if not nums:
        return None

    # Declare a variable minimum to store the minimum number.
    minimum: int = nums[0]

    for number in nums:
        if minimum > number:
            minimum = number

    # Return smallest number in the list.
    return minimum


if __name__ == "__main__":
    main()
