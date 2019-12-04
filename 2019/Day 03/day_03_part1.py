# TODO: Consider better approach


from collections import defaultdict


with open('input.txt', 'r') as f:
    wires = [wire.split(",") for wire in f.read().split("\n")]

DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

locations = defaultdict(int)
overlaping_locations = []

for i, wire in enumerate(wires):
    x = 0
    y = 0
    for instruction in wire:
        direction = instruction[0]
        amount = int(instruction[1:])

        dx, dy = DIRECTIONS[direction]
        while amount:
            x += dx
            y += dy

            locations[(x, y)] |= 2**i
            if locations[(x, y)] == 3:
                overlaping_locations.append((x, y))

            amount -= 1


print(overlaping_locations)

min_distance = None
for x, y in overlaping_locations:
    distance = abs(x) + abs(y)
    if min_distance is None or distance < min_distance:
        min_distance = distance

print(min_distance)  # answer: 1264
