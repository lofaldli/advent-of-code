from collections import defaultdict
from aocd import data

def solve(numbers, turns):
    history = defaultdict(list)

    for turn, n in enumerate(numbers):
        history[n].append(turn + 1)

    for turn in range(len(numbers), turns):
        if len(history[n]) == 1:
            n = 0
        else:
            n = history[n][-1] - history[n][-2]
        history[n].append(turn + 1)
    return n

numbers = [int(x) for x in data.split(',')]
print('part 1', solve(numbers, 2020))
print('part 2', solve(numbers, 30000000))
