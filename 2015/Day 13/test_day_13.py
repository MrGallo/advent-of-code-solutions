from day_13 import *


def test_extract_number():
    assert extract_number("blah gain 5 blah") == 5
    assert extract_number("blah lose 5 blah") == -5
    assert extract_number("blah lose 501 blah") == -501


def test_line_to_blah():
    assert (line_to_partners_rating("Alice w gain 54 h u b s n t Bob. ") ==
            {("Alice", "Bob"): 54})
    assert (line_to_partners_rating("Bob w gain 54 h u b s n t Alice. ") ==
            {("Bob", "Alice"): 54})
    assert (line_to_partners_rating("Bob w lose 545 h u b s n t Alice. ") ==
            {("Bob", "Alice"): -545})


def test_rate_arrangement():
    lines = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""".split("\n")

    happiness_map = {}
    for line in lines:
        partners_rating = line_to_partners_rating(line)
        happiness_map.update(partners_rating)

    assert rate_arrangement(["David", "Alice", "Bob", "Carol"], happiness_map) == 330
