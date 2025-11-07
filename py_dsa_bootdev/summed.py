"""
    Function sum accepts a list and return the sum of values
    in the list. Sum of empty list is 0.
"""


def main():
    # Create a list.
    views: list = [45, 50, 32, 100, 77]
    views1: list = [1, 2, 3]
    print(summed(views))
    print(summed(views1))


def summed(nums):
    # Sum variable to store the sum of views.
    sum: int = 0

    for number in nums:
        sum += number

    return sum


if __name__ == "__main__":
    main()
