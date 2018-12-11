from collections import defaultdict, deque


def get_highest_score(players=468, last_marble_value=71010):
    CLOCKWISE = -1
    COUNTER_CW = 1
    
    marbles = last_marble_value + 1
    player_scores = defaultdict(int)

    circle = deque([0])
    turn = 0
    for current_marble in range(1, marbles):
        turn += 1
        player = turn % players + 1

        if current_marble % 23 == 0:
            circle.rotate(COUNTER_CW*7)
            player_scores[player] += current_marble + circle.pop()
            circle.rotate(CLOCKWISE)
        else:
            circle.rotate(CLOCKWISE)
            circle.append(current_marble)
            
    return max(player_scores.values())


# part 1
print(get_highest_score())

# part 2
print(get_highest_score(last_marble_value=71010*100))
