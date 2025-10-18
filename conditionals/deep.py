"""
    This program takes in input for an answer for a question and
    determines whether the answer is right.
"""


def main():
    # Accept srting input:
    answer: str = get_str_input(
        "What is the answer to the Great Question of Life, the Universe and Everything?")

    # Determine whether the answer is correct:
    print(answer_determiner(answer))
    print(answer)


def get_str_input(prompt: str) -> str:
    return input(prompt).lower()


def answer_determiner(possible_answer: str) -> str:
    if possible_answer == "42":
        return "Yes"
    elif possible_answer == "forty-two":
        return "Yes"
    elif possible_answer == "forty two":
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    main()
