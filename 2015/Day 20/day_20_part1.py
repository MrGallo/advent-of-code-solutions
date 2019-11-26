"""
Inspired by solution by r_sreeram
https://www.reddit.com/r/adventofcode/comments/3xjpp2/day_20_solutions/?utm_source=share&utm_medium=web2x
"""


puzzle_input = 33100000

houses = [0 for _ in range(puzzle_input//10)]

for elf in range(1, puzzle_input//10):
    for house in range(elf, puzzle_input//10, elf):
        houses[house] += elf * 10

for i, presents in enumerate(houses):
    if presents >= puzzle_input:
        print(i)
        break

# answer: 776160