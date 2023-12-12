from typing import List

Universe = List[List[str]]


def main():
    original_universe = []
    with open("input.txt", "r") as f:
        for line in f.read().split("\n"):
            original_universe.append(list(line))


    galaxies = extract_galaxies(original_universe)

    # expand
    rows_to_expand = []
    for i, row in enumerate(original_universe):
        if len(tuple(c for c in row if c != ".")) == 0:
            rows_to_expand.append(i)
    
    columns_to_expand = []
    for i in range(len(original_universe[0])):
        if len(tuple(original_universe[j][i] for j in range(len(original_universe)) if original_universe[j][i] != ".")) == 0:
            columns_to_expand.append(i)

    for j, row in enumerate(rows_to_expand):
        for i, (y, x) in enumerate(galaxies):
            if row + j < y:
                galaxies[i] = (y + 1, x)
    
    for j, col in enumerate(columns_to_expand):
        for i, (y, x) in enumerate(galaxies):
            if col + j < x:
                galaxies[i] = (y, x + 1)

    distances = []
    for i, galaxy_a in enumerate(galaxies):
        for galaxy_b in galaxies[i+1:]:
            distance = calc_manhatten_distance(galaxy_a, galaxy_b)
            distances.append(distance)
    
    print(sum(distances))  # Part 1: 9233514

    # PART 2
    galaxies = extract_galaxies(original_universe)
    time = 1_000_000
    for j, row in enumerate(rows_to_expand):
        for i, (y, x) in enumerate(galaxies):
            if row + j * (time - 1) < y:
                galaxies[i] = (y + time-1, x)

    for j, col in enumerate(columns_to_expand):
        for i, (y, x) in enumerate(galaxies):
            if col + j * (time - 1) < x:
                galaxies[i] = (y, x + time-1)

    distances = []
    for i, galaxy_a in enumerate(galaxies):
        for galaxy_b in galaxies[i+1:]:
            distance = calc_manhatten_distance(galaxy_a, galaxy_b)
            distances.append(distance)
    
    print(sum(distances))  # Part 2: 363293506944


def extract_galaxies(universe):
    galaxies = []
    for y, row in enumerate(universe):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((y, x))
    return galaxies


def calc_manhatten_distance(a, b):
    y1, x1 = a
    y2, x2 = b
    return abs(y1 - y2) + abs(x1 - x2)


if __name__ == "__main__":
    main()