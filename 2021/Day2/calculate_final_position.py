class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, distance: int) -> None:
        self.x += distance

    def up(self, distance: int) -> None:
        self.y -= distance

    def down(self, distance: int) -> None:
        self.y += distance

    def move(self, direction: str, distance: int) -> None:
        movements = {
            "forward": self.forward,
            "up": self.up,
            "down": self.down,
        }
        movements[direction](distance)

    def position_code(self) -> int:
        return self.x * self.y


submarine = Submarine()
with open("input.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        direction, distance = row.split()
        submarine.move(direction, int(distance))

print(f"Final position code: {submarine.position_code()}")
