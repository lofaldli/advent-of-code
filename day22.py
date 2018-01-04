from aocd import data
from collections import defaultdict

def walk(pos, dir):
    return pos[0]+dir[0], pos[1]+dir[1]

def turn_left(dir):
    return -dir[1], dir[0]

def make_grid(lines):
    grid = defaultdict(int)
    radius = (len(lines)-1)//2
    y = radius
    for line in lines:
        x = -radius
        for sym in line:
            grid[(x, y)] = 2 if sym == '#' else 0
            x += 1
        y -= 1
    return grid

def infect(grid, rule, N=10000):
    pos = (0,0)
    dir = (0,1)
    n_infections = 0
    for step in range(N):
        state = grid[pos]
        if state == 0:
            dir = turn_left(dir)
        elif state == 1:
            pass
        elif state == 2:
            dir = turn_left(turn_left(turn_left(dir)))
        elif state == 3:
            dir = turn_left(turn_left(dir))
        grid[pos] = rule(state)
        n_infections += 1 if grid[pos] == 2 else 0
        pos = walk(pos, dir)
    return n_infections

grid = make_grid(data.splitlines())
print('part1:', infect(grid, lambda x: (x+2)%4))
grid = make_grid(data.splitlines())
print('part2:', infect(grid, lambda x: (x+1)%4, 10000000))