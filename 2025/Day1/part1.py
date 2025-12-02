def part1(input_data):
    zeros = 0
    dial_position = 50
    for line in input_data:
        direction = line[0] == "L" and -1 or 1
        amount = int(line[1:])
        dial_position = (dial_position + direction * amount) % 100
        if dial_position == 0:
            zeros += 1
    return zeros


def main():
    with open("2025/Day1/input.txt", "r") as f:
        part1_input = f.readlines()
    result = part1(part1_input)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
