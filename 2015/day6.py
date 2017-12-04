from aocd import data

def parse(line):
    *cmd, fro, _, to = line.split(' ')
    return ' '.join(cmd), tuple(map(int, fro.split(','))), tuple(map(int, to.split(',')))

def logic1(fun, x):
    if fun == 'turn on':
        return True
    elif fun == 'turn off':
        return False
    elif fun == 'toggle':
        return not x

def logic2(fun, x):
    if fun == 'turn on':
        return x + 1
    elif fun == 'turn off':
        return max(0, x - 1)
    elif fun == 'toggle':
        return x + 2

def solve(cmds, logic):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for cmd in cmds:
        fun, (x0, y0), (x1,y1) = cmd
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                lights[x][y] = logic(fun, lights[x][y])
    return sum(map(sum, lights))

cmds = tuple(map(parse, data.split('\n')))
print('part 1:', solve(cmds, logic1))
print('part 2:', solve(cmds, logic2))
