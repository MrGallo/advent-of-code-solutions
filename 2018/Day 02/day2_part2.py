with open('input.txt') as f:
    box_ids = [line.strip() for line in f]


def find_match(box_ids):
    for current in box_ids:
        for other in box_ids:
            if current == other:
                continue

            diff = None
            for i, (a, b) in enumerate(zip(current, other)):
                if a != b and not diff:
                    diff = i
                elif a != b and diff:
                    diff = None
                    break

            if diff:
                return current[:diff] + current[diff+1:]


match = find_match(box_ids)
print(match)
