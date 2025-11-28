from collections import deque


def parse_monkey_num(row: str) -> None:
    row = row.removeprefix("Monkey ").removesuffix(":")
    return int(row)


def parse_starting_items(row: str) -> None:
    row = row.removeprefix("Starting items: ")
    return deque([int(x) for x in row.split(", ")])


def parse_operation(row: str) -> None:
    row = row.removeprefix("Operation: new = old ")
    words = row.split()
    if words[0] == "+":
        return lambda old: old + int(words[1])
    if words[0] == "*":
        if words[1] == "old":
            return lambda old: old * old
        return lambda old: old * int(words[1])


def parse_test(row: str) -> None:
    row = row.removeprefix("Test: divisible by ")
    return int(row)


def parse_true(row: str) -> None:
    row = row.removeprefix("If true: throw to monkey ")
    return int(row)


def parse_false(row: str) -> None:
    row = row.removeprefix("If false: throw to monkey ")
    return int(row)
