"""
    This program takes in input that is a number plate and
    determines whether it is valid based on some conditions,
    if it is valid it returns Valid else Invalid.
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(number_plate: str) -> bool:
    # Conditions:
    # start with at least two letters
    # maximum of 6 characters letters or numbers
    # minimum of 2 characters
    # No numbers in the middle of the plate.
    # Numbers come in the end
    # No periods, spaces, or punctuation marks are allowed.


if __name__ == "__main__":
    main()
