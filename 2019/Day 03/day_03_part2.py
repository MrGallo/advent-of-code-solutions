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

locations = {
    0: defaultdict(int),
    1: defaultdict(int)
}

overlaping_locations = []
for i, wire in enumerate(wires):
    x = 0
    y = 0
    steps = 0
    for instruction in wire:
        direction = instruction[0]
        amount = int(instruction[1:])

        dx, dy = DIRECTIONS[direction]
        while amount:
            steps += 1
            x += dx
            y += dy

            if locations[i][(x, y)] == 0:
                locations[i][(x, y)] = steps

            if i == 1 and locations[0][(x, y)] != 0:
                overlaping_locations.append((x, y))

            amount -= 1


print(overlaping_locations)

min_steps = None
for location in overlaping_locations:
    steps = locations[0][location] + locations[1][location]
    if min_steps is None or steps < min_steps:
        min_steps = steps

print(min_steps)  # answer: 37390
