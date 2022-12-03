import re
from aocd import data

regs = [0 for _ in range(3)]
OPS = {
    'addr': lambda a,b: regs[a] + regs[b],
    'addi': lambda a,b: regs[a] + b,
    'mulr': lambda a,b: regs[a] * regs[b],
    'muli': lambda a,b: regs[a] * b,
    'banr': lambda a,b: regs[a] & regs[b],
    'bani': lambda a,b: regs[a] & b,
    'borr': lambda a,b: regs[a] | regs[b],
    'bori': lambda a,b: regs[a] | b,    
    'setr': lambda a,b: regs[a],
    'seti': lambda a,b: a,
    'gtir': lambda a,b: int(a > regs[b]),
    'gtri': lambda a,b: int(regs[a] > b),
    'gtrr': lambda a,b: int(regs[a] > regs[b]),
    'eqir': lambda a,b: int(a == regs[b]),
    'eqri': lambda a,b: int(regs[a] == b),
    'eqrr': lambda a,b: int(regs[a] == regs[b])
}

def eval(func, a, b, c):
    regs[c] = func(a, b)
    
def check(before, after, a, b, c):
    global regs
    opcodes = set()
    for opcode, func in OPS.items():
        regs = before[:]
        eval(func, a, b, c)
        if all(x == y for x,y in zip(regs, after)):
            opcodes.add(opcode)
    return opcodes

def get_numbers(line):
    return list(map(int ,re.findall(r'\d+', line)))
    
def collapse(candidates):
    solved = set()
    for s in filter(lambda c: len(c) == 1, candidates):
        solved |= s
    for i, c in enumerate(candidates):
        if len(c) == 1:
            continue
        candidates[i] = c - solved
    
lines = iter(data.splitlines())

for i in range(16):
  candidates = [set(OPS.keys()) for _ in range(len(OPS))]
    
total = 0   
while True:
    before = get_numbers(next(lines))
    if len(before) == 0:
        break
    op, a, b, c = get_numbers(next(lines))
    after = get_numbers(next(lines))
    opcodes = check(before, after, a, b, c)
    if len(opcodes) > 2:
        total+=1
    next(lines)
    candidates[op] -= (candidates[op] - opcodes)
print('part 1', total)
    
while any(len(c) != 1 for c in candidates):
    collapse(candidates)
    
opcodes = [list(c)[0] for c in candidates]
regs = [0 for _ in range(4)]
next(lines)
next(lines)
while True:
    try:
        op, a, b, c = get_numbers(next(lines))
    except:
        break
    eval(OPS[opcodes[op]], a, b, c)
print('part 2', regs[0])
