
with open('input.txt', 'r') as f:
    lines = f.read().split('\n')


registers = {
    'a': 0,
    'b': 0
}

registers['a'] = 1  # part 2

i = 0
while i < len(lines):
    line = lines[i]
    print(i, line)
    if line.startswith("hlf"):
        r = line[-1]
        registers[r] /= 2
        i += 1
    elif line.startswith("tpl"):
        r = line[-1]
        registers[r] *= 3
        i += 1
    elif line.startswith("inc"):
        r = line[-1]
        registers[r] += 1
        i += 1
    elif line.startswith("jmp"):
        parts = line.split(" ")
        offset = int(parts[-1])
        i += offset
    elif line.startswith("jie"):
        parts = line.split(" ")
        r = parts[1][0]
        offset = int(parts[-1])
        if registers[r] % 2 == 0:
            i += offset
        else:
            i += 1
    elif line.startswith("jio"):
        parts = line.split(" ")
        r = parts[1][0]
        offset = int(parts[-1])
        if registers[r] == 1:
            i += offset
        else:
            i += 1



print(registers)

# part 1 answer: 184
# part 2 answer: 231