guide = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        guide.append(line.split())
    
SELECTION_POINT_MAP = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

RESULT_POINT_MAP = {
    "win": 6,
    "tie": 3,
    "loss": 0
}

WIN_MAP = {
    ("A", "Y"): True,
    ("B", "Z"): True,
    ("C", "X"): True
}

game_points = []
for opponent, you in guide:
    print(opponent, you)
    points = SELECTION_POINT_MAP[you]

    win = WIN_MAP.get((opponent, you), False)
    if opponent == you:
        points += RESULT_POINT_MAP["tie"]
    elif win is True:
        points += RESULT_POINT_MAP["win"]

    game_points.append(points)

print(sum(game_points))