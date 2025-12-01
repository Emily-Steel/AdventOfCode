from typing import List

from utils import first_and_last_element, spelled_out_digit_to_int

SPELLED_OUT_DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

DIGIT_STATE_MACHINE = {
    "z": {"e": {"r": {"o": "zero"}}},
    "o": {"n": {"e": "one"}},
    "t": {"w": {"o": "two"}, "h": {"r": {"e": {"e": "three"}}}},
    "f": {"o": {"u": {"r": "four"}}, "i": {"v": {"e": "five"}}},
    "s": {"i": {"x": "six"}, "e": {"v": {"e": {"n": "seven"}}}},
    "e": {"i": {"g": {"h": {"t": "eight"}}}},
    "n": {"i": {"n": {"e": "nine"}}},
}


def digits_from_string_including_spelled_out(input: str) -> list[int]:
    digits = []
    current_state = None
    i = 0
    head = 0
    while i < len(input):
        char = input[i]
        if char.isdigit():
            digits.append(int(char))
            current_state = None
            i += 1
            continue
        if current_state is None:
            if char in DIGIT_STATE_MACHINE:
                current_state = DIGIT_STATE_MACHINE[char]
                head = i
        else:
            if char in current_state:
                next_state = current_state[char]
                if isinstance(next_state, str):
                    # Completed a spelled-out digit
                    digits.append(spelled_out_digit_to_int(next_state))
                    current_state = None
                    i = head  # Reset to character after the start of the spelled-out digit
                else:
                    current_state = next_state
            else:
                i = head
                current_state = None
        i += 1
    return digits


def part2(input: List[str]) -> int:
    calibration_values = []
    for line in input:
        print(f"Processing line: {line.strip()}")
        numbers = digits_from_string_including_spelled_out(line)
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
        part2_input = f.readlines()
    result = part2(part2_input)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
