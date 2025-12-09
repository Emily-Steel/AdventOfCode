from dataclasses import dataclass
from utils.point2d import Point2D

@dataclass
class Rectangle:
    p1: Point2D
    p2: Point2D

    def area(self) -> int:
        width = abs(self.p2.x - self.p1.x) + 1
        height = abs(self.p2.y - self.p1.y) + 1
        return width * height
    
    def intersects_with_line(self, line_start: Point2D, line_end: Point2D) -> bool:
        rect_min_x = min(self.p1.x, self.p2.x)
        rect_max_x = max(self.p1.x, self.p2.x)
        rect_min_y = min(self.p1.y, self.p2.y)
        rect_max_y = max(self.p1.y, self.p2.y)

        line_min_x = min(line_start.x, line_end.x)
        line_max_x = max(line_start.x, line_end.x)
        line_min_y = min(line_start.y, line_end.y)
        line_max_y = max(line_start.y, line_end.y)

        if (rect_max_x <= line_min_x or rect_min_x >= line_max_x or
            rect_max_y <= line_min_y or rect_min_y >=line_max_y):
            return False
        return True