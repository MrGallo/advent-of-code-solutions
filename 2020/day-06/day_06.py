from typing import List, Set


def main():
    with open('input.txt', 'r') as f:
        groups = [
            [answers for answers in group.split("\n")]
            for group in f.read().split("\n\n")
        ]
    
    total = 0
    for group in groups:
        total += len(unique_group_affirmatives(group))
    print(total)  # Part 1: 6387

    total = 0
    for group in groups:
        total += len(intersection_of_group_affirmatives(group))
    print(total)  # Part 2: 3039


def unique_group_affirmatives(group_affirmatives: List[str]) -> Set[str]:
    unique = set()
    for person_affirmatives in group_affirmatives:
        unique.update(set(person_affirmatives))
    return unique


def intersection_of_group_affirmatives(group_affirmatives: List[str]) -> Set[str]:
    intersection = set(group_affirmatives[0])
    for personal in group_affirmatives[1:]:
        intersection = intersection.intersection(set(personal))
    return intersection


def tests():
    assert unique_group_affirmatives(["abc"]) == set("abc")
    assert unique_group_affirmatives(list("abc")) == set("abc")
    assert unique_group_affirmatives(["ab", "ac"]) == set("abc")
    assert unique_group_affirmatives(list("aaaa")) == set("a")

    assert intersection_of_group_affirmatives(["abc"]) == set("abc")
    assert intersection_of_group_affirmatives(list("abc")) == set()
    assert intersection_of_group_affirmatives(["ab", "ac"]) == set("a")
    assert intersection_of_group_affirmatives(list("aaaa")) == set("a")


if __name__ == "__main__":
    tests()
    main()