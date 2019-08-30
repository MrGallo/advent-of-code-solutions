from collections import Counter


def part_one():
    with open('input.txt') as f:
        containers = [int(line) for line in f]

    containers.sort()
    combos = get_combos(150, containers)
    print(len(combos))


def part_two():
    with open('input.txt') as f:
        containers = [int(line) for line in f]

    containers.sort()
    combos = get_combos(150, containers)
    sizes = Counter([len(combo) for combo in combos])
    smallest_combo = min(sizes.keys())
    num_of_smallest_combo = sizes[smallest_combo]
    print(num_of_smallest_combo)


def get_combos(total_litres, containers, current_combo=None, combos=None):
    if len(containers) == 0:
        return []

    if combos is None:
        combos = []

    for i, volume in enumerate(containers):
        if current_combo is None:
            current_combo = []

        remaining_litres = total_litres - volume

        if remaining_litres == 0:
            combos.append(current_combo + [volume])
            continue
        elif remaining_litres < volume:
            continue

        get_combos(remaining_litres,
                   containers[i+1:],
                   current_combo[:] + [volume],
                   combos)

    return combos


if __name__ == "__main__":
    part_one()  # answer: 654
    part_two()  # answer: 57
