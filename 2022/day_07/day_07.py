from typing import Optional


terminal_lines = []
with open("test.txt", "r") as f:
    terminal_lines = [line.strip().split() for line in f.readlines()]

print(terminal_lines)

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


root = Directory("/")
pwd = root
for line in terminal_lines[1:]:
    if line[0] == "$":
        cmd = line[1]
        if cmd == "cd":
            arg = line[2]
            if arg == "..":
                pwd = pwd.parent
            else:
                new_dir = Directory(dir_name, parent=pwd)
                pwd.directories.append(new_dir)
                pwd = new_dir
    # elif line[0] == "dir":
    #     dir_name = line[1]
    #     pwd.directories.append(Directory(dir_name, parent=pwd))
    else:
        size, name = line
        size = int(size)
        pwd.files.append(File(name, size))

def print_tree(root: Directory, level = 1):
    print(root.name)
    for dir in root.directories:
        print(" " * (level * 2) + dir.name + " (dir)")
    
    for file in root.files:
        print(" " * (level * 2) + file.name + f" (file, size={file.size})")
    
    for dir in root.directories:
        print_tree(dir, level + 1)


print_tree(root)