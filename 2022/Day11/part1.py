# Monkey 0:
#   Starting items: 91, 54, 70, 61, 64, 64, 60, 85
#   Operation: new = old * 13
#   Test: divisible by 2
#     If true: throw to monkey 5
#     If false: throw to monkey 2

from collections import deque
from dataclasses import dataclass
import sys
from typing import Callable, List
from pathlib import Path

from monkey_parse import (
    parse_false,
    parse_monkey_num,
    parse_operation,
    parse_starting_items,
    parse_test,
    parse_true,
)

SELF_PATH = Path(__file__).parent

@dataclass
class Monkey:
    id: int
    inventory: deque[int]
    operation: Callable[[int], int]
    operation_label: str
    divisible_by: int
    pass_when_true: int
    pass_when_false: int
    total_inspections: int = 0

def print_monkeys(monkeys: List[Monkey], extended_info: bool = False) -> None:
    for monkey in monkeys:
        inv = ", ".join([str(x) for x in monkey.inventory])
        print(f"Monkey {monkey.id}: {inv}")
        if extended_info:
            print(f"  Operation: {monkey.operation_label}")
            print(f"  Test: divisible by {monkey.divisible_by}")
            print(f"    If true: throw to monkey {monkey.pass_when_true}")
            print(f"    If false: throw to monkey {monkey.pass_when_false}")
    print()

def part1(input_data) -> int:
    monkeys: List[Monkey] = []

    rows = [r.strip() for r in input_data]
    i = 0
    while i < len(rows):
        num = parse_monkey_num(rows[i])
        starting_items = parse_starting_items(rows[i + 1])
        operation, operation_label = parse_operation(rows[i + 2])
        test = parse_test(rows[i + 3])
        pass_true = parse_true(rows[i + 4])
        pass_false = parse_false(rows[i + 5])
        monkeys.append(Monkey(num, starting_items, operation, operation_label, test, pass_true, pass_false))
        i += 7  # Skip blank line
    print("Initial state:")
    print_monkeys(monkeys, extended_info=True)
    for round_number in range(20):
        for monkey in monkeys:
            while len(monkey.inventory) > 0:
                monkey.total_inspections += 1
                item = monkey.inventory.popleft()
                print(f"Monkey {monkey.id} inspects item {item}")
                item = monkey.operation(item)
                print(f"  Worry level after operation: {item} ({monkey.operation_label})")
                item = item // 3
                print(f"  Worry level after relief: {item}")
                if item % monkey.divisible_by == 0:
                    target_monkey = monkey.pass_when_true
                else:
                    target_monkey = monkey.pass_when_false
                monkeys[target_monkey].inventory.append(item)
        print(f"After round {round_number + 1}:")
        print_monkeys(monkeys)

    inspection_counts = sorted([m.total_inspections for m in monkeys], reverse=True)
    result = inspection_counts[0] * inspection_counts[1]
    return result

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