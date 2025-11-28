from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class FSNode:
    name: str
    parent: "FSNode"
    children: List["FSNode"]
    size: int

    def getChild(self, name: str) -> "FSNode" | None:
        return next(filter(lambda x: x.name == name, self.children), None)

    def hasChild(self, name: str) -> bool:
        return self.getChild(name) is not None

    def createChildDir(self, name: str) -> FSNode:
        child = FSNode(name, self, [], 0)
        self.children.append(child)
        return child

    def createChildFile(self, name: str, size: int) -> FSNode:
        child = FSNode(name, self, [], size)
        self.children.append(child)
        cursor = child.parent
        while cursor is not None:
            cursor.size += size
            cursor = cursor.parent
        return child

    def print_tree(self, indent=0):
        indent_block = " " * indent
        type_label = "dir" if len(self.children) > 0 else "file"
        print(f"{indent_block}- {self.name} ({type_label}) size {self.size}")
        for child in self.children:
            child.print_tree(indent + 2)
