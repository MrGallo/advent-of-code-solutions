from typing import List, Tuple


def main():
    with open('input.txt', 'r') as f:
        grid = [
            [{'.': 0, '#': 1}[c] for c in row]
            for row in f.read().split("\n")
        ]

    print(count_trees_in_slope(grid, (3, 1)))  # Part 1: 171

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    product = 1
    for slope in slopes:
        product *= count_trees_in_slope(grid, slope)

    print(product)  # Part 2: 1206576000


def count_trees_in_slope(grid: List[List[int]], slope: Tuple[int, int]) -> int:
    count = 0
    dx, dy = slope
    x, y = 0, 0
    width = len(grid[0])
    while y < len(grid):
        count += grid[y][x % width]
        x += dx
        y += dy
    
    return count


if __name__ == "__main__":
    main()
