from aocd import data

neighbors = ((-1,-1), (0,-1), (1,-1),
             (-1, 0),         (1, 0),
             (-1, 1), (0, 1), (1, 1))

def count1(x, y, grid):
    n = 0
    for dx, dy in neighbors:
        x_, y_ = x + dx, y + dy
        if 0 <= y_ < len(grid) and 0 <= x_ < len(grid[y_]):
            if grid[y_][x_] == '#':
                n += 1
    return n

def count2(x, y, grid):
    n = 0
    for dx, dy in neighbors:
        x_, y_ = x + dx, y + dy
        while 0 <= y_ < len(grid) and 0 <= x_ < len(grid[y_]):
            cell = grid[y_][x_]
            if cell == '#':
                n += 1
                break
            if cell == 'L':
                break
            x_ += dx
            y_ += dy
    return n

def step(grid, checker, N):
    new_grid = []
    new_line = []
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            n = checker(x, y, grid)
            if cell == 'L' and n == 0:
                new_line.append('#')
            elif cell == '#' and n >= N:
                new_line.append('L')
            else:
                new_line.append(cell)
        new_grid.append(new_line)
        new_line = []
    return new_grid

def solve(grid, checker, N):
    next_grid = []
    while True:
        next_grid = step(grid, checker, N)
        if grid == next_grid:
            break
        grid = next_grid
    return sum(line.count('#') for line in grid)

grid = [list(line) for line in data.splitlines()]
print('part 1', solve(grid, count1, 4))
print('part 2', solve(grid, count2, 5))
