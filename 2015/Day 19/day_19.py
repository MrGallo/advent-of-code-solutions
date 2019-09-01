from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        replacements = defaultdict(list)
        for line in f:
            i = line.find(" => ")
            if i != -1:
                key = line[:i]
                value = line[i+4:].strip()
                replacements[key].append(value)
            elif line != "\n":
                molecule = line.strip()

    unique = set()

    for i, _ in enumerate(molecule):
        for chem, subs in replacements.items():
            for sub in subs:
                if molecule[i:].startswith(chem):
                    new_molecule = (molecule[:i] +
                                    sub +
                                    molecule[i+len(chem):])
                    unique.add(new_molecule)
    print(len(unique))


def part_two():
    with open('input.txt') as f:
        replacements = {}
        for line in f:
            i = line.find(" => ")
            if i != -1:
                value = line[:i]
                key = line[i+4:].strip()
                replacements[key] = value
            elif line != "\n":
                molecule = line.strip()

    steps = 0
    while molecule != "e":
        for chem, sub in replacements.items():
            i = molecule.find(chem)
            if i != -1:
                molecule = (molecule[:i] +
                            sub +
                            molecule[i+len(chem):])
                steps += 1
    print(steps)


if __name__ == "__main__":
    part_one()  # answer: 509
    part_two()  # answer: 195
