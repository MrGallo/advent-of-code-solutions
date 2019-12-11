import math
from collections import defaultdict
from itertools import cycle
from typing import Dict, List, Tuple

Asteroid = Tuple[int, int]


def main() -> None:
    with open("input.txt", "r") as f:
        asteroid_map = f.read().split()

    asteroids = parse_asteroids(asteroid_map)
    best_location, headings = get_best_location(asteroids)
    print(len(headings))  # part 1 answer: 263

    vaporized = vaporize_asteroids(best_location, headings)
    x, y = vaporized[199]
    print(x*100 + y)  # part2 answer: 1110


def parse_asteroids(asteroid_map: List[str]) -> Asteroid:
    asteroids = []
    for y, row in enumerate(asteroid_map):
        for x, char in enumerate(row):
            if char == "#":
                asteroids.append((x, y))

    return asteroids


def get_best_location(asteroids: List[Asteroid]) -> Tuple[Asteroid, int]:
    best_location = None
    location_headings = {}
    for current in asteroids:
        headings = defaultdict(list)
        for other in asteroids:
            if current == other:
                continue
            heading = get_heading_degrees(current, other)
            headings[heading].append(other)
        location_headings[current] = headings

        if (best_location is None or
                len(location_headings[current]) >
                len(location_headings[best_location])):
            best_location = current

    return best_location, location_headings[best_location]


def get_heading_degrees(asteroid1: Asteroid, asteroid2: Asteroid) -> float:
    x1, y1 = asteroid1
    x2, y2 = asteroid2

    # reverse y axis due to inverted grid
    degree = math.degrees(math.atan2(x2-x1, y1-y2))
    return degree if degree >= 0 else 360 + degree


def get_distance(asteroid1: Asteroid, asteroid2: Asteroid) -> float:
    x1, y1 = asteroid1
    x2, y2 = asteroid2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def vaporize_asteroids(best_location: Asteroid,
                       visible: Dict[float, List[Asteroid]]):
    sorted_visible = sorted(visible.items())
    vaporized = []

    while sorted_visible:
        i = 0
        while i < len(sorted_visible):
            heading, locations = sorted_visible[i]
            closest_i = None
            for j, target in enumerate(locations):
                distance = get_distance(best_location, target)
                if closest_i is None or distance < get_distance(best_location, locations[closest_i]):
                    closest_i = j
            vaporized.append(locations.pop(closest_i))
            if len(locations) == 0:
                del sorted_visible[i]
                continue
            i += 1

    return vaporized


if __name__ == "__main__":
    main()
