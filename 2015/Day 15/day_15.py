import re
from typing import List, Union
from itertools import combinations, chain


CATEGORY = {
    'capacity': 1,
    'durability': 2,
    'flavor': 3,
    'texture': 4,
    'calories': 5
}


def part_one():
    with open('input.txt') as f:
        ingredients = [parse_ingredient(line) for line in f]

    highest_score = None
    for capacity in range(0, 100):
        for durability in range(0, 100-capacity):
            for flavor in range(0, 100-capacity-durability):
                texture = 100-capacity-durability-flavor
                portions = capacity, durability, flavor, texture
                cookie_score = calc_total_score(portions, ingredients)
                if not highest_score or cookie_score > highest_score:
                    highest_score = cookie_score
    print(highest_score)


def part_two():
    with open('input.txt') as f:
        ingredients = [parse_ingredient(line) for line in f]

    highest_score = None
    for capacity in range(0, 100):
        for durability in range(0, 100-capacity):
            for flavor in range(0, 100-capacity-durability):
                texture = 100-capacity-durability-flavor
                portions = capacity, durability, flavor, texture
                calories = calc_calories(portions, ingredients)
                if calories != 500:
                    continue
                cookie_score = calc_total_score(portions, ingredients)
                if not highest_score or cookie_score > highest_score:
                    highest_score = cookie_score
    print(highest_score)


def parse_ingredient(ingredient_data: str):
    regex = re.compile("(?P<name>\\w+): "
                       "capacity (?P<capacity>-?[0-9]+), "
                       "durability (?P<durability>-?[0-9]+), "
                       "flavor (?P<flavor>-?[0-9]+), "
                       "texture (?P<texture>-?[0-9]+), "
                       "calories (?P<calories>-?[0-9]+)")
    match = re.search(regex, ingredient_data)

    return (
        match.group('name'),
        int(match.group('capacity')),
        int(match.group('durability')),
        int(match.group('flavor')),
        int(match.group('texture')),
        int(match.group('calories'))
    )


def calc_total_score(portions: List, ingredients: List) -> int:
    product = 1
    for category in [index for name, index in CATEGORY.items()
                     if name != 'calories']:
        product *= calc_category(category, portions, ingredients)
    return product


def calc_category(category: Union[int, str], portions: List[int],
                  ingredients: List[tuple]) -> int:
    if type(category) is str:
        category = CATEGORY[category]

    total = 0
    for portion, ingredient in zip(portions, ingredients):
        property_value = ingredient[category]
        category_score = portion * property_value
        total += category_score
    return max(total, 0)


def calc_calories(portions: List, ingredients: List) -> int:
    return sum([ingredient[CATEGORY['calories']] * unit
                for ingredient, unit in zip(ingredients, portions)])


if __name__ == "__main__":
    part_one()  # answer: 13882464
    part_two()  # answer: 11171160
