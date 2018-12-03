from re import findall
from aocd import data
from collections import defaultdict

def parse(line):
    return map(int, findall(r'-?\d+', line))

sheet = defaultdict(int)
patches = defaultdict(list)
for id, l, t, w, h in map(parse, data.splitlines()):
    for x in range(w):
        for y in range(h):
            sheet[(x+l, y+t)] += 1
            patches[id].append((x+l, y+t))
print('part 1', sum(x>1 for x in sheet.values()))

for id, patch in patches.items():
    if all(sheet[(x,y)]==1 for x,y in patch):
        print('part 2', id)
        break
