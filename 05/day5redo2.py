from collections import Counter

def reaction(unit1, unit2):
    return unit1 != unit2 and unit1.lower() == unit2.lower()


def collapse_polymer(polymer):
    collapsed = ['.']
    for unit in polymer:
        tail = collapsed[-1]
        if reaction(tail, unit):
            collapsed.pop()
        else:
            collapsed.append(unit)
    
    return collapsed[1:]


polymer = open('input.txt').read().strip()
# polymer = "AaxbBXcdEfFeG"

unique = set([unit for unit in polymer.lower()])
lengths = [len(collapse_polymer(polymer.replace(unit, "").replace(unit.upper(), ""))) for unit in unique]

print(min(lengths))