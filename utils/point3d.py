from dataclasses import dataclass


@dataclass
class Point3D:
    x: int
    y: int
    z: int
    id: int

    @staticmethod
    def get_autoincrement_id(cls):
        if not hasattr(cls, "_id_counter"):
            cls._id_counter = 0
        cls._id_counter += 1
        return cls._id_counter
    
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.id = Point3D.get_autoincrement_id(Point3D)

    def sq_distance(self, other: "Point3D") -> int:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def from_string(s: str) -> "Point3D":
        x_str, y_str, z_str = s.split(",")
        return Point3D(int(x_str), int(y_str), int(z_str))

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.id))