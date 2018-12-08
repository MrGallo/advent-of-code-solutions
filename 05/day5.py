# Day 5: Alchemical Reduction
from collections import Counter

def reaction(e1, e2):
    return e1.lower() == e2.lower() and e1 != e2
    

def get_reacted_length(polymer, problem_unit=''):
    i = 0
    while i < len(polymer)-1:
        c1, c2 = polymer[i], polymer[i+1]
        # if c1.lower() == problem_unit.lower():
        #     polymer = polymer[:i] + polymer[i+1:]
        #     i = max(i-1, 0)
        if reaction(c1, c2):
            polymer = polymer[:i] + polymer[i+2:]
            i = max(i-1, 0)
        else:
            i += 1
    return len(polymer)
    
print("Day 5: Alchemical Reduction")

print("Part 1:")
with open('input.txt') as f:
    polymer = f.read()

# print(get_reacted_length(polymer))

print("Part 2:")

# figure out highest blocking unit count
# polymer = "dabAcCaCBAcCcaDA"

# unit_counts = Counter()
# i = 1
# while i < len(polymer)-1:
#     unit = polymer[i]
#     before, after = polymer[i-1], polymer[i+1]
#     adjust = 0
#     while not reaction(unit, after) and unit.lower() == after.lower():
#         adjust += 1
#         try:
#             after = polymer[i+1+adjust]
#         except IndexError:
#             adjust -= 1
#             break
#     if reaction(before, after):
#         unit_counts[unit.lower()] += 1
#     i += 1 + adjust

# print(unit_counts)
# problem_unit = unit_counts.most_common(1)[0][0]
units = Counter(polymer.lower()).keys()
unit_lengths = []
for unit in units:
    unit_lengths.append((get_reacted_length(polymer.replace(unit, "").replace(unit.upper(), "")), unit))

print(sorted(unit_lengths))