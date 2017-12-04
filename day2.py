from aocd import data
from itertools import combinations

rows = [list(map(int, row.split('\t'))) for row in data.split('\n')]
print('part 1:', sum(max(r) - min(r) for r in rows))
print('part 2:', sum(y // x for r in rows for x, y in combinations(sorted(r), 2) if y % x == 0))
