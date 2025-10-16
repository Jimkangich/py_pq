"""
    This program takes in mass in kilograms and calculates energy using
    Albert Einstein's formula F = mc2 (f is equal to m times c squared).
"""


def main():
    # Accept input for mass in kilograms.
    mass: int = int(input("m: "))
    # Call the function that calculates energy.
    print("E: ", energy_calculation(mass))

def mass_input() -> int:
    while True:
        try:
                
def energy_calculation(some_mass: int) -> int:
    return some_mass * 300000000


if __name__ == "__main__":
    main()
