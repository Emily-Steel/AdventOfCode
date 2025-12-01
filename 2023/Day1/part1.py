from typing import List

from utils import digits_from_string, first_and_last_element


def part1(input: List[str]) -> int:
    calibration_values = []
    for line in input:
        print(f"Processing line: {line.strip()}")
        numbers = digits_from_string(line)
        digits = first_and_last_element(numbers)
        print(f"  Extracted numbers: {numbers}")
        print(f"  First and last elements: {digits}")
        value = int("".join(map(str, digits)))
        print(f"  Combined value: {value}")
        calibration_values.append(value)
        print(" --- ")
    return sum(calibration_values)


def main():
    with open("2023/Day1/input.txt") as f:
        part1_input = f.readlines()
    result = part1(part1_input)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
