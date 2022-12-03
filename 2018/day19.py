from aocd import data

regs = [0 for _ in range(6)]

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

lines = data.splitlines()
ip = int(lines.pop(0).split(' ')[1])


program = []
for line in lines:
    op, *args = line.split(' ')
    program.append((op, *map(int, args)))
#regs[0] = 1  # part 2
while 0 <= regs[ip] < len(program):
    op, a, b, c = program[regs[ip]]
    print(regs[ip], regs)
    eval(OPS[op], a, b, c)
    print(op, a, b, c, regs)
    regs[ip] += 1

print('reg 0', regs[0])
