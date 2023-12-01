pairs = []
with open("input.txt", "r") as f:
    for pair in f.read().split("\n"):
        pairs.append(pair.split(","))

count = 0
for a, b in pairs:
    a_start, a_end = map(int, a.split("-"))
    b_start, b_end = map(int, b.split("-"))
    if (a_start <= b_start and a_end >= b_end or
        b_start <= a_start and b_end >= a_end):
        count += 1

print(count)  # part 1: 453

count = 0
for a, b in pairs:
    a_start, a_end = map(int, a.split("-"))
    b_start, b_end = map(int, b.split("-"))
    a_assignment = set(range(a_start, a_end + 1))
    b_assignment = set(range(b_start, b_end + 1))
    
    if len(a_assignment & b_assignment) > 0:
        count += 1

print(count)  # part 2: 
