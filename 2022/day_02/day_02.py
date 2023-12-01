guide = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        guide.append(line.split())
    
RESULT_POINT_MAP = {
    "win": 6,
    "tie": 3,
    "loss": 0
}

game_points = []
for opponent, you in guide:
    points = dict(zip("XYZ", (1, 2, 3)))[you]
    if (opponent, you) in zip("ABC", "XYZ"):  # TIE
        points += RESULT_POINT_MAP["tie"]
    elif (opponent, you) in zip("ABC", "YZX"):
        points += RESULT_POINT_MAP["win"]

    game_points.append(points)

print(sum(game_points))  # 13221

ACTUAL_SELECTION_POINT_MAP = {
    'A': 1,
    'B': 2,
    'C': 3
}

# x - lose, y - draw, z - win
move_index = dict(zip("XYZ", (0, 1, 2)))
oppenent_result_move_map = {
    "A": "CAB",
    "B": "ABC",
    "C": "BCA"
}

game_points = []
for opponent, result in guide:
    you = oppenent_result_move_map[opponent][move_index[result]]
    points = ACTUAL_SELECTION_POINT_MAP[you]
    if opponent == you:  # tie
        points += RESULT_POINT_MAP["tie"]
    elif (opponent, you) in zip("ABC", "BCA"):  # a win
        points += RESULT_POINT_MAP["win"]
    
    game_points.append(points)

print(sum(game_points))  # 13131