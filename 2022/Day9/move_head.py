from grid import Grid


def move_head(grid: Grid, direction: str):
    x_step, y_step = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }[direction]
    x = grid.head.x + x_step
    y = grid.head.y + y_step
    grid.setHead(x, y)
