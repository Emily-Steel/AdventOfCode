import pytest
from utils.rectangle import Rectangle
from utils.point2d import Point2D

def test_rectangle_area():
    rect = Rectangle(Point2D(2, 5), Point2D(11, 1))
    assert rect.area() == 50
