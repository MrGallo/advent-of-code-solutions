from day_18 import *
import numpy as np


initial_state_raw = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


step_1_raw = """..##..
..##.#
...##.
......
#.....
#.##.."""


step_4_raw = """......
......
..##..
..##..
......
......"""


def test_parse_light_state():
    parsed_state = parse_light_state(initial_state_raw)
    assert parsed_state[0] == [0, 1, 0, 1, 0, 1]
    assert parsed_state[1] == [0, 0, 0, 1, 1, 0]


def test_get_roi():
    assert get_roi(0, 0) == (slice(0, 2), slice(0, 2))
    assert get_roi(5, 7) == (slice(4, 7), slice(6, 9))


def test_sum_roi():
    parsed_state = np.array(parse_light_state(initial_state_raw))
    assert np.sum(parsed_state) == 15
    assert np.sum(parsed_state[0:2, 0:2]) == 1
    roi = get_roi(2, 3)
    assert np.sum(parsed_state[roi]) == 3
    roi = get_roi(5, 1)
    assert np.sum(parsed_state[roi]) == 5
    roi = get_roi(5, 5)
    assert np.sum(parsed_state[roi]) == 1


def test_next_step():
    initial_state = np.array(parse_light_state(initial_state_raw))
    # was off, stayed off
    assert next_step((0, 0), initial_state) == 0

    # was off, turned on
    assert next_step((0, 2), initial_state) == 1


    # was on, turned off
    assert next_step((0, 1), initial_state) == 0

    # was on, stayed on
    assert next_step((0, 3), initial_state) == 1


def test_acceptance():
    initial_state = np.array(parse_light_state(initial_state_raw))
    step_1 = np.array(parse_light_state(step_1_raw))
    step_4 = np.array(parse_light_state(step_4_raw))

    current_state = np.array(initial_state)
    assert current_state is not initial_state

    for n in range(4):
        current_state = np.array([
            [next_step((j, i), current_state) for i, row in enumerate(col)]
            for j, col in enumerate(current_state)
        ])

        if n == 0:
            assert np.array_equal(current_state, step_1)
    assert np.array_equal(current_state, step_4)

    assert np.sum(current_state) == 4


def test_keep_corners_activated():
    initial = np.array([
        [0, 0],
        [0, 0]
    ])
    expected = np.array([
        [1, 1],
        [1, 1]
    ])
    assert initial.shape == (2, 2)
    assert np.array_equal(keep_corners_activated(initial), expected)

    initial = np.array([
        [0, 0, 0],
        [0, 0, 0],
    ])
    expected = np.array([
        [1, 0, 1],
        [1, 0, 1],
    ])
    assert initial.shape == (2, 3)
    assert np.array_equal(keep_corners_activated(initial), expected)
