from typing import Tuple, Dict
Coordinate = Tuple[int, int]


def main():
    part_1()  # 6682
    # part_2()  # no idea


def part_1():
    start_pos, map = parse_map()
    pointer_a, pointer_b = start_pos, start_pos
    steps = 0
    visited = {start_pos}
    while True:
        # advance pointer A
        child_a, child_b = map[pointer_a]
        pointer_a = child_a if child_a not in visited else child_b
        visited.add(pointer_a)

        # advance pointer B
        child_a, child_b = map[pointer_b]
        pointer_b = child_a if child_a not in visited else child_b
        visited.add(pointer_b)

        steps += 1

        if pointer_a == pointer_b:
            break
    
    print(steps)


def parse_map() -> Tuple[Coordinate, Dict[Coordinate, Tuple[Coordinate]]]:
    directions_map = {  # by row, column
        "|": ((-1, 0), (1, 0)),
        "L": ((-1, 0), (0, 1)),
        "J": ((0, -1), (-1, 0)),
        "7": ((1, 0), (0, -1)),
        "-": ((0, -1), (0, 1)),
        "F": ((0, 1), (1, 0))
    }

    text_map = []
    with open("input.txt", "r") as f:
        for row in f.read().split("\n"):
            text_map.append(list(row))
    
    map = {}
    map_start = None
    map_start_children = []
    for row_i, row in enumerate(text_map):
        for col_i, c in enumerate(row):
            if c == "S":
                map_start = (row_i, col_i)
            elif c != ".":
                a_direction, b_direction = directions_map[c]
                a_dy, a_dx = a_direction
                b_dy, b_dx = b_direction

                # find child A
                try:
                    if row_i + a_dy < 0 or col_i + a_dx < 0:
                        raise IndexError()
                    next_a = (row_i + a_dy, col_i + a_dx)
                    if text_map[next_a[0]][next_a[1]] == "S":
                        map_start_children.append((row_i, col_i))
                        # TODO: Postential issue: will add neighbour pipes
                        # even if not part of the circuit 
                except IndexError:
                    next_a = None
                
                
                # find child B
                try:
                    if row_i + b_dy < 0 or col_i + b_dx < 0:
                        raise IndexError
                    next_b = (row_i + b_dy, col_i + b_dx)
                    if text_map[next_b[0]][next_b[1]] == "S":
                        map_start_children.append((row_i, col_i))
                except IndexError:
                    next_b = None
                
                map[(row_i, col_i)] = (next_a, next_b)
    
    map[map_start] = tuple(map_start_children)
    return map_start, map


if __name__ == "__main__":
    main()