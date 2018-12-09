from collections import Counter


def reaction(u1, u2):
    return u1 != u2 and u1.lower() == u2.lower()


def collapse(polymer):
    stack = ['.']
    for unit in polymer:
        current = stack.pop()
        if not reaction(current, unit):
            stack.append(current)
            stack.append(unit)

    return "".join(stack[1:])


with open('input.txt') as f:
    polymer = f.read().strip()

unique_units = Counter(polymer.lower()).keys()
polymer_lengths = [len(collapse(polymer.replace(unit, "").replace(unit.upper(), ""))) for unit in unique_units]
print(min(polymer_lengths))
