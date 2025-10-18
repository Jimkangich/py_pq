"""
    This is my personal package for the most reused functions in my programs.
"""

# Get str input


def get_str_input(prompt: str) -> str:
    return (input(prompt))


# Get str input in lower case
def get_str_input_lower(prompt: str) -> str:
    return (input(prompt).lower())


# Get str input in upper case
def get_str_input_upper(prompt: str) -> str:
    return (input(prompt).upper())


# Get int input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue


# Get float input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            continue
