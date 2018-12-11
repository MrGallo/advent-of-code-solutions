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

power_levels = {}
highest = None

for i in range(GRID_SIZE - 2):
    for j in range(GRID_SIZE - 2):
        roi = grid_power[i:i+3, j:j+3]
        grid_cell = i+1, j+1
        power_levels[grid_cell] = np.sum(roi)
        if not highest or power_levels[grid_cell] > power_levels[highest]:
            highest = grid_cell

x, y = highest
print(f"{x},{y}")  # answer: 20,41
