from collections import defaultdict, deque

CLOCKWISE = -1
COUNTER_CW = 1


def get_highest_score(players=468, last_marble_value=71010):
    marbles = last_marble_value + 1
    player_scores = defaultdict(int)

    circle = deque([0])
    turn = 0
    for current_marble in range(1, marbles):
        turn += 1
        player = turn % players + 1

        if current_marble % 23 != 0:
            circle.rotate(CLOCKWISE)
            circle.append(current_marble)
        else:
            circle.rotate(COUNTER_CW*7)
            player_scores[player] += current_marble + circle.pop()
            circle.rotate(CLOCKWISE)

    return max(player_scores.values())


# part 1
print(get_highest_score())

# part 2
print(get_highest_score(last_marble_value=71010*100))
