"""
    This program asks the user for input and converts :) to an emoji known
    as slightly smiling face and :( to an emoji known as slightly frowning face.
"""


def main():
    # Accept input for a sentence with the required ascii emojis
    sentence: str = input("Enter some text with :) or :( or both: ")
    # Output having converted the ascii emoji entered.
    print(face_convert(sentence))


def face_convert(some_text: str) -> str:
    # Create the emojis:
    """
    if ":)" in some_text:
        return some_text.replace(":)", "\U0001F642")
    elif ":(" in some_text:
        return some_text.replace("(", "\U0001F641")
    else:
    """
    return some_text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


if __name__ == "__main__":
    main()
