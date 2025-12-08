import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def print_row(beams):
    for b in beams:
        if isinstance(b, int):
            if b == 0:
                print(".", end="")
            else:
                print(b, end="")
        else:
            print(b, end="")
    print()

def part2(input_data):
    beams = list(map(lambda c: 1 if c == "S" else 0, input_data[0]))
    print_row(beams)
    for i in range(1, len(input_data)):
        next_beams = list([0] * len(beams))
        for j, c in enumerate(input_data[i]):
            if c == "^":
                next_beams[j - 1] += beams[j]
                next_beams[j] = "^"
                next_beams[j + 1] += beams[j]
            else:
                if beams[j] != "^":
                    next_beams[j] += beams[j]
        print_row(next_beams)
        beams = next_beams
    total_timelines = sum(b for b in beams if isinstance(b, int))

    return total_timelines

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part2(day_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()