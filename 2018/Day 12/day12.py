from time import perf_counter as pc
from collections import deque
from itertools import islice


def next_generation(pots):
    # create a deque trailer rather than a whole new list
    # as you loop through, popleft fom trailer to pots out of influence

    # can you do this quickly of over dict?
    # label -> state

    next_gen = deque()

    # check pot before
    first_label, first_state = pots[0]
    second_label, second_state = pots[1]
    observation = f"...{first_state}{second_state}"

    left_label = first_label - 1
    left_state = notes[observation]
    previous_pot = (left_label, left_state)
    if "#" in previous_pot:
        next_gen.append(previous_pot)

    for i, (label, state) in enumerate(pots):

        observation = ""
        if i < 2:
            observation += '.' * (2-i)

        observation += "".join([s for (l, s) in islice(pots, max(0, i-2), i+3)])

        if i > len(pots)-3:
            observation += '.' * (i+3 - len(pots))

        updated_pot = (label, notes[observation])
        next_gen.append(updated_pot)

    # check pot after
    first_l_label, first_l_state = pots[-1]
    second_l_label, second_l_state = pots[-2]
    observation = f"{second_l_state}{first_l_state}..."

    right_label = first_l_label + 1
    right_state = notes[observation]
    next_pot = (right_label, right_state)
    if "#" in next_pot:
        next_gen.append(next_pot)

    # remove empty pots from beginning
    while True:
        left_most = next_gen.popleft()
        if "#" in left_most:
            next_gen.appendleft(left_most)
            break

    return next_gen


with open('input.txt') as f:
    lines = [line.strip() for line in f]

pots = list(enumerate(lines[0][15:]))

notes = {}
for line in lines[2:]:
    k = line[:5]
    v = line[-1]

    notes[k] = v

print("0", "".join([s for l, s in pots]))

# lists
# 5* 10**10
# ** 4 -> 1.5
# ** 5 -> 14
# ** 6 -> 147

# deques
# ** 5 ->

start = pc()
for i in range(5*10**4):
    pots = next_generation(pots)
    # print("".join([s for l, s in pots[:50]]))
    # print(i+1, "".join([s for l, s in pots]))

print(sum([l for l, s in pots if s == "#"]))

print(pc()-start)

# 45689663 - incorrect, too low