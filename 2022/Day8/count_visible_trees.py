from dataclasses import dataclass
from typing import List


@dataclass
class Tree:
    height: int
    visible: bool


forest: List[Tree] = []

with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        row_trees = []
        for tree in row:
            row_trees.append(Tree(int(tree), False))
        forest.append(row_trees)

# W -> E && E -> W
for row in forest:
    for direction in [iter(row), reversed(row)]:
        tallest_so_far = -1
        for tree in direction:
            if tree.height > tallest_so_far:
                tree.visible = True
                tallest_so_far = tree.height

# N -> S && S -> N
for direction in [iter(forest), reversed(forest)]:
    tallest_for_columns = [-1] * len(forest[0])
    for row in direction:
        for i, tree in enumerate(row):
            if tree.height > tallest_for_columns[i]:
                tree.visible = True
                tallest_for_columns[i] = tree.height

total_visible_trees = 0
for row in forest:
    for tree in row:
        if tree.visible:
            total_visible_trees += 1

for row in forest:
    rowstr = ""
    for tree in row:
        rowstr += str(tree.height)
    print(rowstr)

for row in forest:
    rowstr = ""
    for tree in row:
        rowstr += "V" if tree.visible else "."
    print(rowstr)


print(f"Total of visible trees is {total_visible_trees}")
