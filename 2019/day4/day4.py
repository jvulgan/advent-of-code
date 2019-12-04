def is_there_double_digit(number):
    """
    Check if there's two same adjecent digits in the number.

    There needs to be at least one pair of digits, if there's more it does not
    count as a pair.

    122345 returns True.
    111111 returns False (there's no distict pair, only 6 same digits).
    123789 returns False (there's no pair at all).
    123444 returns False (there's no pair, only triplet).
    111122 returns True (there's a pair of 2's, more 1's don't matter).

    Args:
        number: Int to be checked.

    Returns:
        True if the number passed the check, false otherwise.

    """
    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 1):
        if (i < len(digits) - 2) and digits[i] == digits[i+1]:
            if digits[i+2] != digits[i] and digits[i-1] != digits[i]:
                return True
        else:
            if digits[i] == digits[i+1] and digits[i-1] != digits[i]:
                return True
    return False


def are_digits_decreasing(number):
    """
    Check if the digits in number ever decrease from left to right.

    122345 returns True.
    111111 returns True.
    123450 returns False.

    Args:
        number: Int to be checked.

    Returns:
        True if the number passed the check, false otherwise.

    """
    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 1):
        if digits[i+1] < digits[i]:
            return True
    return False


def run_the_checks(numbers):
    """
    Run the checks on numbers.

    Args:
        numbers: List of numbers.

    Returns:
        Total number of numbers that passed the checks.

    """
    total = 0
    for nr in numbers:
        if is_there_double_digit(nr) and not are_digits_decreasing(nr):
            total += 1
    return total


def main():
    start = 136818
    end = 685979
    print(run_the_checks(range(start, end+1)))


if __name__ == "__main__":
    main()
