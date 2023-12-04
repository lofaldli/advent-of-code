from collections import Counter

def parse(data):
    for line in data.splitlines():
        _, _, numbers = line.partition(": ")
        winning, _, have = numbers.partition(" | ")
        winning = set(map(int, winning.split()))
        have = set(map(int, have.split()))
        yield len(winning & have)

def points(count):
    if count > 0:
        return 2 ** (count - 1)
    return 0

def count_total(num_winning):
    cards = Counter(range(len(num_winning)))
    for index, count in enumerate(num_winning):
        for offset in range(count):
            cards[index + offset + 1] += cards[index]
    return cards.total()

from aocd import data
num_winning = list(parse(data))
print("part 1", sum(map(points, num_winning)))
print("part 2", count_total(num_winning))
