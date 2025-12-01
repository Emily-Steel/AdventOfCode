from enum import Enum
from functools import reduce
from operator import mul
import re

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

def parse_draw(draw):
    colours = re.findall(r'(\d+) (red|green|blue)', draw)
    return {Color(colour): int(count) for count, colour in colours}

def parse_game(line):
    splits = line.strip().split(';')
    return [parse_draw(split) for split in splits]

def get_max_colors_for_game(game):
    max_colors = {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 0}
    for draw in game:
        for color in Color:
            max_colors[color] = max(max_colors[color], draw.get(color, 0))
    return max_colors

def part2(input_data):
    game_powers = []
    for i, line in enumerate(input_data):
        game = parse_game(line)
        max_colors = get_max_colors_for_game(game)
        power = reduce(mul, [max_colors[color] for color in Color if max_colors[color] > 0])
        game_powers.append(power)
        print(f"Game on line {i + 1}: {line.strip()} with power {power}")
    return sum(game_powers)

def main():
    with open('2023/Day2/input.txt', 'r') as f:
        part2_input = f.readlines()
    result = part2(part2_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()