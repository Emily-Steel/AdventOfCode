from operator import add, mul
import sys
from pathlib import Path

SELF_PATH = Path(__file__).parent

def symbol_to_operator(symbol: str):
    symbol_map = {
        "+": add,
        "*": mul
    }
    return symbol_map.get(symbol)

def part1(input_data):
    operators = [symbol_to_operator(symbol) for symbol in input_data[-1].split()]
    equation_results = [None] * len(operators)
    for line in input_data[:-1]:
        operands = line.split()
        for i, operator in enumerate(operators):
            if equation_results[i] is None:
                equation_results[i] = int(operands[i])
            else:
                equation_results[i] = operator(equation_results[i], int(operands[i]))
    return sum(equation_results)

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = f.readlines()
    lines = [line.strip() for line in day_input if line.strip()]
    result = part1(lines)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()