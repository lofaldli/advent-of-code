from math import prod
from collections import Counter

def parse(line):
    index, _, draws = line.removeprefix("Game ").partition(": ")
    counters = []
    for draw in draws.split("; "):
        counter = Counter()
        for cube in draw.split(", "):
            count, _, color = cube.partition(" ")
            counter[color] = int(count)
        counters.append(counter)
    return int(index), counters

def find_minimum(draws):
    minimum = Counter()
    for draw in draws:
        minimum |= draw
    return minimum

from aocd import data
bag = Counter({"red": 12, "green": 13, "blue": 14})
part1 = part2 = 0
for index, counters in map(parse, data.splitlines()):
    if all(counter <= bag for counter in counters):
        part1 += index
    part2 += prod(find_minimum(counters).values())
print("part 1", part1)
print("part 2", part2)
