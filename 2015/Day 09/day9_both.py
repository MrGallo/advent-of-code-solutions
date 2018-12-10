import itertools


def parse_line(line):
    to_i = line.index(" to")
    eq_i = line.index(" =")
    num_i = eq_i + 3

    dest1 = line[:to_i]
    dest2 = line[to_i+4:eq_i]
    dist = int(line[num_i:])

    return dest1, dest2, dist


with open('input.txt') as f:
    lines = [line.strip() for line in f]

distances = [parse_line(line) for line in lines]

cities = set()
matrix = {}
for dest1, dest2, dist in distances:
    cities.update({dest1, dest2})
    matrix[(dest1, dest2)] = dist
    matrix[(dest2, dest1)] = dist

longest = None
shortest = None
for route in itertools.permutations(cities):
    dist = 0
    for i in range(len(route)-1):
        city1 = route[i]
        city2 = route[i+1]
        dist += matrix[(city1, city2)]

    if not longest or dist > longest:
        longest = dist

    if not shortest or dist < shortest:
        shortest = dist

print(shortest)  # answer part1: 207
print(longest)   # answer part2: 804
