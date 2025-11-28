from dataclasses import dataclass
from typing import List


@dataclass
class Tree:
    height: int


forest: List[Tree] = []

with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        row_trees = []
        for tree in row:
            row_trees.append(Tree(int(tree)))
        forest.append(row_trees)


def calculate_scenic_score(start_x, start_y, step_x, step_y):
    x = start_x
    y = start_y
    our_height = forest[y][x].height
    visible_trees = 0
    while x >= 0 and x < len(forest[0]) and y >= 0 and y < len(forest):
        if x != start_x or y != start_y:
            visible_trees += 1
            if forest[y][x].height >= our_height:
                break
        x += step_x
        y += step_y
    return visible_trees


highest_scenic_score = 0

directions = [
    [0, -1],
    [-1, 0],
    [1, 0],
    [0, 1],
]

for tree_y, row in enumerate(forest):
    for tree_x, tree in enumerate(row):
        tree_score = 1
        for x_mod, y_mod in directions:
            direction_score = calculate_scenic_score(tree_x, tree_y, x_mod, y_mod)
            tree_score = tree_score * direction_score
        highest_scenic_score = max(highest_scenic_score, tree_score)

print(f"Highest scenic score of all trees is {highest_scenic_score}")
