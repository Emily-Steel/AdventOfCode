from dataclasses import dataclass


@dataclass
class Point2D:
    x: int
    y: int
    id: int

    @staticmethod
    def get_autoincrement_id(cls):
        if not hasattr(cls, "_id_counter"):
            cls._id_counter = 0
        cls._id_counter += 1
        return cls._id_counter
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.id = Point2D.get_autoincrement_id(Point2D)

    def sq_distance(self, other: "Point2D") -> int:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def from_string(s: str) -> "Point2D":
        x_str, y_str = s.split(",")
        return Point2D(int(x_str), int(y_str))

    def __hash__(self):
        return hash((self.x, self.y, self.id))