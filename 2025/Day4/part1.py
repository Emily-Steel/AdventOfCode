import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def get_moveable_rolls(previous_line, current_line, next_line):
    movable_rolls = 0
    for i in range(len(current_line)):
        if current_line[i] == "@":
            adjacent_rolls = 0
            adj_str = ""
            if i > 0:
                adjacent_rolls += 1 if previous_line[i - 1] == "@" else 0
                adjacent_rolls += 1 if current_line[i - 1] == "@" else 0
                adjacent_rolls += 1 if next_line[i - 1] == "@" else 0
            adjacent_rolls += 1 if previous_line[i] == "@" else 0
            adjacent_rolls += 1 if next_line[i] == "@" else 0
            if i < len(current_line) - 1:
                adjacent_rolls += 1 if previous_line[i + 1] == "@" else 0
                adjacent_rolls += 1 if current_line[i + 1] == "@" else 0
                adjacent_rolls += 1 if next_line[i + 1] == "@" else 0
            if adjacent_rolls < 4:
                movable_rolls += 1
    return movable_rolls

def part1(input_data):
    if len(input_data) == 0:
        return 0
    movable_rolls = 0
    previous_line = ["."] * len(input_data[0].strip())
    for i in range(len(input_data)):
        line = input_data[i].strip()
        next_line = input_data[i + 1].strip() if i + 1 < len(input_data) else ["."] * len(line)
        rolls = get_moveable_rolls(previous_line, line, next_line)
        movable_rolls += rolls
        previous_line = line
    return movable_rolls

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = f.readlines()
    result = part1(day_input)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()