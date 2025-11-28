from fs_parser import FSNode, FSParser


class CommandParser(FSParser):
    def __init__(self, rootNode: FSNode):
        self.root = rootNode

    def parse(self, data: str, cwd: FSNode) -> FSNode | None:
        _, *words = data.split()
        if words[0] == "cd":
            return self.cd(words[1], cwd)
        if words[0] == "ls":
            return self.ls()
        return None

    def cd(self, path: str, cwd: FSNode) -> FSNode:
        if path == "..":
            return cwd.parent
        if path == "/":
            return self.root
        if not cwd.hasChild(path):
            cwd.createChildDir(path)
        return cwd.getChild(path)

    def ls(self) -> None:
        return

    def can_parse_data(self, data: str) -> bool:
        return data.startswith("$")
