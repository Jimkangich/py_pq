"""
    This program takes input from the user for a program construct in camelCase
    and it converts it to snake case which is the Python construct.
"""


def main():
    # Obtain input using get_str_function
    program_construct = get_str_input("camelCase: ")

    # Call function to convert camelCase to snake_case:
    print("snake_case: ", to_snake_case(program_construct))


# Get input from the user:
def get_str_input(prompt: str) -> str:
    return (input(prompt))


def to_snake_case(camel_case: str) -> str:
    # List to store each letter in the camelCased input:
    convert_to_snake_case_list: list = []
    count: int = 0
    for letter in camel_case:
        convert_to_snake_case_list.insert(count, letter)
        count += 1

    second_count: int = 0
    # Create a str to store the snake_cased output.
    # The output will be a sum of the elements of the list.
    answer_snake_case: str = ""
    for letter in convert_to_snake_case_list:
        if letter.isupper():
            answer_snake_case += "_"
            answer_snake_case += (
                convert_to_snake_case_list[second_count].lower())
            second_count += 1
            continue
        answer_snake_case += convert_to_snake_case_list[second_count]
        second_count += 1

    return answer_snake_case


if __name__ == "__main__":
    main()
