import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def find_max_joltage(battery_bank: str) -> int:
    max_value = 0
    second_max_value = 0
    for i, joltage_rating_raw in enumerate(battery_bank):
        joltage_rating = int(joltage_rating_raw)
        if joltage_rating > max_value and i < len(battery_bank) - 1:
            max_value = joltage_rating
            second_max_value = 0
        elif joltage_rating > second_max_value:
            second_max_value = joltage_rating
    return int(f"{max_value}{second_max_value}")            

def part1(input_data):
    sum_joltages = 0
    for battery_bank in input_data:
        sum_joltages += find_max_joltage(battery_bank.strip())
    return sum_joltages

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