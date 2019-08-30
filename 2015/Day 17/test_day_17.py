from day_17 import *


def test_get_combos():
    assert get_combos(0, [1, 3, 5, 7]) == []
    assert get_combos(2, [1, 3, 5, 7]) == []
    assert get_combos(1, [2, 3]) == []
    assert get_combos(9, [1, 3, 5, 7]) == [[1, 3, 5]]
    assert len(get_combos(25, [5, 5, 10, 15, 20])) == 4
