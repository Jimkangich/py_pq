"""
    This program takes time and outputs whether it is breakfast time,
    lunch time, or dinner time.
"""


def main():
    # Obtain the time from the user:
    current_time: str = get_str_input_lower("What time is it? ")
    if current_time == "Invalid input, enter the correct time.":
        print("Invalid input, enter the correct time.")
    else:
        # Call convert to convert the time to a float:
        current_time_float = convert(current_time)

        if type(current_time_float) is float:
            # Which meal is to be eaten at current time?
            print(meal_for_current_time(current_time_float))
        else:
            print("Invalid input, enter the correct time.")


# Get str input in lower case in this case time:
def get_str_input_lower(prompt: str) -> str:
    time_entered = (input(prompt).lower())
    if ":" in time_entered or "." in time_entered:
        time_entered = time_entered.replace(":", ".")
        return time_entered
    else:
        return "Invalid input, enter the correct time."


def convert(time: str):
    try:
        return float(time)
    except ValueError:
        return "Invalid input, enter the correct time."


# Determine which meal is to be taken at the time:
def meal_for_current_time(current_time_float: float) -> str:
    if current_time_float >= 0.00 and current_time_float <= 24.00:
        if current_time_float >= 7.00 and current_time_float <= 8.00:
            return "breakfast time"
        elif current_time_float >= 12.00 and current_time_float <= 13.00:
            return "lunch time"
        elif current_time_float >= 18.00 and current_time_float <= 19.00:
            return "dinner time"
        else:
            return " "
    else:
        return "Invalid input, enter the correct time."


if __name__ == "__main__":
    main()
