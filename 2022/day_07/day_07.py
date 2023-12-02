from typing import Optional, List, Tuple, Set



class File:
    def __init__(self, name: str, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"] = None):
        self.name = name
        self.parent = parent
        self.files: list[File] = []
        self.directories: list["Directory"] = []
    
    def __repr__(self) -> str:
        parent_name = self.parent.name if self.parent is not None else "None"
        return f"Directory(name={self.name}, parent={parent_name})"


    def print_tree(self, level = 1, tab_size = 4):
        print(" " * ((level-1) * tab_size) + self.name + "/")
        for dir in self.directories:
            dir.print_tree(level=level + 1)
        
        for file in self.files:
            print(" " * (level * tab_size) + file.name + f" (file, size={file.size})")
        
    def get_size(self, visited: Optional[Set[Tuple["Directory", int]]] = None) -> int:
        if visited is None:
            visited = {}
        
        # if visited.get(self, False):
        #     return visited[self]

        size = 0

        for file in self.files:
            size += file.size
        
        for child_dir in self.directories:
            size += child_dir.get_size(visited)
        
        visited[self] = size
        return size

    def find_dirs_with_size(self):
        visited = {}
        self.get_size(visited)
        return tuple(visited.items())


terminal_lines = []
with open("input.txt", "r") as f:
    terminal_lines = [line.strip().split() for line in f.readlines()]

print(terminal_lines)
root = Directory("")
pwd = root
for line in terminal_lines[1:]:
    if line[0] == "$":
        cmd = line[1]
        if cmd == "cd":
            arg = line[2]
            if arg == "..":
                pwd = pwd.parent
            else:
                new_dir = Directory(arg, parent=pwd)
                pwd.directories.append(new_dir)
                pwd = new_dir
    elif line[0] != "dir":
        size, name = line
        size = int(size)
        pwd.files.append(File(name, size))

    
root.print_tree()
dirs = root.find_dirs_with_size()
print(sum(size for dir, size in dirs if size < 100_000))  # Part 1: 1297159

MAX_CAPACITY = 70_000_000
REQUIRED_STORAGE = 30_000_000

root_size = root.get_size()
for dir, size in sorted(dirs, key=lambda a: a[1]):
    remaining = MAX_CAPACITY - root_size + size
    if remaining > REQUIRED_STORAGE:
        found = dir, size
        break

print(size)  # Part 2: 3866390