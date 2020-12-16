from typing import List, Dict, Optional


def main():
    with open('input.txt', 'r') as f:
        adapters = list(map(int, f.readlines()))

    adapters.sort()

    diffs = joltage_differences(adapters)
    print(diffs[1] * diffs[3])  # Part 1: 2312

    print(num_paths(adapters))  # Part 2: 12089663946752


def joltage_differences(adapters: List[int]) -> Dict[int, int]:
    sequence = [0] + adapters + [adapters[-1] + 3]
    diffs = {1: 0, 2: 0, 3: 0}
    i = 1
    while i < len(sequence):
        prev = sequence[i - 1]
        current = sequence[i]
        diffs[current - prev] += 1
        i += 1
    return diffs


def num_paths(adapters: List[int]) -> int:
    sequence = [0] + adapters + [adapters[-1] + 3]
    return _num_paths(sequence)

def _num_paths(sequence: List[int], i: int = 0, memo: Optional[Dict[int, int]] = None) -> int:
    if memo is None:
        memo = {}
    
    current = sequence[i]

    if current in memo.keys():
        return memo[current]
    
    if sequence[i] == sequence[-1]:
        return 1
    
    j = i + 1
    child_indicies = []    
    while j < len(sequence) and sequence[j] - current <= 3:
        child_indicies.append(j)
        j += 1

    paths = 0
    for child in child_indicies:
        paths += _num_paths(sequence, child, memo)
    
    memo[current] = paths
    return paths

def tests():
    assert joltage_differences([1, 3, 6]) == {1: 1, 2: 1, 3: 2}
    assert joltage_differences(sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]))[1] == 7
    assert joltage_differences(sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]))[3] == 5

    assert num_paths([4]) == 0
    assert num_paths([3]) == 1
    assert num_paths([3, 4]) == 1
    assert num_paths([3, 4, 5]) == 2
    assert num_paths(sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])) == 8


if __name__ == "__main__":
    tests()
    main()