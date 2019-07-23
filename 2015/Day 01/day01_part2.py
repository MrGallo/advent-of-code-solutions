import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

instruction_map = {
    '(': 1,
    ')': -1,
}

floor = 0
i = 0
with open('input.txt', 'r') as f:
    while floor != -1:
        instruction = f.read(1)
        try:
            floor += instruction_map[instruction]
            i += 1
        except KeyError:
            break

print(i)
