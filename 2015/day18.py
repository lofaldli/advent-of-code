from aocd import data

def try_check(r, c, grid):
    return grid[r][c] == '#' if 0 <= r < len(grid) and 0 <= c < len(grid[r]) else False

def neighbors_on(r, c, grid):
    return sum(try_check(x,y,grid) for x,y in ((r-1,c-1), (r-1, c), (r-1,c+1),
                                               (r  ,c-1),           (r  ,c+1),
                                               (r+1,c-1), (r+1, c), (r+1,c+1)))

def step(grid):
    next = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[r])):
            n = neighbors_on(r,c,grid)
            if grid[r][c] == '#' and n in (2,3) or grid[r][c] == '.' and n == 3:
                row.append('#')
            else:
                row.append('.')
        next.append(row)
    return next

def run(grid, broken=False):
    for _ in range(100):
        grid = step(grid)
        if broken:
            grid[0][0] = grid[-1][0] = grid[0][-1] = grid[-1][-1] = '#'
    return sum(r.count('#') for r in grid)

grid = list(list(x for x in line) for line in data.split('\n'))
print('part 1:', run(grid[:]))
grid[0][0] = grid[-1][0] = grid[0][-1] = grid[-1][-1] = '#'
print('part 2:', run(grid, True))
