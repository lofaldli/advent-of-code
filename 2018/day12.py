import re
from aocd import data
lines = data.splitlines()

def grow(row):
    next_row = '..'
    for i in range(2, len(row) - 1):
        r = row[i-2:i+3]
        next_row += rules[r] if r in rules else '.'
    return next_row + '..'

def value(row, offset=4):
    total = 0
    for i, r in enumerate(row):
        if r == '#':
            total += i - offset
    return total

initial = lines.pop(0).split(': ')[1].strip()
lines.pop(0)
rules = {}
for line in lines:
    k, v = line.strip().split(' => ')
    rules[k] = v

row = '....' + initial[:] + '....'
for i in range(20):
    next_row = grow(row)
    print(row)
    if i == 19:
        print('part 1', value(next_row))

    stripped = next_row.strip('.')
    row = next_row
