from aocd import data

def run(program):
    acc = ip = 0
    seen = set()
    while ip not in seen and ip < len(program):
        op, x = program[ip]
        seen.add(ip)
        if op == 'acc':
            acc += x
        elif op == 'jmp':
            ip += x - 1
        ip += 1
    return acc, ip

def fix(program):
    for i, (op, x) in enumerate(program):
        if op == 'jmp':
            yield program[:i] + [('nop', x)] + program[i+1:]
        elif op == 'nop':
            yield program[:i] + [('jmp', x)] + program[i+1:]    
        
def parse(line):
    op, x = line.split(' ')
    return op, int(x)

def run_fixed(program):
    for fixed in fix(program):
        acc, ip = run(fixed)
        if ip == len(program):
            return acc

program = list(map(parse, data.splitlines()))
print('part 1', run(program)[0])
print('part 2', run_fixed(program))
