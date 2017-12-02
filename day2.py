#!/usr/bin/env python3
import sys, csv
from functools import reduce
from itertools import permutations

def part1(rows):
    print(reduce(lambda tot, row: tot + max(row) - min(row), rows, 0))

def part2(rows):
    total = 0
    for row in rows:
        total += sum(x // y for x, y in permutations(row, 2) if x%y ==0)
    print(total)

tsvin = csv.reader(sys.stdin, delimiter='\t')
rows = [list(map(int, row)) for row in tsvin]
part1(rows)
part2(rows)
