from time import perf_counter as pc


def next_generation(pots_bin, last):
    iter_num = pots_bin << 4
    last += 2

    # build new
    new = 0
    power = 1
    while iter_num:
        observation = iter_num & 0b11111
        new += (notes[observation]) * power
        # print(observation, bin(observation), bin(new), sep='\t')
        iter_num = iter_num >> 1
        power *= 2

    # remove 0's from right
    while not (new & 1):
        new = new >> 1
        last -= 1

    return new, last


def pots_sum(pots, last):
    total = 0
    while pots:
        total += (pots & 1) * last
        pots = pots >> 1
        last -= 1

    return total


with open('input.txt') as f:
    lines = [line.strip() for line in f]

# Parse pots into binary representation
initial_state = lines[0][15:]


last = len(initial_state) - 1

pots = 0
for i, pot in enumerate(initial_state):
    pots = (pots << 1) + (pot == '#')
    # print(i, pot, bin(pots))



# create notes dict
notes = {}
for line in lines[2:]:
    key_string = line[:5]
    key_binary = int("0b"+key_string.replace('.', '0').replace('#', '1'), 2)
    notes[key_binary] = line[-1] == '#'
    # print(line, key_string, bin(key_binary), notes[key_binary], sep='\t')

start = pc()
for i in range(5*10**5):
    pots, last = next_generation(pots, last)

print(bin(pots), last)
print(pots_sum(pots, last))  # answer: 2049
print(pc()-start)

