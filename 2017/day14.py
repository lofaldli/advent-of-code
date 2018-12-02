from aocd import data
from day10 import hash

def to_bits(hex_str):
    return ''.join(format(int(x, 16), '04b') for x in hex_str)

def neighbors(r, c):
    return ((r-1, c), (r, c-1), (r, c+1), (r+1, c))

def set_group(r, c, id, grid):
    grid[r][c] = str(id)
    for x, y in neighbors(r,c):
        if 0 <= x < len(grid) and 0 <= y < len(grid[r]) and grid[x][y] == '#':
            set_group(x, y, id, grid)

def groupify(grid):
    grid = [[x for x in row.replace('1','#').replace('0', '.')] for row in grid]
    id = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '#':
                id += 1
                set_group(r, c, id, grid)
    return id

grid = tuple(map(to_bits, (hash('%s-%d' % (data, salt)) for salt in range(128))))
print('part 1:', sum(row.count('1') for row in grid))
print('part 2:', groupify(grid))
