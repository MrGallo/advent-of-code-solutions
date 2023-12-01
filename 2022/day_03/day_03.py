with open("input.txt", "r") as f:
    sacks = [line.strip() for line in f.readlines()]

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
priorities = dict(zip(lower + upper, range(1, 53)))

priority_sum = 0
for sack in sacks:
    mid = len(sack) // 2
    compartment1 = set(sack[:mid])
    compartment2 = set(sack[mid:])
    letter = list(compartment1 & compartment2)[0]
    priority_sum += priorities[letter]

print(priority_sum)  # part 1: 7785

priority_sum = 0
for i in range(0, len(sacks), 3):
    a = set(sacks[i])
    b = set(sacks[i + 1])
    c = set(sacks[i + 2])
    letter = list(a & b & c)[0]
    priority_sum += priorities[letter]
    
print(priority_sum)  # part 2: 2633
