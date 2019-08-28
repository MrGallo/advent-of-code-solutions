import re
from itertools import permutations
from collections import defaultdict


def extract_number(string: str):
    coefficient_map = {"gain": 1, "lose": -1}
    regex = re.compile("(gain|lose) [0-9]+")
    match_str = re.search(regex, string).group(0)
    coefficient, num_str = match_str.split()
    return coefficient_map[coefficient] * int(num_str)


def line_to_partners_rating(line: str) -> dict:
    partner1 = re.search(r"^\w*", line).group(0)
    partner2 = re.search(r"(\w*)\.", line).group(1)
    happiness = extract_number(line)
    return {(partner1, partner2): happiness}


def parse_hapiness_map(file):
    happiness_map = defaultdict(int)
    with open('input.txt') as f:
        for line in f:
            partners_rating = line_to_partners_rating(line)
            happiness_map.update(partners_rating)
    return happiness_map


def rate_arrangement(arrangement, happiness_map):
    total_rating = 0

    for i, person in enumerate(arrangement):
        left_index = i - 1
        left_partner = arrangement[left_index]
        left_rating = happiness_map[(person, left_partner)]

        right_index = (i + 1) % len(arrangement)
        right_partner = arrangement[right_index]
        right_rating = happiness_map[(person, right_partner)]

        total_rating += left_rating + right_rating

    return total_rating


def get_max_rating(happiness_map, with_me=False):
    people = set()
    for name1, name2 in happiness_map.keys():
        people.add(name1)

    if with_me:
        people.add("me")

    maximum = None
    arrangements_map = {}
    for arrangement in permutations(people):
        current_rating = rate_arrangement(arrangement, happiness_map)
        arrangements_map.update(
            {arrangement: current_rating})
        if not maximum or current_rating > maximum:
            maximum = current_rating
    return maximum


def part_one():
    happiness_map = parse_hapiness_map('input.txt')
    maximum = get_max_rating(happiness_map)
    print(maximum)


def part_two():
    happiness_map = parse_hapiness_map('input.txt')
    maximum = get_max_rating(happiness_map, with_me=True)
    print(maximum)


if __name__ == "__main__":
    part_one()  # answer: 709
    part_two()  # answer: 668
