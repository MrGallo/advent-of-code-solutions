crates_string = []
instructions = []

first_part = True
with open("input.txt", "r") as f:
    for line in f.read().split("\n"):
        if line == "":
            first_part = False
            continue

        if first_part:
            crates_string.append(line)
        else:
            split_up = line.split()
            ins = [
                int(split_up[i])
                for i in range(1, len(split_up), 2) 
            ]
            instructions.append(ins)

print(crates_string)
print(instructions)

column_index = []
for i, c in enumerate(crates_string[-1]):
    if c.isdigit():
        column_index.append((int(c), i))

print(column_index)

stacks = {}
for col, i in column_index:
    stack = []
    for line in crates_string[:-1]:
        c = line[i]
        if c != " ":
            stack.append(c)
    stack.reverse()
    stacks[col] = stack

print(stacks)

for amount, frm, to in instructions:
    origin = stacks[frm]
    destination = stacks[to]
    for _ in range(amount):
        crate = origin.pop()
        destination.append(crate)

print(stacks)

string = ""
for i, _ in column_index:
    string += stacks[i][-1]

print(string)  # part 1: LJSVLTWQM

stacks = {}
for col, i in column_index:
    stack = []
    for line in crates_string[:-1]:
        c = line[i]
        if c != " ":
            stack.append(c)
    stack.reverse()
    stacks[col] = stack

print(stacks)
for amount, frm, to in instructions:
    origin = stacks[frm]
    destination = stacks[to]
    substack = origin[-amount:]
    stacks[frm] = origin[:-amount]
    destination += substack

print(stacks)

string = ""
for i, _ in column_index:
    string += stacks[i][-1]

print(string)  # part 2: 