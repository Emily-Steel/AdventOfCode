import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def find_max_joltage(battery_bank: str, max_batteries: int = 12) -> int:
    maxes_found = [0] * max_batteries
    batteries_found = 0
    for i, joltage_rating_raw in enumerate(battery_bank):
        joltage_rating = int(joltage_rating_raw)
        is_resetting = False
        for j in range(batteries_found, max_batteries):
            if is_resetting:
                maxes_found[j] = 0
            elif joltage_rating > maxes_found[j]:
                maxes_found[j] = joltage_rating
                is_resetting = True
        if joltage_rating == 9:
            batteries_found += 1 # 9 is the max possible rating for a battery, we won't find a higher one so lock it in
        if i >= len(battery_bank) - (max_batteries - batteries_found):
            batteries_found += 1
    maxes_str = int("".join(str(x) for x in maxes_found))
    print (f"Maxes found: {maxes_str} for battery bank: {battery_bank}")
    return maxes_str

def part2(input_data):
    sum_joltages = 0
    for battery_bank in input_data:
        sum_joltages += find_max_joltage(battery_bank.strip())
    return sum_joltages

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        part2_input = f.readlines()
    result = part2(part2_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()