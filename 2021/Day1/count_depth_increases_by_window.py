from typing import List


class DepthWindow:
    def __init__(self, window_size: int = 3):
        self.data: List[int] = []
        self.window_size: int = window_size
        self.did_depth_increase: bool = False

    def add_depth_reading(self, depth: int) -> None:
        if len(self.data) < self.window_size:
            self.data.append(depth)
            return
        old_window_sum = sum(self.data)
        popped_value = self.data.pop(0)
        self.data.append(depth)
        new_window_sum = old_window_sum - popped_value + depth
        self.did_depth_increase = new_window_sum > old_window_sum


depth_window = DepthWindow()
depth_increases = 0
with open("sonar_readings.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        if not row:
            continue
        depth = int(row)
        depth_window.add_depth_reading(depth)
        if depth_window.did_depth_increase:
            depth_increases += 1

print(f"Times that depth increased: {depth_increases}")
