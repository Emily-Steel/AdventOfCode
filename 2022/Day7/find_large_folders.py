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


def rec_detect_large_folders(cursor: FSNode) -> List[FSNode]:
    detected = []
    if cursor.size <= 100000 and len(cursor.children) > 0:
        detected.append(cursor)
    for child in cursor.children:
        detected = detected + rec_detect_large_folders(child)
    return detected


detected = rec_detect_large_folders(root)
for x in detected:
    print(f"{x.size} {x.name}")

total_size = 0
for item in detected:
    total_size += item.size

print(f"Total size of large folders is {total_size}")
