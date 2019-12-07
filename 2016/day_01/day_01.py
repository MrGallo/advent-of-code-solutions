from typing import List


HEADINGS = {
        0: (0, 1),   # north
        1: (1, 0),   # east
        2: (0, -1),  # south
        3: (-1, 0)   # west
    }

TURNS = {
    "R": 1,
    "L": -1
}


def main() -> None:
    with open("input.txt", "r") as f:
        directions = f.read().split(", ")

    print(part1(directions))  # answer: 291
    print(part2(directions))  # answer: 159


def part1(directions: List[str]) -> int:
    heading = 0
    x, y = 0, 0
    for direction in directions:
        turn = direction[0]
        magnitude = int(direction[1:])
        heading = (heading + TURNS[turn]) % len(HEADINGS)
        dx, dy = (magnitude * h for h in HEADINGS[heading])
        x, y = x+dx, y+dy

    distance = abs(x) + abs(y)
    return distance


def part2(directions: List[str]) -> int:
    heading = 0
    x, y = 0, 0
    visited = [(0, 0)]
    for direction in directions:
        turn = direction[0]
        magnitude = int(direction[1:])
        heading = (heading + TURNS[turn]) % len(HEADINGS)
        hx, hy = HEADINGS[heading]
        while magnitude > 0:
            x += 1 * hx
            y += 1 * hy
            if (x, y) in visited:
                distance = abs(x) + abs(y)
                return distance
            visited.append((x, y))
            magnitude -= 1


if __name__ == "__main__":
    main()
