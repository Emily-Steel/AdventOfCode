from typing import List

from command import CommandParser
from node import FSNode
from output import OutputParser

root = FSNode("/", None, [], 0)
cwd = root
parsers = [CommandParser(root), OutputParser(root)]

with open("input.txt", "r") as commands:
    for command in commands.readlines():
        command = command.strip()
        for parser in parsers:
            if parser.can_parse_data(command):
                ret_val = parser.parse(command, cwd)
                if ret_val is not None:
                    cwd = ret_val

root.print_tree()

free_space = 70000000 - root.size
needed_space = 30000000
space_to_free = needed_space - free_space


def rec_detect_suitable_folders(cursor: FSNode) -> List[FSNode]:
    detected = []
    if cursor.size >= space_to_free and len(cursor.children) > 0:
        detected.append(cursor)
    for child in cursor.children:
        detected = detected + rec_detect_suitable_folders(child)
    return detected


smallest_suitable = min([x.size for x in rec_detect_suitable_folders(root)])

print(f"Size of folder to delete is {smallest_suitable}")
