from aocd import data
from collections import defaultdict

def parse_lines(lines):
    comps = defaultdict(set)
    for line in lines:
        x, y = map(int, line.split('/'))
        comps[x].add(y)
        comps[y].add(x)
    return comps
    
def make_bridges(comps, bridge=[(0,0)]):
    _,y = bridge[-1]
    for x in comps[y]:
        if  ((y, x) not in bridge and (x, y) not in bridge):
            next = bridge + [(y, x)]
            yield next
            for b in make_bridges(comps, next):
                yield b

comps = parse_lines(data.splitlines())   
max_sum = longest = longest_sum = 0
for b in make_bridges(comps):
    max_sum = max(max_sum, sum(map(sum, b)))
    if len(b) > longest or len(b) == longest and sum(map(sum, b)) > longest_sum:
        longest = len(b)
        longest_sum = sum(map(sum, b))
print('part 1:', max_sum)
print('part 2:', longest_sum)