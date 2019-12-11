from typing import List, Tuple, Dict
import math
from collections import defaultdict


Asteroid = Tuple[int, int]

def main() -> None:
    with open("input.txt", "r") as f:
        asteroid_map = f.read().split()

    asteroid_map = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split()

    asteroids = parse_asteroid_map(asteroid_map)
    best_asteroid, num_visible = part1(asteroids)
    print(num_visible)  # answer: 263
    print(part2(best_asteroid, asteroids))  # answer: 17 wrong


def parse_asteroid_map(asteroid_map: List[str]) -> List[Asteroid]:
    asteroids = []
    for y, row in enumerate(asteroid_map):
        for x, char in enumerate(row):
            if char == "#":
                asteroids.append((x, y))
    return asteroids
            

def part1(asteroids: List[Asteroid]) -> int:
    astroid_visibilities = {}  # {Asteroid: int}
    for current in asteroids:
        unique_headings = set()
        for other in asteroids:
            if current == other:
                continue
            x1, y1 = current
            x2, y2 = other
            opposite = x2-x1
            adjacent = y2-y1
            heading = get_heading_degrees(opposite, adjacent)
            unique_headings.add(heading)
        astroid_visibilities[current] = len(unique_headings)
    
    maximum = None
    for ast, headings in astroid_visibilities.items():
        if maximum is None or headings > astroid_visibilities[maximum]:
            maximum = ast
    
    return maximum, astroid_visibilities[maximum]


def part2(best_asteroid: Asteroid, asteroids: List[Asteroid]) -> Tuple[int, int]:
    """Returns: 200th asteroid"""
    heading_distances = defaultdict(list)
    for other in asteroids:
        if other == best_asteroid:
            continue
        x1, y1 = best_asteroid
        x2, y2 = other
        diff_x = x1-x2
        diff_y = y1-y2
        heading = get_heading_degrees(diff_x, diff_y)
        distance = math.sqrt(diff_x**2 + diff_y**2)
        heading_distances[heading].append((other, distance))
    
    for heading in sorted(heading_distances):
        heading_distances[heading].sort(key=sort_heading_distances)
    
    vaporized = []
    for i, heading in enumerate(sorted(heading_distances.keys())):
        target = heading_distances[heading].pop(0)
        print(i, heading, target)
        vaporized.append(target)
    
    print(*enumerate(vaporized), sep="\n")
    print(best_asteroid)


def sort_heading_distances(distance: Tuple[Asteroid, float]):
    ast, dist = distance
    return dist

def get_heading_degrees(opposite: float, adjacent: float) -> int:
    degrees = math.degrees(math.atan2(opposite, adjacent))
    return degrees if degrees >= 0 else 360 + degrees


if __name__ == "__main__":
    main()