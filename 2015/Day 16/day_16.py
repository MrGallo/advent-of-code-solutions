import re
from typing import List

ITEMS = {
    "id": 0,
    "children": 1,
    "cats": 2,
    "samoyeds": 3,
    "pomeranians": 4,
    "akitas": 5,
    "vizslas": 6,
    "goldfish": 7,
    "trees": 8,
    "cars": 9,
    "perfumes": 10
}


TICKER_TAPE = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]


def part_one():
    with open('input.txt') as f:
        aunts = [parse_aunt(line) for line in f]

    for aunt in aunts:
        aunt_id = aunt[ITEMS['id']]
        for a, t in zip(aunt[1:], TICKER_TAPE):
            if a is None:
                continue
            if a != t:
                break  # not a match
        else:
            break
    print(aunt_id)


def part_two():
    with open('input.txt') as f:
        aunts = [parse_aunt(line) for line in f]

    for aunt in aunts:
        aunt_id = aunt[ITEMS['id']]
        for i, (a, t) in enumerate(zip(aunt[1:], TICKER_TAPE), 1):
            if a is None:
                continue
            if i in [ITEMS['cats'], ITEMS['trees']]:
                "Must be greater than ticker value"
                if a <= t:
                    break
            elif i in [ITEMS['pomeranians'], ITEMS['goldfish']]:
                "Must be less than ticker value"
                if a >= t:
                    break
            elif a != t:
                break  # not a match
        else:
            break
    print(aunt_id)


def parse_aunt(line: str) -> List:
    match = re.search(r"^Sue (?P<id>[0-9]+)", line)
    sue_id = int(match.group('id'))
    attributes = [None] * len(ITEMS)
    attributes[ITEMS['id']] = sue_id

    matches = re.findall(r"\w+?: [0-9]+", line)
    for match in matches:
        key = re.match(r"\w+", match).group(0)
        value = int(re.findall(r"[0-9]+", match)[0])
        attributes[ITEMS[key]] = value
    return attributes


if __name__ == "__main__":
    part_one()  # answer: 213
    part_two()  # answer: 323