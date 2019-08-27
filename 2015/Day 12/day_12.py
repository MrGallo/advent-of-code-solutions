import json


def sum_of_children(parent, exclude_value=None):
    items = []

    if type(parent) is dict:
        items = parent.values()
        if exclude_value is not None and exclude_value in items:
            return 0
    elif type(parent) is list:
        items = parent
    else:
        return 0

    total = 0
    for item in items:
        try:
            total += item
        except TypeError:
            total += sum_of_children(item, exclude_value=exclude_value)

    return total


def part_one():
    with open('input.txt') as f:
        data = json.loads(f.read())
        print(sum_of_children(data))


def part_two():
    with open('input.txt') as f:
        data = json.loads(f.read())
        print(sum_of_children(data, exclude_value="red"))


if __name__ == '__main__':
    part_one()  # answer: 119433
    part_two()  # answer: 68466
