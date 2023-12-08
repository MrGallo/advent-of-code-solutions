from itertools import count
from typing import List
from collections import defaultdict


def main():
    hands_and_bids = []
    with open("input.txt", "r") as f:
        for line in f.read().split("\n"):
            hand, bid = line.split()
            hands_and_bids.append((hand, int(bid)))
    
    bubble_sort(hands_and_bids)
    
    total_winnings = 0
    for rank, (hand, bid) in enumerate(hands_and_bids, 1):
        total_winnings += rank * bid
    
    print(total_winnings)  # 249748283

    # PART 2

    bubble_sort(hands_and_bids, joker_rule=True)
    total_winnings = 0
    for rank, (hand, bid) in enumerate(hands_and_bids, 1):
        total_winnings += rank * bid
    
    print(total_winnings)  # Part 2: 248029057


def bubble_sort(hands_and_bids, joker_rule: bool = False):
    for times in range(len(hands_and_bids) - 1):
        sorted = True
        for i in range(len(hands_and_bids) - 1 - times):
            a, b = hands_and_bids[i: i + 2]
            if hand_is_higher(a[0], b[0], joker_rule):
                tmp = hands_and_bids[i]
                hands_and_bids[i] = hands_and_bids[i + 1]
                hands_and_bids[i + 1] = tmp
                sorted = False
        if sorted:
            break


def card_is_higher(a: str, b: str, card_order: str = "23456789TJQKA") -> bool:
    card_rankings = dict(zip(card_order, count()))
    return card_rankings[a] > card_rankings[b]


def reduce_hand(hand: str, joker_rule: bool = False) -> List[int]:
    # Might need to memo repeated hands
    """Get the hand in the format [4, 1], for 4 of a kind, for example"""
    card_frequencies = defaultdict(int)
    for card in hand:
        card_frequencies[card] += 1
    

    if joker_rule:
        jokers = 0
        try:
            jokers = card_frequencies.pop("J")
        except KeyError:
            pass  # stays 0
    
    reduced_list = list(sorted(card_frequencies.values(), reverse=True))
    if joker_rule:
        try:
            reduced_list[0] += jokers
        except IndexError:  # 5 Jokers
            return (5,)
    
    return tuple(reduced_list)


def hand_is_higher(hand_a: str, hand_b: str, joker_rule: bool = False) -> bool:
    if hand_a == hand_b:
        raise ValueError(f"The hands are the same ({hand_a})")
    
    hand_rankings = dict(
        zip(
            (
                (1, 1, 1, 1, 1),  # high card
                (2, 1, 1, 1),     # one pair
                (2, 2, 1),        # two pair
                (3, 1, 1),        # three of a kind
                (3, 2),           # full house
                (4, 1),           # 4 of a kind
                (5,)              # 5 of a kind
            ),
            count()
        )
    )

    reduced_a = reduce_hand(hand_a, joker_rule)
    reduced_b = reduce_hand(hand_b, joker_rule)

    if reduced_a == reduced_b:
        for a, b in zip(hand_a, hand_b):
            if a == b:
                continue
            if joker_rule:
                return card_is_higher(a, b, "J23456789TQKA")
            return card_is_higher(a, b)
    
    return hand_rankings[reduced_a] > hand_rankings[reduced_b]
        

if __name__ == "__main__":
    main()