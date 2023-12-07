from collections import Counter

def parse(data):
    for line in data.splitlines():
        hand, bid = line.split()
        yield hand, int(bid)

def typeof(hand):
    return [count for label, count in Counter(hand).most_common()]

def typeof_replace_jokers(hand):
    for label, count in Counter(hand).most_common():
        if label != "J":
            hand = hand.replace("J", label)
            break
    return typeof(hand)
   
def winnings(games, typeof, order):
    def strength(game):
        hand, bid = game
        return typeof(hand), [order.index(card) for card in hand]
    for rank, (hand, bid) in enumerate(sorted(games, key=strength), start=1):
        yield rank * bid

from aocd import data
games = list(parse(data))
print("part 1", sum(winnings(games, typeof, "23456789TJQKA")))
print("part 2", sum(winnings(games, typeof_replace_jokers, "J23456789TQKA")))
