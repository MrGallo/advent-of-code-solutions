MAPPING = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

with open('input.txt') as f:
    directions = f.read()

current_loc_santa = current_loc_robo = (0, 0)
visited = set([current_loc_santa])

for i in range(0, len(directions), 2):
    direction_santa = directions[i]
    direction_robo = directions[i+1]

    x, y = current_loc_santa
    dx, dy = MAPPING[direction_santa]
    current_loc_santa = x+dx, y+dy

    x, y = current_loc_robo
    dx, dy = MAPPING[direction_robo]
    current_loc_robo = x+dx, y+dy

    visited.add(current_loc_santa)
    visited.add(current_loc_robo)

print(len(visited))  # answer: 2631
