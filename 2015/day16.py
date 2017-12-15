import re
from aocd import data
from collections import namedtuple

def parse(line):
    _,_, *line = line.split()
    sue = {}
    for i in range(0, len(line), 2):
        k, v = line[i:i+2]
        sue[k] = int(v)
    return sue

def check1(sue, target):
    return sum(target[k] == v for k,v in sue.items()) == 3

def check2(sue, target):
    total = 0
    for k, v in sue.items():
        if k in ('cats', 'trees'):
            total += target[k] < v
        elif k in ('pomeranians', 'goldfish'):
            total += target[k] > v
        else:
            total += target[k] == v
    return total == 3

def find(sues, target, check):
    i = 0
    for sue in sues:
        i += 1
        if check(sue, target):
            break
    return i

lines = re.sub('[:,]', '', data).split('\n')
sues = tuple(map(parse, lines))
target = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
    'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1
}

print('part 1:', find(sues, target, check1))
print('part 2:', find(sues, target, check2))
