from typing import List, Tuple, Dict

from intcode_computer import IntcodeComputer


Hull = Dict[Tuple[int], int]

DIRECTIONS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

ROTATIONS = {
    0: -1,
    1: 1
}


def main() -> None:
    with open("input.txt", "r") as f:
        program = [int(n) for n in f.read().split(",")]

    print(part1(program))  # answer: 1732
    part2(program)  # answer: ABCLFUHJ


def part1(program: List[int]) -> int:
    paint_bot = IntcodeComputer(program)
    ship_hull = paint_hull(paint_bot, {})
    return len(ship_hull)       
    

def part2(program: List[int]) -> None:
    paint_bot = IntcodeComputer(program)
    ship_hull = paint_hull(paint_bot, {(0, 0): 1})

    # get canvas dimensions based on visited hull locations
    max_x, _ = max(ship_hull.keys(), key=lambda p: p[0])
    min_x, _ = min(ship_hull.keys(), key=lambda p: p[0])
    _, max_y = max(ship_hull.keys(), key=lambda p: p[1])
    _, min_y = min(ship_hull.keys(), key=lambda p: p[1])

    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)

    canvas = [[0 for _ in range(width+1)] for _ in range(height+1)]

    # color the canvas according to hull colors
    for (x, y), color in ship_hull.items():
        canvas[y-min_y][x-min_x] = color

    COLORS = {
        0: "█",
        1: " "
    }

    # print the canvas
    for row in reversed(canvas):
        for char in row:
            print(COLORS[char], end="")
        print()


def paint_hull(paint_bot: IntcodeComputer, ship_hull: Hull) -> Hull:
    current_location = (0, 0)
    heading = 0
    while True:
        try:
            bot_input = ship_hull[current_location]
        except KeyError:
            bot_input = 0
        paint_bot.set_inputs([bot_input])

        code, color = paint_bot.execute()
        if code != IntcodeComputer.RETURNING_OUTPUT:
            break

        ship_hull[current_location] = color

        code, turn_direction = paint_bot.execute()
        if code != IntcodeComputer.RETURNING_OUTPUT:
            raise Exception("Should not be exiting here.")
            
        heading = (heading + ROTATIONS[turn_direction]) % len(DIRECTIONS)
        x, y, = current_location
        dx, dy = DIRECTIONS[heading]
        current_location = x + dx, y + dy
    
    return ship_hull


if __name__ == "__main__":
    main()
