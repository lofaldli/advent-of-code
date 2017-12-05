from aocd import data

def solve(data, rule=None):
    instr = list(map(int, data.split('\n')))
    cur = 0
    i = 0
    while True:
        steps = instr[cur]
        instr[cur] += rule(steps) if rule else 1
        cur += steps
        i += 1
        if not 0 <= cur < len(instr):
            break
    return i

print('part 1:', solve(data))
print('part 2:', solve(data, lambda x: 1 if x < 3 else -1))
