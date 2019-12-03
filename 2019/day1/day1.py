def calculate_fuel(mass):
    """
    Calculate fuel required to launch.

    Take the mass, divide it by 3, round down and subtract 2.
    Also calculate fuel needed to account for mass of fuel.

    Args:
        mass: Mass of the module.

    Returns:
        Fuel required to launch the module.

    """
    fuel = (mass // 3) - 2
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    else:
        fuel = 0
    return fuel


def main():
    """
    Open input file, and sum fuel for all entries.
    """
    with open('input') as f:
        data = f.readlines()
    total = 0
    for item in data:
        total += calculate_fuel(int(item.strip()))
    return total


if __name__ == "__main__":
    print(main())
