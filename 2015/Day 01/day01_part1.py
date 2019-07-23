import os
from collections import Counter

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

instruction_map = {
    '(': 1,
    ')': -1,
}

with open('input.txt', 'r') as f:
    instruction_count = Counter(f.read())


print(sum(instruction_map[instruction] * count
          for instruction, count in instruction_count.items()))

#  result: 280
