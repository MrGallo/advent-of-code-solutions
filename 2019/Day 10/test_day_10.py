from day_10 import *

import math


def test_parse_asteroids():
    result = parse_asteroids([".#.", "#.#"])
    expected = [(1, 0), (0, 1), (2, 1)]
    assert result == expected


def test_get_best_location():
    asteroid_map = """.#..#
.....
#####
....#
...##""".split()

    asteroids = parse_asteroids(asteroid_map)
    result = get_best_location(asteroids)
    expected = (3, 4)


def test_get_heading_degrees():
    best = (8, 3)
    other = (8, 1)
    assert get_heading_degrees(best, other) == 0

    best = (8, 3)
    other = (9, 2)
    assert get_heading_degrees(best, other) == 45

    best = (8, 3)
    other = (12, 3)
    assert get_heading_degrees(best, other) == 90

    best = (8, 3)
    other = (9, 4)
    assert get_heading_degrees(best, other) == 90+45

    best = (8, 3)
    other = (8, 4)
    assert get_heading_degrees(best, other) == 180

    best = (8, 3)
    other = (7, 4)
    assert get_heading_degrees(best, other) == 180+45

    best = (8, 3)
    other = (7, 3)
    assert get_heading_degrees(best, other) == 90*3
