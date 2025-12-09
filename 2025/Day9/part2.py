import sys
from pathlib import Path
from utils import list_all_pairings
from utils.point2d import Point2D
from utils.rectangle import Rectangle

SELF_PATH = Path(__file__).parent

def parse_points(input_data) -> list[Point2D]:
    points = []
    for line in input_data:
        if line == "":
            continue
        point = Point2D.from_string(line)
        points.append(point)
    return points

def create_sequential_pairs(points: list[Point2D]) -> list[tuple[Point2D, Point2D]]:
    pairs = []
    for i in range(len(points) - 1):
        pairs.append((points[i], points[i + 1]))
    return pairs

def part1(input_data):
    points = parse_points(input_data)
    polygon_edges = create_sequential_pairs(points)
    rectangles = [Rectangle(a, b) for a, b in list_all_pairings(points, points)]
    sorted_rectangles = sorted(rectangles, key=lambda r: r.area(), reverse=True)
    max_area = 0
    for rect in sorted_rectangles:
        print(f"Checking rectangle with area {rect.area()}")
        for edge_start, edge_end in polygon_edges:
            if rect.intersects_with_line(edge_start, edge_end):
                break
        else:
            max_area = rect.area()
            break
    return max_area

def main():
    filename = "example.txt" if "-e" in sys.argv else "input.txt"
    with open(SELF_PATH / filename, "r") as f:
        day_input = f.readlines()
    result = part1(day_input)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python part1.py [-e] [--help|-h]\n-e : use example input\n--help|-h : show this help message")
        sys.exit(0)
    main()