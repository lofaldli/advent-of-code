from aocd import data
import operator
from itertools import combinations
from functools import reduce

def solve(numbers, n):
    for c in combinations(numbers, n):
        if sum(c) == 2020:
            return reduce(operator.mul, c, 1)

numbers = [int(x) for x in data.split()]
print('part 1', solve(numbers, 2))
print('part 2', solve(numbers, 3))
