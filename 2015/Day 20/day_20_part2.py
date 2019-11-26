"""
Inspired by solution by r_sreeram
https://www.reddit.com/r/adventofcode/comments/3xjpp2/day_20_solutions/?utm_source=share&utm_medium=web2x
"""
from itertools import count
from collections import defaultdict

puzzle_input = 33100000

houses = [0 for _ in range(puzzle_input//11)]


for elf in range(1, puzzle_input//11):
    delivery_count = 0
    for house in range(elf, puzzle_input//11, elf):
        houses[house] += elf * 11
        delivery_count += 1
        if delivery_count == 50:
            break

for i, presents in enumerate(houses):
    if presents >= puzzle_input:
        print(i)
        break


# Answer: 786240