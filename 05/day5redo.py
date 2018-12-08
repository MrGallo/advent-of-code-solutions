# Inspired by: https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4jzni
from collections import Counter, defaultdict

def collapse(polymer):
    collapsed = ["."]
    for unit in polymer:
        last = collapsed[-1]
        if unit != last and unit.lower() == last.lower():
            collapsed.pop()
        else:
            collapsed.append(unit)
    
    return len(collapsed) - 1


polymer = open('input.txt').read().strip()

units = Counter(polymer.lower())

minimum = None
for unit in units.keys():
    resulting_size = collapse(polymer.replace(unit, '').replace(unit.upper(), ""))
    if minimum is None or resulting_size < minimum:
        minimum = resulting_size

print(minimum)