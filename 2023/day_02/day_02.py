import functools


MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14

games = []
with open("input.txt", "r") as f:
    for line in f.read().split("\n"):
        colon_i = line.index(":")
        rounds = list(
            tuple(round.split(", ")) 
            for round in map(
                str.strip,
                line[colon_i + 1:].split(";"))
        )
        games.append(rounds)

sum_ids = 0
for id, game in enumerate(games, 1):
    for rnd in game:
        color_amounts = {
            "red": MAX_RED,
            "green": MAX_GREEN,
            "blue": MAX_BLUE
        }
        possible = True
        for draw in rnd:
            amount, color = draw.split()
            amount = int(amount)
            color_amounts[color] -= amount
            if color_amounts[color] < 0:
                possible = False
                break
        if not possible:
            break

    if possible:
        sum_ids += id

print(sum_ids)  # Part 1: 2541

sum_powers = 0
for game in games:
    power = 0
    min_needed = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for rnd in game:
        for draw in rnd:
            amount, color = draw.split()
            amount = int(amount)
            if min_needed[color] < amount:
                min_needed[color] = amount
    power = functools.reduce(lambda x, y: x * y, min_needed.values())
    sum_powers += power

print(sum_powers)  # part 2: 66016