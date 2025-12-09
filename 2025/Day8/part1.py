from dataclasses import dataclass
import sys
from pathlib import Path
from utils.dsu import DSU
from utils.point3d import Point3D

SELF_PATH = Path(__file__).parent

def points_to_sorted_distances(points: list[Point3D]) -> list[tuple[int, Point3D, Point3D]]:
    distances = []
    for i, point in enumerate(points):
        for other in points[i+1:]:
            distances.append((point.sq_distance(other), point, other))
    sorted_distances = sorted(distances, key=lambda x: x[0])
    return sorted_distances

def part1(input_data, use_example: bool = False) -> int:
    points = []
    for line in input_data:
        if line == "":
            continue
        point = Point3D.from_string(line)
        points.append(point)
    sorted_distances = points_to_sorted_distances(points)
    circuits = DSU(range(1, len(points) + 1))
    max_connections = 10 if use_example else 1000
    connections_made = 0
    for dist, p1, p2 in sorted_distances:
        circuits.union(p1.id, p2.id)
        connections_made += 1
        if connections_made >= max_connections:
            break
    circuit_sets = circuits.get_sets(*circuits.items())
    print(f"Total circuits found: {len(circuit_sets)}")
    sorted_circuits = sorted(circuit_sets, key=lambda x: len(x), reverse=True)
    answer = 1
    for i in range(min(3, len(sorted_circuits))):
        print(f"Circuit {i+1} has {len(sorted_circuits[i])} points")
        answer *= len(sorted_circuits[i])
    return answer

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = [line.strip() for line in f.readlines()]
    result = part1(day_input, True if "-e" in sys.argv else False)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()