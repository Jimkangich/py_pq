"""
    This program takes in input, a sting of text and converts it to uppercase.
"""


def main():
    # Accept input for the sentence
    sentence: str = input("Enter a sentence: ")
    print(set_text_to_lower(sentence))


def set_text_to_lower(some_text: str) -> str:
    return str.lower(some_text)


if __name__ == "__main__":
    main()
