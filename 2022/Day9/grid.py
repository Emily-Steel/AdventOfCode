from dataclasses import dataclass
from typing import List, Set


@dataclass
class Coord:
    x: int = 0
    y: int = 0

    def __hash__(self):
        return (self.x, self.y).__hash__()


class Grid:
    head: Coord
    tail: List[Coord]

    tail_visited: Set[Coord]

    def __init__(self):
        self.head = Coord()
        self.tail = []
        for _ in range(9):
            self.tail.append(Coord())
        self.tail_visited = set([Coord()])

    def setHead(self, x: int, y: int) -> None:
        self.head = Coord(x, y)

    def setTail(self, tail_idx: int, x: int, y: int) -> None:
        self.tail[tail_idx] = Coord(x, y)
        if tail_idx == (len(self.tail) - 1):
            self.tail_visited.add(Coord(x, y))
