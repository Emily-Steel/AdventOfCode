from grid import Grid


def move_tail(grid: Grid, tail_idx: int):
    prev = grid.head if tail_idx == 0 else grid.tail[tail_idx - 1]
    x = grid.tail[tail_idx].x
    y = grid.tail[tail_idx].y
    normalised_prev_x = prev.x - x
    normalised_prev_y = prev.y - y

    if abs(normalised_prev_x) < 2 and abs(normalised_prev_y) < 2:
        return
    x_step, y_step = {
        (2, 0): (1, 0),
        (-2, 0): (-1, 0),
        (0, 2): (0, 1),
        (0, -2): (0, -1),
        (-2, 1): (-1, 1),
        (-2, -1): (-1, -1),
        (-1, 2): (-1, 1),
        (1, 2): (1, 1),
        (2, 1): (1, 1),
        (2, -1): (1, -1),
        (1, -2): (1, -1),
        (-1, -2): (-1, -1),
        (-2, -2): (-1, -1),
        (-2, 2): (-1, 1),
        (2, -2): (1, -1),
        (2, 2): (1, 1),
    }[(normalised_prev_x, normalised_prev_y)]
    x += x_step
    y += y_step
    grid.setTail(tail_idx, x, y)
