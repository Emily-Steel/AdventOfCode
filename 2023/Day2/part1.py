import re
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def parse_draw(draw):
    colours = re.findall(r"(\d+) (red|green|blue)", draw)
    return {Color(colour): int(count) for count, colour in colours}


def parse_game(line):
    splits = line.strip().split(";")
    return [parse_draw(split) for split in splits]


def get_max_colors_for_game(game):
    max_colors = {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 0}
    for draw in game:
        for color in Color:
            max_colors[color] = max(max_colors[color], draw.get(color, 0))
    return max_colors


def part1(input_data):
    max_colors_allowed = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}
    possible_games = []
    for i, line in enumerate(input_data):
        game = parse_game(line)
        max_colors = get_max_colors_for_game(game)
        if all(max_colors[color] <= max_colors_allowed[color] for color in Color):
            possible_games.append(i + 1)  # 1-based index
            print(f"Possible game found on line {i + 1}: {line.strip()} with max colors {max_colors}")
    return sum(possible_games)


def main():
    with open("2023/Day2/input.txt", "r") as f:
        part1_input = f.readlines()
    result = part1(part1_input)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
