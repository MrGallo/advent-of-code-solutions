from typing import List, Callable
from collections import deque


def main():
    with open('input.txt', 'r') as f:
        MAP = {
            "L": 1,
            ".": 0
        }
        floor_plan = [
            [MAP[c] for c in row.strip()]
            for row in f.readlines()
        ]

    occupancy = [
        [0] * len(floor_plan[0])
    ] * len(floor_plan)

    print(find_equilibrium(floor_plan, occupancy, seating_rules_part_one))  # Part 1: 2238
    print(find_equilibrium(floor_plan, occupancy, seating_rules_part_two))  # Part 2: 2013


def find_equilibrium(floor_plan: List[List[int]], occupancy: List[List[int]], seating_rules: Callable) -> int:
    occupancies = deque(maxlen=30)
    count = 0
    while True:
        occupancy = apply_seating_rules(floor_plan, occupancy, seating_rules)
        people = sum([sum(row) for row in occupancy])
        occupancies.append(people)
        count += 1
        if count > 1 and len(set(occupancies)) == 1:
            break
    return people


def apply_seating_rules(floor_plan: List[List[int]], occupancy: List[List[int]], seating_rules: Callable) -> List[List[int]]:
    occupancy_copy = []
    for row in occupancy:
        row_copy = [n for n in row]
        occupancy_copy.append(row_copy)

    for y in range(len(floor_plan)):
        for x in range(len(floor_plan[0])):
            if floor_plan[y][x]:
                seating_rules(floor_plan, occupancy, occupancy_copy, y, x)
    return occupancy_copy


def seating_rules_part_one(floor_plan, occupancy, occupancy_copy, y, x):
    occupied = sum(get_adjacent(occupancy, y, x))
    if occupancy_copy[y][x] == 0 and occupied == 0:
        occupancy_copy[y][x] = 1
    elif occupancy_copy[y][x] == 1 and occupied >= 4:
        occupancy_copy[y][x] = 0


def seating_rules_part_two(floor_plan, occupancy, occupancy_copy, y, x):
    occupied = count_first_seat(floor_plan, occupancy, y, x)
    if occupancy_copy[y][x] == 0 and occupied == 0:
        occupancy_copy[y][x] = 1
    elif occupancy_copy[y][x] == 1 and occupied >= 5:
        occupancy_copy[y][x] = 0



def get_adjacent(grid: List[List[int]], y: int, x: int) -> List[int]:
    top = grid[y-1][max(0, x - 1):x + 2] if y > 0 else []
    left = [grid[y][x-1]] if x > 0 else []
    right = [grid[y][x+1]] if x+1 < len(grid[0]) else []
    bot = grid[y+1][max(0, x - 1):x + 2] if y+1 < len(grid) else []
    return top + left + right + bot


def count_first_seat(floor_plan: List[List[int]], occupancy: List[List[int]], y: int, x: int) -> List[int]:
    directions = (  # dx, dy
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    )
    visible = 0
    for dx, dy in directions:
        cursor_x = x + dx
        cursor_y = y + dy
        while cursor_y >= 0 and cursor_y < len(floor_plan) and cursor_x >= 0 and cursor_x < len(floor_plan[0]):
            if floor_plan[cursor_y][cursor_x]:
                if occupancy[cursor_y][cursor_x]:
                    visible += 1
                break
            cursor_y += dy
            cursor_x += dx

    return visible

def tests():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert get_adjacent(grid, 1, 1) == [1, 2, 3, 4, 6, 7, 8, 9]
    assert get_adjacent(grid, 0, 0) == [2, 4, 5]
    assert get_adjacent(grid, 2, 0) == [4, 5, 8]
    assert get_adjacent(grid, 2, 2) == [5, 6, 8]
    assert get_adjacent(grid, 0, 1) == [1, 3, 4, 5, 6]
    assert get_adjacent(grid, 1, 2) == [2, 3, 5, 8, 9]
    assert get_adjacent(grid, 2, 1) == [4, 5, 6, 7, 9]
    assert get_adjacent(grid, 1, 0) == [1, 2, 5, 7, 8]
    assert get_adjacent(grid, 0, 2) == [2, 5, 6]

    floor_plan = [
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]
    ]

    occupancy = [[0] * 3] * 3
    expected_occupancy = [
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]
    ]
    assert apply_seating_rules(occupancy, floor_plan, seating_rules_part_one) == expected_occupancy

    occupancy = expected_occupancy
    expected_occupancy = [
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1]
    ]
    assert apply_seating_rules(occupancy, floor_plan, seating_rules_part_one) == expected_occupancy


if __name__ == "__main__":
    tests()
    main()
