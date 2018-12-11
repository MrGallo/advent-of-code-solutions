import numpy as np

GRID_SERIAL = 9435
GRID_SIZE = 300


def get_power_level(cell):
    x, y, = cell
    rack_id = x + 10
    power = rack_id * y
    power += GRID_SERIAL
    power *= rack_id
    power = power // 100 % 10
    power -= 5

    return power


grid_cells = [(x, y) for x in range(1, GRID_SIZE + 1) for y in range(1, GRID_SIZE + 1)]

grid_power = [get_power_level(cell) for cell in grid_cells]

grid_power = np.array(grid_power)
grid_power.shape = (GRID_SIZE, GRID_SIZE)

highest = None
for roi_size in range(1, GRID_SIZE):
    for i in range(GRID_SIZE - roi_size + 1):
        for j in range(GRID_SIZE - roi_size + 1):
            roi = grid_power[i:i+roi_size, j:j+roi_size]
            cell_sum = np.sum(roi)

            if not highest or cell_sum > highest[2]:
                grid_cell = i + 1, j + 1
                highest = (grid_cell, roi_size, cell_sum)

(x, y), roi_size, cell_sum = highest
print(f"{x},{y},{roi_size}")  # answer: 236,270,11
