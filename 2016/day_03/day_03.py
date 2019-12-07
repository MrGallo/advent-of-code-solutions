from typing import List


def main() -> None:
    with open("input.txt", "r") as f:
        triangles = [[int(n.strip()) for n in line.split()] 
                     for line in f.read().split("\n")]

    print(part1(triangles))  # answer: 1050
    print(part2(triangles))  # answer: 1921


def part1(triangles: List[List[int]]) -> int:
    return sum((1 for triangle in triangles if is_valid_triangle(*triangle)))


def part2(triangles: List[List[int]]) -> int:
    actual_triangles = []
    for row1, row2, row3 in zip(triangles[0::3], triangles[1::3], triangles[2::3]):
        t1, t2, t3 = [[column[n] for column in (row1, row2, row3)]
                      for n in range(3)]
        actual_triangles += [t1, t2, t3]
    return part1(actual_triangles)


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    main()
