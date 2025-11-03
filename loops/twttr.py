"""
    This is program takes input a str and returns the string
    having removed all the vowels.
"""


def main():
    tweet: str = get_str_input_lower("Input: ")
    print(remove_vowels(tweet))


# Get str input in lower case
def get_str_input_lower(prompt: str) -> str:
    while True:
        try:
            return (input(prompt).lower())
        except ValueError:
            continue


def remove_vowels(tweet: str):
    return tweet.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")


if __name__ == "__main__":
    main()
