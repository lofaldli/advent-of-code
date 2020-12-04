from collections import Counter
from datetime import datetime
from aocd import data

a, b = map(int, data.split('-'))

part1 = part2 = 0
for pw in map(str, range(a, b + 1)):
    if list(pw) == sorted(pw):
        counts = Counter(pw).values()
        if max(counts) > 1:
            part1 += 1
        if 2 in counts:
            part2 += 1

print('part 1', part1)
print('part 2', part2)