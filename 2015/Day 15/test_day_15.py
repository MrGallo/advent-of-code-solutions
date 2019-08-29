from day_15 import *


ingredients_raw_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split("\n")


def test_parse_ingredient():
    name, capacity, durability, flavor, texture, calories = (
        parse_ingredient(ingredients_raw_data[0]))

    assert name == "Butterscotch"
    assert capacity == -1
    assert durability == -2
    assert flavor == 6
    assert texture == 3
    assert calories == 8


def test_calc_category():
    ingredients = [parse_ingredient(ing) for ing in ingredients_raw_data]
    assert calc_category(1, [44, 56], ingredients) == 68
    assert calc_category(2, [44, 56], ingredients) == 80
    assert calc_category(3, [44, 56], ingredients) == 152
    assert calc_category(4, [44, 56], ingredients) == 76

    # test negative property
    assert calc_category(1, [100, 0], ingredients) == 0


def test_calc_total_score():
    ingredients = [parse_ingredient(ing) for ing in ingredients_raw_data]
    total_score = calc_total_score([44, 56], ingredients)
    assert total_score == 62842880


def test_calc_calories():
    ingredients = [parse_ingredient(ing) for ing in ingredients_raw_data]
    assert calc_calories([40, 60], ingredients) == 500
    assert calc_calories([1, 1], ingredients) == 8+3
    assert calc_calories([2, 5], ingredients) == 8*2+3*5
