import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def is_number_repeated_twice(number_str: str) -> bool:
    if len(number_str) % 2 != 0:
        return False
    half_length = len(number_str) // 2
    return number_str[:half_length] == number_str[half_length:]

def brute_force_part1(first: str, second: str) -> None:
    first_start, first_end = int(first), int(second)
    matches = []
    for number in range(first_start, first_end + 1):
        number_str = str(number)
        if is_number_repeated_twice(number_str):
            matches.append(number)
    print(f"Brute force found {len(matches)} matches between {first} and {second}: {matches}")
    return matches

def part1(input_data):
    ranges = []
    for line in input_data:
        items = line.strip().split(",")
        for item in items:
            ranges.append(item)
    summed_matches = 0
    for range_raw in ranges:
        first, second = range_raw.split("-")
        summed_matches += sum(brute_force_part1(first, second))
    return summed_matches

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        part1_input = f.readlines()
    result = part1(part1_input)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()