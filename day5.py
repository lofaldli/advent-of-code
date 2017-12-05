from aocd import data

def rule1(steps):
    return 1

def rule2(steps):
    return 1 if steps < 3 else -1

def solve(data, rule):
    instr = list(map(int, data.split('\n')))
    cur = 0
    i = 0
    while True:
        steps = instr[cur]
        instr[cur] += rule(steps)
        cur += steps
        i += 1
        if not 0 <= cur < len(instr):
            break
    return i

print('part 1:', solve(data, rule1))
print('part 2:', solve(data, rule2))
