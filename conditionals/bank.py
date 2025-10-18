"""
    This program takes in input for a greeting, if the greeting starts with a 'h' but not hello then it return $20, if the greeting starts with 'hello' it returns $0, else it returns $20.
"""


def main():
    # Get input
    greeting = get_str_input_lower("Greeting: ")

    # Determine whether the answer is correct
    print(greeting_return(greeting))


# Get str input in lower case
def get_str_input_lower(prompt: str) -> str:
    return (input(prompt).lower())


# Determine whether the greeting is correct.
def greeting_return(possible_greeting: str) -> str:
    if possible_greeting.lower() == "hello":
        return "$0"
    elif possible_greeting.lower().startswith("hello"):
        return "$0"
    elif possible_greeting.lower().startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
