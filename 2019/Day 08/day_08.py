from typing import List
from collections import Counter


IMG_WIDTH, IMG_HEIGHT = 25, 6


def main() -> None:
    with open("input.txt", "r") as f:
        pixel_data = [int(n) for n in f.read()]

    print(part1(pixel_data))  # answer: 1560
    part2(pixel_data)         # answer: UGCUH


def part1(pixel_data: List[int]) -> int:
    fewest_zeros = None
    for i in range(0, len(pixel_data), IMG_HEIGHT*IMG_WIDTH):
        layer_data = pixel_data[i:i+IMG_HEIGHT*IMG_WIDTH]
        count = Counter(layer_data)
        if fewest_zeros is None or count[0] < fewest_zeros[0]:
            fewest_zeros = count

    return fewest_zeros[1] * fewest_zeros[2]


def part2(pixel_data: List[int]) -> None:
    canvas = [2 for _ in range(IMG_WIDTH) for _ in range(IMG_HEIGHT)]
    for i in range(0, len(pixel_data), IMG_HEIGHT*IMG_WIDTH):
        layer_data = pixel_data[i:i+IMG_HEIGHT*IMG_WIDTH]
        for i, pixel in enumerate(layer_data):
            if canvas[i] == 2:
                canvas[i] = pixel

    char_map = {
        0: "░",
        1: "█",
        2: " "
    }

    for i, pixel in enumerate(canvas):
        print(char_map[pixel], end="")
        if i % IMG_WIDTH == IMG_WIDTH-1:
            print()


if __name__ == "__main__":
    main()
