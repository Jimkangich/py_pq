"""
    This program takes in input as an expression and performs mathematical
    calculations depending on the input.
"""


def main():
    # Get an expression for calculations:
    expression: str = get_expression("Expression: ")

    # Print the answer:
    print(arithmetic_operations(expression))


def get_expression(prompt: str) -> str:
    return (input(prompt))


def arithmetic_operations(expression: str):
    expression = expression.rsplit(" ")

    match expression[1]:
        case "+":
            return round(float(expression[0]) + float(expression[2]), 1)
        case "-":
            return round(float(expression[0]) - float(expression[2]), 1)
        case "*" | "x" | "X":
            return round(float(expression[0]) * float(expression[2]), 1)
        case "/":
            if float(expression[2]) != 0.0:
                return round(float(expression[0]) / float(expression[2]), 1)
            else:
                return "Can't divide by zero."
        case "%":
            if float(expression[2]) != 0.0:
                return round(float(expression[0]) % float(expression[2]), 1)
            else:
                return "Can't divide by zero."
        case _:
            return "Incorrect input. Try again."


if __name__ == "__main__":
    main()
