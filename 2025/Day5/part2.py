import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def parse_input(lines):
    fresh_ranges = []
    ingredients_to_check = []
    i = 0
    while i < len(lines):
        if lines[i] == "":
            break
        fresh_ranges.append(tuple(map(int, lines[i].split("-"))))
        i += 1
    i += 1  # Skip the blank line
    while i < len(lines):
        if lines[i] != "":
            ingredients_to_check.append(int(lines[i]))
        i += 1    
    return fresh_ranges, ingredients_to_check

def part2(input_data):
    fresh_ranges, ingredients_to_check = parse_input(input_data)
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    merged_ranges = []
    current = None
    for r in sorted_ranges:
        if current is None:
            current = r
        else:
            if r[0] <= current[1] + 1:
                current = (current[0], max(current[1], r[1]))
            else:
                merged_ranges.append(current)
                current = r
    if current is not None:
        merged_ranges.append(current)
    number_of_fresh_ingredients = 0
    for r in merged_ranges:
        number_of_fresh_ingredients += r[1] - r[0] + 1
    return number_of_fresh_ingredients

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = f.readlines()
    lines = [line.strip() for line in day_input]
    result = part2(lines)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()