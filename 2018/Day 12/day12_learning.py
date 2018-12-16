with open('input.txt') as f:
    lines = [line.strip() for line in f]

initial_state = set(i for i, x in enumerate(lines[0].split()[-1]) if x == '#')
print(initial_state)


rules = dict(line.split()[::2] for line in lines[2:])
print(rules)