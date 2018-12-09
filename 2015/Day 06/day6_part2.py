import re
import numpy as np


with open('input.txt') as f:
    instructions_raw = [line.strip() for line in f]

grid = np.zeros((1000, 1000), dtype=int)

for line in instructions_raw:
    action = re.search(r'^(.*?)\s[0-9]+', line).group(1)
    point1 = tuple(int(n) for n in re.search(r'^.+?([0-9]+\,[0-9]+)\s', line).group(1).split(','))
    point2 = tuple(int(n) for n in re.search(r'through ([0-9]+\,[0-9]+)', line).group(1).split(','))

    (x1, y1), (x2, y2) = point1, point2

    section = np.index_exp[y1:y2 + 1, x1:x2 + 1]
    if action == 'turn on':
        grid[section] += 1
    elif action == 'turn off':
        kernel = grid[section] - 1
        grid[section] = kernel.clip(0)
    elif action == 'toggle':
        grid[section] += 2

print(np.sum(grid))  # answer: 14687245
