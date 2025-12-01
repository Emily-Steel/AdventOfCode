import pytest
from part1 import Color, get_max_colors_for_game, parse_draw, parse_game, part1


def test_example():
    with open('2023/Day2/example.txt', 'r') as f:
        input_data = f.readlines()
    result = part1(input_data)
    assert result == [1, 2, 5]

def test_parse_draw():
    draw = "3 red, 2 blue, 5 green"
    parsed = parse_draw(draw)
    assert parsed == {
        Color.RED: 3,
        Color.BLUE: 2,
        Color.GREEN: 5
    }

def test_parse_game():
    line = "3 red, 2 blue; 1 green, 4 red"
    parsed = parse_game(line)
    assert parsed == [
        {Color.RED: 3, Color.BLUE: 2},
        {Color.GREEN: 1, Color.RED: 4}
    ]

def test_max_colors_for_game():
    game = [
        {Color.RED: 3, Color.BLUE: 2, Color.GREEN: 1},
        {Color.GREEN: 5, Color.RED: 1, Color.BLUE: 4},
        {Color.RED: 6, Color.BLUE: 1, Color.GREEN: 2},
        {Color.GREEN: 3, Color.RED: 2, Color.BLUE: 5}
    ]
    max_colors = get_max_colors_for_game(game)
    assert max_colors == {
        Color.RED: 6,
        Color.BLUE: 5,
        Color.GREEN: 5
    }

def test_max_colors_for_game_sparse_colors():
    game = [
        {Color.RED: 10},
        {Color.BLUE: 8, Color.GREEN: 3},
        {Color.RED: 2, Color.GREEN: 7},
        {Color.BLUE: 12}
    ]
    max_colors = get_max_colors_for_game(game)
    assert max_colors == {
        Color.RED: 10,
        Color.BLUE: 12,
        Color.GREEN: 7
    }