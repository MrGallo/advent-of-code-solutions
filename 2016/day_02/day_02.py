from typing import List


DIRECTIONS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

KEYPAD_WIDTH = 3
KEYPAD_HEIGHT = 3
KEYPAD = [
    [i for i in range(1+KEYPAD_HEIGHT*j, KEYPAD_HEIGHT*j+KEYPAD_WIDTH+1)]
    for j in range(KEYPAD_HEIGHT)
]

ACTUAL_KEYPAD = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]


def main() -> None:
    with open("input.txt", "r") as f:
        instructions = [list(line) for line in f.read().split("\n")]

    print(part1(instructions))  # answer: 44558
    print(part2(instructions))  # answer: 6BBAD


def part1(instructions: List[List[str]]) -> str:
    passcode = ""
    cursor_x, cursor_y = 1, 1
    for digit_instruction in instructions:
        for direction in digit_instruction:
            dx, dy = DIRECTIONS[direction]
            cursor_x = clamp(cursor_x+dx, 0, KEYPAD_WIDTH-1)
            cursor_y = clamp(cursor_y+dy, 0, KEYPAD_HEIGHT-1)
        passcode += str(KEYPAD[cursor_y][cursor_x])
    return passcode


def part2(instructions: List[List[str]]) -> str:
    passcode = ""
    cursor_x, cursor_y = 0, 2
    for digit_instruction in instructions:
        for direction in digit_instruction:
            dx, dy = DIRECTIONS[direction]
            if cursor_y+dy < 0 or cursor_x+dx < 0:  # fix list[-1] wrap-around
                continue
            try:
                if ACTUAL_KEYPAD[cursor_y+dy][cursor_x+dx] is not None:
                    cursor_x += dx
                    cursor_y += dy
            except IndexError:
                continue
        passcode += ACTUAL_KEYPAD[cursor_y][cursor_x]

    return passcode


def clamp(n: int, a: int, b: int):
    """Clamp an integer (n) within the range of a to b inclusive"""
    return min(max(n, a), b)


if __name__ == "__main__":
    main()
