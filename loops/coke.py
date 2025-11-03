"""
    This program takes in input specifically  25, 10, 5 cents to pay
    for a coke. The default price is 50 and it is hardcoded.
    Upon full payment the amount due will be displayed.
"""


def main():
    # Initial output.
    cost: int = 50
    print(f"Amount Due: {cost}")

    while True:
        coin_inserted: int = get_coin_inserted("Insert Coin: ")
        change: int = cost - coin_inserted
        cost = change
        if change <= 0:
            break
        print(f"Amount Due: {change}")

    print(f"Change Owed: {change}")


# Get input.
def get_coin_inserted(prompt: str) -> int:
    while True:
        try:
            coin: int = int(input(prompt))
        except ValueError:
            continue
        else:
            if coin == 25 or coin == 10 or coin == 5:
                return coin
            else:
                continue


if __name__ == "__main__":
    main()
