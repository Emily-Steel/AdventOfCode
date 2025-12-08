from dataclasses import dataclass
import sys
from pathlib import Path
from utils.dsu import DSU

SELF_PATH = Path(__file__).parent

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
        return hash((self.x, self.y, self.z))

def points_to_sorted_distances(points: list[Point3D]) -> list[tuple[int, Point3D, Point3D]]:
    distances = []
    for i, point in enumerate(points):
        for other in points[i+1:]:
            distances.append((point.sq_distance(other), point, other))
    sorted_distances = sorted(distances, key=lambda x: x[0])
    return sorted_distances

def part2(input_data, use_example: bool = False) -> int:
    points = []
    for line in input_data:
        if line == "":
            continue
        point = Point3D.from_string(line)
        points.append(point)
    sorted_distances = points_to_sorted_distances(points)
    circuits = DSU(range(1, len(points) + 1))
    total_circuits = len(points)
    result = 0
    for dist, p1, p2 in sorted_distances:
        if circuits.union(p1.id, p2.id):
            total_circuits -= 1
        if total_circuits == 1:
            print("All points connected")
            result = p1.x * p2.x
            break
    return result

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part2(day_input, True if "-e" in sys.argv else False)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part2.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()