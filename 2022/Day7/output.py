from fs_parser import FSNode, FSParser


class OutputParser(FSParser):
    def __init__(self, rootNode: FSNode):
        self.root = rootNode

    def parse(self, data: str, cwd: FSNode) -> FSNode | None:
        words = data.split()
        if cwd.hasChild(words[1]):
            return
        if words[0] == "dir":
            cwd.createChildDir(words[1])
            return
        if words[0].isnumeric():
            cwd.createChildFile(words[1], int(words[0]))

    def can_parse_data(self, data: str) -> bool:
        return not data.startswith("$")
