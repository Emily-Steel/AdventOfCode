# Monkey 0:
#   Starting items: 91, 54, 70, 61, 64, 64, 60, 85
#   Operation: new = old * 13
#   Test: divisible by 2
#     If true: throw to monkey 5
#     If false: throw to monkey 2

from collections import deque
from dataclasses import dataclass
from typing import Callable, List

from monkey_parse import (
    parse_false,
    parse_monkey_num,
    parse_operation,
    parse_starting_items,
    parse_test,
    parse_true,
)


@dataclass
class Monkey:
    id: int
    inventory: deque[int]
    operation: Callable[[int], int]
    divisible_by: int
    pass_when_true: int
    pass_when_false: int
    total_inspections: int = 0


monkeys: List[Monkey] = []
with open("input.txt", "r") as rows:
    rows = deque(filter(None, [r.strip() for r in rows.readlines()]))
    while len(rows) > 0:
        num = parse_monkey_num(rows.popleft())
        starting_items = parse_starting_items(rows.popleft())
        operation = parse_operation(rows.popleft())
        test = parse_test(rows.popleft())
        pass_true = parse_true(rows.popleft())
        pass_false = parse_false(rows.popleft())
        monkeys.append(Monkey(num, starting_items, operation, test, pass_true, pass_false))

print(monkeys)

for round_number in range(20):
    for monkey in monkeys:
        while len(monkey.inventory) > 0:
            monkey.total_inspections += 1
            item = monkey.inventory.popleft()
            item = operation(item) // 3
            if item % monkey.divisible_by == 0:
                target_monkey = monkey.pass_when_true
            else:
                target_monkey = monkey.pass_when_false
            monkeys[target_monkey].inventory.append(item)
    print(f"After round {round_number}:")
    for monkey in monkeys:
        inv = ", ".join([str(x) for x in monkey.inventory])
        print(f"Monkey {monkey.id}: {inv}")
    print()

inspection_counts = sorted([m.total_inspections for m in monkeys], reverse=True)
result = inspection_counts[0] * inspection_counts[1]
print(f"Total monkey business was {result}")
