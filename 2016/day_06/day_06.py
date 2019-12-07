from collections import Counter
from typing import List


def main() -> None:
    with open("input.txt", "r") as f:
        codes = f.read().split()

    print(part1(codes))  # answer: nabgqlcw
    print(part2(codes))  # answer: ovtrjcjh


def part1(codes: List[str]) -> str:
    most_common = [Counter([code[n] for code in codes]).most_common()[0]
                   for n in range(len(codes[0]))]

    word = "".join([letter for letter, count in most_common])
    return word


def part2(codes: List[str]) -> str:
    least_common = [Counter([code[n] for code in codes]).most_common()[-1]
                    for n in range(len(codes[0]))]
    word = "".join([letter for letter, count in least_common])
    return word


if __name__ == "__main__":
    main()
