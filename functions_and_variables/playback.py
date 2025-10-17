"""
    This program asks the user for input which is in the form of text
    and then replaces the spaces in the input to ...
"""


def main():
    # Accept some input.
    sentence: str = input("Enter a sentence: ")

    # Call function to replace whitespaces with ...
    print(spaces_to_elipsis(sentence))


# Function to return the input with spaces replaced by ...
def spaces_to_elipsis(text: str) -> str:
    return text.replace(" ", "...")


if __name__ == "__main__":
    main()
