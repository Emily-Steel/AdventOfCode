from operator import add, mul
import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def get_columns(operator_row: str):
    symbol_map = {
        "+": add,
        "*": mul
    }
    column_starting_index = 0
    column_operator = symbol_map[operator_row[0]]
    i = 1
    while i < len(operator_row):
        if operator_row[i] in symbol_map:
            yield column_starting_index, i - 2, column_operator
            column_starting_index = i
            column_operator = symbol_map[operator_row[i]]
        i += 1
    yield column_starting_index, len(operator_row) - 1, column_operator

def part2(input_data):
    equation_results = []
    operand_rows = input_data[:-1]
    for start_idx, end_idx, operator in get_columns(input_data[-1]):
        current_result = None
        for j in range(end_idx, start_idx - 1, -1):
            current_operand = ""
            for row in operand_rows:
                current_operand += row[j]
            if current_result is None:
                current_result = int(current_operand)
            else:
                current_result = operator(int(current_operand), current_result)
        equation_results.append(current_result)
    return sum(equation_results)

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = f.readlines()
    result = part2(day_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()