from typing import List


def main() -> None:
    start, end = 402328, 864247

    matches = []
    for num in range(start, end):
        num_list = int_to_list(num)
        # if has_2_adjacent(num_list) and is_increasing(num_list):  # part 1
        if has_at_most_2_adjacent(num_list) and is_increasing(num_list):  # part 2
            matches.append(num)

    print(len(matches))


def has_2_adjacent(digits: List[int]) -> bool:
    """For Part 1"""
    for a, b in zip(digits[:-1], digits[1:]):
        if a == b:
            return True
    return False


def has_at_most_2_adjacent(digits: List[int]) -> bool:
    """For Part 2"""
    adjacent = [digits[0]]
    for num in digits[1:]:
        if adjacent[0] == num:
            adjacent.append(num)
        else:
            if len(adjacent) == 2:
                return True
            adjacent = [num]
    
    return len(adjacent) == 2


def is_increasing(digits: List[int]) -> bool:
    for a, b in zip(digits[:-1], digits[1:]):
        if a > b:
            return False
    return True
        

def int_to_list(n: int) -> List[int]:
    return [int(digit) for digit in str(n)]


if __name__ == "__main__":
    main()
