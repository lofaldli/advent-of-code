from aocd import data
from operator import lt,le,eq,ne,ge,gt
from collections import defaultdict

OPS = {'==': eq, '!=': ne, '<': lt,
       '<=': le, '>=': ge, '>': gt} 

def parse(line):
    target, dir, v, _, x, op, y = line.split()
    return target, dir, int(v), x, OPS[op], int(y)

regs = defaultdict(int)
max_val = 0
for target, dir, v, x, op, y in map(parse, data.split('\n')):
    if op(regs[x], y):
        regs[target] += v if dir == 'inc' else -v
        if regs[target] > max_val:
            max_val = regs[target]

print('part 1:', max(regs.values()))
print('part 2:', max_val)
