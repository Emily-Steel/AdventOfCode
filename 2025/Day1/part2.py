from typing import Tuple


def rotate_dial(initial_position: int, amount: int) -> Tuple[int, int]:
    zeros_to_add = 0
    dial_position_raw = initial_position + amount
    dial_position = dial_position_raw % 100
    if dial_position == 0 and dial_position_raw == dial_position:
        zeros_to_add = 1
    elif dial_position_raw != dial_position:
        zeros_to_add = abs(int(dial_position_raw / 100))
        if dial_position_raw < 0 and initial_position != 0:
            zeros_to_add += 1
    return dial_position, zeros_to_add


def part2(input_data):
    zeros = 0
    dial_position = 50
    for line in input_data:
        direction = line[0] == "L" and -1 or 1
        amount = int(line[1:])
        new_position, zeros_to_add = rotate_dial(dial_position, direction * amount)
        print(f"{line.strip()} Dial wrapped around from {dial_position} to {new_position}, total zeros: {zeros}, added {zeros_to_add}")
        dial_position = new_position
        zeros += zeros_to_add
    return zeros


def main():
    with open("2025/Day1/input.txt", "r") as f:
        part2_input = f.readlines()
    result = part2(part2_input)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
