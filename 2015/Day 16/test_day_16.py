from day_16 import *


aunts_raw = """Sue 1: children: 1, cars: 8, vizslas: 7
Sue 2: akitas: 10, perfumes: 10, children: 5""".split("\n")


def test_parse_aunt():
    sue_one = parse_aunt(aunts_raw[0])
    assert sue_one == [1, 1, None, None, None, None, 7, None, None, 8, None]
