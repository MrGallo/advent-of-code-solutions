from collections import Counter

with open('input.txt') as f:
    box_ids = [line.strip() for line in f]

twos = 0
threes = 0

for box_id in box_ids:
    count = Counter(box_id)

    values = count.values()
    if 2 in values:
        twos += 1
    if 3 in values:
        threes += 1

print(twos*threes)
