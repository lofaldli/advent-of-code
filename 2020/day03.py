import operator
from functools import reduce
from aocd import data

rows = data.splitlines()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def solve(rows, right, down):
    return sum(row[(right * i) % len(row)] == '#' for i, row in enumerate(rows[::down]))

def prod(it):
    return reduce(operator.mul, it, 1)

print('part 1', solve(rows, 3, 1))
print('part 2', prod(solve(rows, right, down) for right, down in slopes))
