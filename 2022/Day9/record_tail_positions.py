from grid import Grid
from move_head import move_head
from move_tail import move_tail

grid = Grid()

with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        direction, times = row.split()
        for _ in range(int(times)):
            move_head(grid, direction)
            for i in range(len(grid.tail)):
                move_tail(grid, i)

total = len(grid.tail_visited)
print(f"Total unique tail positions: {total}")
