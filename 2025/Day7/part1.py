import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def part1(input_data):
    beams = list(map(lambda c: "|" if c == "S" else ".", input_data[0]))
    print("".join(beams))
    total_splits = 0
    for i in range(1, len(input_data)):
        next_beams = list(["."] * len(beams))
        for j, c in enumerate(input_data[i]):
            if c == "^" and beams[j] == "|":
                next_beams[j - 1] = "|"
                next_beams[j] = "^"
                next_beams[j + 1] = "|"
                total_splits += 1
            else:
                if beams[j] == "|" or next_beams[j] == "|":
                    next_beams[j] = "|"
                else:
                    next_beams[j] = c
        print("".join(next_beams))
        beams = next_beams

    return total_splits

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part1(day_input)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()