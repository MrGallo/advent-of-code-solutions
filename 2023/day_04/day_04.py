cards = []
with open("input.txt", "r") as f:
    for line in f.read().split("\n"):
        _, useful = line.split(": ")
        winning, yours = useful.split(" | ")
        winning = set(map(int, winning.split()))
        yours = set(map(int, yours.split()))
        cards.append((winning, yours))

total_points = 0
for winning, yours in cards:
    intersection = winning & yours
    if intersection:
        points = 2 ** (len(intersection) - 1)
        total_points += points

print(total_points)

# Part 2

def count_cards(cards):
    total = 0
    memo = {}
    for i in range(len(cards)):
        total += count_children(cards, i, memo)
    return total

def count_children(cards, i, memo = None):
    if i >= len(cards):
        return 0

    if memo is None:
        memo = {}
    
    if i in memo.keys():
        return memo[i]
    
    count = 1
    winning, yours = cards[i]
    intersection = winning & yours
    num_copies = len(intersection)
    for n in range(1, num_copies + 1):
        count += count_children(cards, i + n, memo)

    memo[i] = count
    return count

print(count_cards(cards))  # Part 2: 5554894