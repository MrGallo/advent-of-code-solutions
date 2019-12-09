from typing import List

from intcode_computer import IntcodeComputer


def main() -> None:
    with open("input.txt", "r") as f:
        program = [int(n) for n in f.read().split(",")]
    print(part1(program))  # answer: 2955820355
    print(part2(program))  # answer: 46643


def part1(program: List[int]) -> int:
    computer = IntcodeComputer(program, [1])

    while True:
        code, result = computer.execute()
        if code == IntcodeComputer.RETURNING_OUTPUT:
            return result


def part2(program: List[int]) -> int:
    computer = IntcodeComputer(program, [2])
    while True:
        code, result = computer.execute()
        if code == IntcodeComputer.RETURNING_OUTPUT:
            return result
    

if __name__ == "__main__":
    main()