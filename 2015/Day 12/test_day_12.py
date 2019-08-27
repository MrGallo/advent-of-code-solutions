from day_12 import *


def test_sum_of_children():
    assert sum_of_children(3) == 0
    assert sum_of_children([1, 2, 3, 4]) == 10
    assert sum_of_children([1, 2, "red", 3]) == 6
    assert sum_of_children([1, 2, "red", [1, 1, 1]]) == 6
    assert sum_of_children({"e": [1, 2]}) == 3
    assert sum_of_children({"e": "red", "f": [1, 2, 3]}, exclude_value="red") == 0
    assert sum_of_children([1, {"c": "red", "b": 2}, 3]) == 6
    assert sum_of_children([1, {"c": "red", "b": 2}, 3], exclude_value="red") == 4
