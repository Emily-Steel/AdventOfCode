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

def part1(input_data):
    points = parse_points(input_data)
    rectangles = list_all_pairings(points, points)
    areas = [Rectangle(a, b).area() for a, b in rectangles]
    max_area = max(areas)
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