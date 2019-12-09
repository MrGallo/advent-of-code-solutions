from typing import List
import re


SCREEN_WIDTH, SCREEN_HEIGHT = 50, 6


def main() -> None:
    with open("input.txt", "r") as f:
        instructions = f.read().split("\n")

    screen = part1(instructions)
    print(sum([sum(row) for row in screen]))  # answer: 115
    part2(screen)  # answer: EFEYKFRFIJ


def part1(instructions: List[str]) -> List[int]:
    screen = [[0 for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    for ins in instructions:
        if ins.startswith("rect"):
            regex = r"([0-9]+)x([0-9]+)"
            matches = re.search(regex, ins)
            w = int(matches.group(1))
            h = int(matches.group(2))

            for row in range(h):
                for col in range(w):
                    screen[row][col] = 1
        elif ins.startswith("rotate row"):
            regex = r"\=([0-9]+) by ([0-9]+)"
            matches = re.search(regex, ins)
            row = int(matches.group(1))
            amount = int(matches.group(2))
            split_point = amount % SCREEN_WIDTH
            screen[row] = screen[row][-split_point:] + screen[row][:-split_point]
        elif ins.startswith("rotate column"):
            regex = r"\=([0-9]+) by ([0-9]+)"
            matches = re.search(regex, ins)
            col = int(matches.group(1))
            amount = int(matches.group(2))
            new_col = [screen[row][col] for row in range(SCREEN_HEIGHT)]
            split_point = amount % SCREEN_HEIGHT
            new_col = new_col[-split_point:] + new_col[:-split_point]
            for row in range(len(new_col)):
                screen[row][col] = new_col[row]

    return screen


def part2(screen: List[int]) -> None:
    char_map = {
        0: " ",
        1: "█"
    }
    for row in screen:
        for i in range(len(row)):
            print(char_map[row[i]], end="")
        print()
    print()


if __name__ == "__main__":
    main()
