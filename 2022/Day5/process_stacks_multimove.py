from collections import deque
from itertools import repeat
from queue import LifoQueue as Queue
from typing import List


class StateMachine:
    def enter(self, crates: List[Queue]): ...

    def process(self, row: str): ...

    def exit(self) -> List[Queue]: ...


state_transition: StateMachine | None = None


class GatherCrates(StateMachine):
    def __init__(self):
        self.raw_crates = deque()

    def process(self, row: str):
        if "[" in row:
            self.raw_crates.appendleft(row)
        else:
            self.crates_key = []
            for idx, character in enumerate(row):
                if character.isnumeric():
                    self.crates_key.append(idx)
            global state_transition
            state_transition = ProcessMoves()

    def exit(self) -> List[Queue]:
        stacks: List[Queue] = []
        for _ in repeat(None, len(self.crates_key)):
            stacks.append(Queue())
        for row in self.raw_crates:
            for key_idx, row_idx in enumerate(self.crates_key):
                if len(row) > row_idx and row[row_idx] != " ":
                    stacks[key_idx].put(row[row_idx])
        return stacks


class ProcessMoves(StateMachine):
    def enter(self, crates: List[Queue]):
        self.stacks = crates

    def process(self, row: str):
        move_this_much, source, target = [int(x) for x in row.split() if x.isnumeric()]
        print(f"Moving {move_this_much} from {source} to {target}")
        crates_to_move = deque()
        for _ in repeat(None, move_this_much):
            crate = self.stacks[source - 1].get()
            crates_to_move.appendleft(crate)
        for crate in crates_to_move:
            self.stacks[target - 1].put(crate)

    def exit(self) -> List[Queue]:
        return self.stacks


row_processor: StateMachine = GatherCrates()


def print_stacks(stacks: List[Queue]):
    for x in range(3):
        for stack in stacks:
            if stack.qsize() < 3 - x:
                print(" ", end=" ")
            else:
                print(stack.get(), end=" ")
        print()


with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.rstrip()
        print(f"'{row}' len {len(row)}")
        if not row:
            print("Skip")
            continue
        if state_transition is not None:
            print("Transition")
            print("Exit")
            crates = row_processor.exit()
            print("Transpose")
            row_processor = state_transition
            print("Enter")
            row_processor.enter(crates)
            print("Conclude")
            state_transition = None
        print("Process")
        row_processor.process(row)

final_values = []
for stack in row_processor.exit():
    final_values.append(stack.get())

final_values = "".join(final_values)
print(f"Final topmost crates are: {final_values}")
