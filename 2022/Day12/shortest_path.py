from dataclasses import dataclass
from typing import List


@dataclass
class GraphNode:
    value: int
    distance_from_goal: int
    links: List["GraphNode"]


def parse_input(file_name: str) -> List[List[GraphNode]]:
    nodes = []
    with open(file_name, "r") as rows:
        for row in rows.readlines():
            row = row.strip()
            nodes.append([])
