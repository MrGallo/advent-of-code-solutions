import numpy as np


with open('input.txt') as f:
    claims = []
    for claim in f:
        c_id = int(claim[1:claim.index(" ")])
        at_i = claim.index("@")
        colon_i = claim.index(":")
        x, y = [int(n) for n in claim[at_i+2:colon_i].split(",")]
        w, h = [int(n) for n in claim[colon_i+2:].split("x")]

        claims.append((c_id, x, y, w, h))

grid = np.zeros((1000, 1000), dtype=int)

# Place claims on grid
for c_id, x, y, w, h in claims:
    grid[y:y+h, x:x+w] += 1


# check each claim on the grid
for c_id, x, y, w, h in claims:
    roi = grid[y:y+h, x:x+w]

    if np.all(roi == 1):  # if all cells are 1
        print(c_id)
        break


