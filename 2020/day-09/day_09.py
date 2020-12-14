from typing import List
from itertools import combinations


def main():
    with open('input.txt', 'r') as f:
        nums = [int(n) for n in f.readlines()]
    
    invalid_number = find_invalid_number(nums)
    print(invalid_number)  # Part 1: 1492208709

    cont_set = find_contiguous_set(nums, invalid_number)
    print(max(cont_set) + min(cont_set))  # Part 2: 238243506


def find_invalid_number(nums: List[int], preamble_length: int = 25):
    i = preamble_length
    valid = True
    while valid:
        previous_section = nums[i - preamble_length:i]
        current_num = nums[i]
        # print(current_num)
        valid = False
        for a, b in combinations(previous_section, 2):
            # print(a, b)
            if a + b == current_num:
                valid = True
                break
        i += 1
    return current_num


def find_contiguous_set(nums: List[int], target: int) -> List[int]:
    i = 0
    while i < len(nums):
        total = 0
        j = i
        while j < len(nums):
            total += nums[j]
            if total == target:
                return nums[i:j+1]
            j += 1
        i += 1


def tests():
    nums = [int(n) for n in "35 20 15 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576".split(" ")]

    invalid_number = find_invalid_number(nums, preamble_length=5)
    assert invalid_number == 127

    result = find_contiguous_set([35, 20], 35)
    assert result == [35]

    result = find_contiguous_set([35, 20], 20)
    assert result == [20]

    result = find_contiguous_set([35, 20, 22], 55)
    assert result == [35, 20]

    result = find_contiguous_set([1, 2, 3], 4)
    assert result == None

    result = find_contiguous_set(nums, invalid_number)
    assert result == [15, 25, 47, 40]


if __name__ == "__main__":
    tests()
    main()