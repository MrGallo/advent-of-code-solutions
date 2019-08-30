import numpy as np


STATE_MAP = {k: v for k, v in zip(".#", (0, 1))}


def part_one():
    with open('input.txt') as f:
        light_state = np.array(parse_light_state(f.read()))

    for step in range(100):
        light_state = np.array([
            [next_step((j, i), light_state) for i, row in enumerate(col)]
            for j, col in enumerate(light_state)
        ])

    print(np.sum(light_state))


def part_two():
    with open('input.txt') as f:
        light_state = keep_corners_activated(
            np.array(parse_light_state(f.read())))

    for step in range(100):
        light_state = keep_corners_activated(
            np.array([
                [next_step((j, i), light_state) for i, row in enumerate(col)]
                for j, col in enumerate(light_state)
            ])
        )

    print(np.sum(light_state))


def parse_light_state(initial_state_raw):
    return [
        [STATE_MAP[v] for v in line]
        for line in initial_state_raw.strip().split("\n")
    ]


def get_roi(col, row):
    return slice(max(0, col-1), col+2), slice(max(0, row-1), row+2)


def next_step(loc, state):
    col, row = loc
    roi = get_roi(col, row)
    sum_roi = np.sum(state[roi])
    current_state = state[col][row]

    if current_state == 0:
        if sum_roi == 3:
            return 1
        return 0
    else:
        if sum_roi - current_state in [2, 3]:
            return 1
        return 0


def keep_corners_activated(state):
    height, width = state.shape
    state[0][0] = 1
    state[0][width-1] = 1
    state[height-1][0] = 1
    state[height-1][width-1] = 1
    return state


if __name__ == "__main__":
    part_one()  # answer: 821
    part_two()  # answer: 886
