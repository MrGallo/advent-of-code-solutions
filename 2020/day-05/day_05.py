from typing import List
import math

def main():
    with open('input.txt', 'r') as f:
        boarding_passes = f.read().split("\n")
    
    seat_ids = get_seat_ids(boarding_passes)
    maximum = None
    minimum = None
    for id in seat_ids:
        if maximum is None or id > maximum:
            maximum = id
        if minimum is None or id < minimum:
            minimum = id
    print(maximum)  # Part 1: 861

    my_id = sum(range(minimum, maximum + 1))
    for id in seat_ids:
        my_id -= id
    
    print(my_id)  # Part 2: 633

def tests():
    assert get_row("BBBBBBB") == 127
    assert get_row("FBFBBFF") == 44
    assert get_row("FFFFFFF") == 0
    assert get_row("BFFFBBF") == 70
    assert get_column("RLR") == 5
    assert get_column("LLL") == 0
    assert calc_seat_id("FBFBBFFRLR") == 357
    assert calc_seat_id("BFFFBBFRRR") == 567
    assert calc_seat_id("FFFFFFFLLL") == 0


def get_seat_ids(boarding_passes: List[str]) -> List[int]:
    return [calc_seat_id(bp) for bp in boarding_passes]


def calc_seat_id(boarding_pass: str) -> int:
    row = get_row(boarding_pass[:7])
    column = get_column(boarding_pass[-3:])
    return row * 8 + column


def get_row(row_string: str) -> int:
    left = 0
    right = 127
    for dir in row_string:
        if dir == "F":
            mid = math.floor((left + right) / 2)
            right = mid
        else:
            mid = math.ceil((left + right) / 2)
            left = mid
    return mid


def get_column(col_string: str) -> int:
    left = 0
    right = 7
    for dir in col_string:
        if dir == "L":
            mid = math.floor((left + right) / 2)
            right = mid
        else:
            mid = math.ceil((left + right) / 2)
            left = mid
    return mid


if __name__ == "__main__":
    tests()
    main()