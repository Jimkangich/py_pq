"""
    This program takes input for cost of meal and percentage expected for tip
    and calculates the cost of the tip that will be paid.
"""


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = (dollars * percent) / 100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    # Convert input of type str to float removing the $ sign.
    try:
        return float(d.replace("$", ""))
    except ValueError:
        return 0.00
    else:
        return 0.00


def percent_to_float(p: str) -> float:
    # Convert input of type str to float removing the % sign.
    try:
        return float(p.replace("%", ""))
    except ValueError:
        return 0.00
    else:
        return 0.00


if __name__ == "__main__":
    main()
