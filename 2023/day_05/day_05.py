from typing import List


def main():

    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    seeds = [int(n) for n in lines[0].split(": ")[1].split()]
    almanac = parse_almanac(lines[2:])
    min_location = None
    for seed in seeds:
        result = find_location(seed, almanac)
        if min_location is None or result < min_location:
            min_location = result
    print(min_location)  # Part 1: 1181555926
    
    print(seeds)

    # find lowest seed
    lowest_seed = None
    highest_seed = None
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        start, amount = seeds[i], seeds[i + 1]
        end = start + amount - 1
        if lowest_seed is None or start < lowest_seed:
            lowest_seed = start
        if highest_seed is None or end > highest_seed:
            highest_seed = end
        seed_ranges.append((start, end))

    potential_loc = 0
    while True:
        seed = find_location(potential_loc, almanac, backwards=True)
        found = False
        # print(seed)
        for start, end in seed_ranges:
            if start <= seed <= end:
                print(start, seed, end)
                # print(f"found: {start}, {end}")
                found = True
                break
        if found:
            break
        # input()
        potential_loc += 1
    
    print(potential_loc)  # Part 2: 37806486



def parse_almanac(lines: List[str]):
    almanac = []
    section = []
    for i, line in enumerate(lines):
        if len(line) == 0:
            almanac.append(section)
            continue

        try:
            apart = line.split()
            section.append(list(map(int, apart)))
        except ValueError:
            section = []

        if i == len(lines) - 1:
            almanac.append(section)
    
    return almanac


def find_location(seed: int, almanac: List[List[List[int]]], backwards = False) -> int:
    result = seed
    # print(f"******** Seed: {seed}")
    sections = almanac
    if backwards:
        sections = reversed(almanac)

    for section in sections:
        for dest, source, n in section:
            if backwards:
                dest, source = source, dest
            # print(dest, source, n)
            source_diff = result - source
            if source_diff >= 0 and source_diff < n:
                result = dest + source_diff
                # print(f"{result} ->", end="")
                break

        # print(f"{result} falls within {source}-{source+n-1}. {source_diff} + {dest} -> {result}")
    return result


if __name__ == "__main__":
    main()