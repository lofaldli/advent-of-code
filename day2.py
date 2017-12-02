#!/usr/bin/env python3
import sys, csv
from itertools import combinations

def part1(rows):
    print(sum(max(r) - min(r) for r in rows))

def part2(rows):
    print(sum(y // x for r in rows for x, y in combinations(sorted(r), 2) if y % x == 0))

tsvin = csv.reader(sys.stdin, delimiter='\t')
rows = [list(map(int, row)) for row in tsvin]
part1(rows)
part2(rows)
