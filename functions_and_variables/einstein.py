"""
    This program takes in mass in kilograms and calculates energy using
    Albert Einstein's formula F = mc2 (f is equal to m times c squared).
"""


def main():
    # Accept input for mass in kilograms.
    mass: int = int(mass_input("m: "))
    # Call the function that calculates energy.
    print("E:", energy_calculation(mass))


def mass_input(prompt: str):
    while True:
        try:
            return (int(input(prompt)))
        except ValueError:
            continue


def energy_calculation(some_mass: int) -> int:
    return (some_mass * 300000000 * 300000000)


if __name__ == "__main__":
    main()
