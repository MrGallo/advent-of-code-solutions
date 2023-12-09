from typing import List


def main():
    readings = []
    with open("input.txt", "r") as f:
        for line in f.read().split("\n"):
            readings.append(list(map(int, line.split())))
    
    sum_next = 0
    for history in readings:
        sum_next += get_next(history)

    
    print(sum_next)  # Part 1: 1930746032

    sum_prev = 0
    for history in readings:
        sum_prev += get_prev(history)

    print(sum_prev)  # Part 2: 1154



def get_next(history: List[int]) -> int:
    if all_zero(history):
        return 0
    
    diffs = []
    for i in range(len(history) - 1):
        a = history[i]
        b = history[i + 1]
        diff = b - a
        diffs.append(diff)
    
    return history[-1] + get_next(diffs)


def get_prev(history: List[int]) -> int:
    if all_zero(history):
        return 0
    
    diffs = [0] * (len(history) - 1)
    for i in range(len(history) - 1, 0, -1):
        a = history[i - 1]
        b = history[i]
        diff = b - a
        diffs[i - 1] = diff
    
    return history[0] - get_prev(diffs)


def all_zero(nums) -> bool:
    for n in nums:
        if n != 0:
            return False
            break
    return True




if __name__ == "__main__":
    main()