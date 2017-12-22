from aocd import data

def split(rows):
    return tuple(map(tuple, rows.split('/')))

def parse(line):
    return tuple(map(split, line.split(' => ')))

def flip(x):
    return tuple(tuple(reversed(s)) for s in x)

def rotate(x):
    if len(x) == 2:
        return ((x[1][0], x[0][0]), 
                (x[1][1], x[0][1]))
    elif len(x) == 3:
        return ((x[2][0], x[1][0], x[0][0]),
                (x[2][1], x[1][1], x[0][1]),
                (x[2][2], x[1][2], x[0][2]))

def make_rules(lines): # add rules for all rotations and flipped rotations
    rules = {}
    for line in lines:
        x, y = parse(line)
        xf = flip(x)
        rules[x] = y
        rules[xf] = y
        for _ in range(3):
            x = rotate(x)
            xf = rotate(xf)
            rules[x] = y
            rules[xf] = y
    return rules

def conquer(subgrids, rules): # what a mess..
    if len(subgrids) == 1:
        return rules[subgrids[0]]
    sz = int(len(subgrids)**0.5)
    next = []
    for i in range(0, len(subgrids), sz): # go through one row worth of subgrids at a time
        rows = tuple(zip(*(rules[sg] for sg in subgrids[i:i+sz]))) # apply the appropriate rule
        for row in rows:
            next.append(tuple(item for part in row for item in part)) # glue them together again
    return tuple(next)

def divide(grid): # divide the big grid into smaller grids
    if len(grid) % 2 == 0: # the small ones are either 2x2
        sz = 2
    elif len(grid) % 3 == 0: # or 3x3
        sz = 3
    subgrids = []
    for i in range(0,len(grid),sz):
        for j in range(0,len(grid[i]),sz):
            subgrids.append(tuple(g[j:j+sz] for g in grid[i:i+sz]))
    return tuple(subgrids)

rules = make_rules(data.splitlines())
grid = split('.#./..#/###')
for i in range(18):
    grid = conquer(divide(grid), rules)
    print(i+1, '/'.join(''.join(s) for s in grid).count('#'))