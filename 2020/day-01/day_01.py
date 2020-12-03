from typing import List, Optional, Set, Tuple


def main():
    with open('input.txt', 'r') as f:
        expenses = list(map(int, f.read().split("\n")))


    a, b = part_one(expenses)
    print(a * b)  # 1020084

    a, b, c = part_two(expenses)
    print(a * b * c)  # 295086480


def part_one(expenses: List[int], target_sum: int = 2020) -> Optional[Tuple[int]]:
    potential_partners: Set[int] = set()
    for expense in expenses:
        potential_partners.add(expense)
        partner = target_sum - expense
        if partner in potential_partners:
            return partner, expense

    return None


def part_two(expenses: List[int], target_sum: int = 2020) -> Tuple[int, int, int]:
    for expense in expenses:
        new_target_sum = target_sum - expense
        other_two = part_one(expenses, new_target_sum)
        if other_two:
            return expense, *other_two


if __name__ == "__main__":
    main()
