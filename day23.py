from aocd import data
from collections import defaultdict
    
def val(x, regs):
    try:
        return int(x)
    except:
        return regs[x]

def part1(program):
    regs = defaultdict(int)
    ip = n_muls = 0
    while 0 <= ip < len(program):
        op, x, y = program[ip]
        y = val(y, regs)
        if op == 'set':
            regs[x] = y
        elif op == 'sub':
            regs[x] -= y
        elif op == 'mul':
            regs[x] *= y
            n_muls += 1        
        elif op == 'jnz':
            x = val(x, regs)
            if x != 0:
                ip += y
                continue
        ip += 1
    return n_muls

def part2(program):
    b = int(program[0][-1])
    h = 0
    b = (b*100)+100000
    c = b + 17000
    for x in range(b, c+1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h
        
program = tuple(map(split, data.splitlines()))
print('part 1:', part1(program))
print('part 2:', part2(program))