import re


def numbers_from_string(input: str) -> list[int]:
    """Extracts all integers from a given string and returns them as a list."""
    return list(map(int, re.findall(r"-?\d+", input)))


def digits_from_string(input: str) -> list[int]:
    """Extracts all single digit integers from a given string and returns them as a list."""
    return [int(char) for char in input if char.isdigit()]


def first_and_last_element(input: list) -> tuple:
    """Returns the first and last elements of a list as a tuple."""
    if not input:
        raise ValueError("Input list is empty")
    return (input[0], input[-1])


def spelled_out_digit_to_int(input: str) -> int:
    """Converts a spelled-out digit (e.g., 'zero', 'one', ...) to its integer representation."""
    mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    input_lower = input.lower()
    if input_lower in mapping:
        return mapping[input_lower]
    else:
        raise ValueError(f"Input '{input}' is not a valid spelled-out digit")
