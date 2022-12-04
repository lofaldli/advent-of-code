from typing import NamedTuple
from aocd import data
        
class Cube(NamedTuple):
    x: int
    y: int
    z: int
        
    def __add__(self, other):
        return Cube(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z)

neighbors = {
    'nw': Cube( 0, 1,-1), 
    'ne': Cube( 1, 0,-1),
    'e' : Cube( 1,-1, 0),
    'se': Cube( 0,-1, 1),
    'sw': Cube(-1, 0, 1),
    'w' : Cube(-1, 1, 0),
}

def walk(coords, start=Cube(0,0,0)):
    current = start
    coords = iter(coords)
    for c in coords:
        if c in 'ns':
            c += next(coords)
        current += neighbors[c]
    return current
    
def process(instructions):
    grid = {}
    for line in instructions:
        pos = walk(line)
        if grid.get(pos, '.') == '.':
            grid[pos] = '#'
        else:
            grid.pop(pos)
    return grid
        
def count_neighbors(pos, grid):
    total = 0
    for neighbor in neighbors.values():
        if grid.get(pos + neighbor) == '#':
            total += 1
    return total


def step(grid):
    min_x = min(grid, key=lambda g: g.x).x
    max_x = max(grid, key=lambda g: g.x).x
    min_y = min(grid, key=lambda g: g.y).y
    max_y = max(grid, key=lambda g: g.y).y
    min_z = min(grid, key=lambda g: g.z).z
    max_z = max(grid, key=lambda g: g.z).z
    new_grid = {}
    for x in range(min_x-1, max_x + 2):
        for y in range(min_y-1, max_y + 2):
            for z in range(min_z-1, max_z + 2):
                pos = Cube(x, y, z)
                cell = grid.get(pos, '.')
                N = count_neighbors(pos, grid)
                if cell == '#':
                    if not (N == 0 or N > 2):
                        new_grid[pos] = '#'
                    pass
                elif cell == '.' and N == 2:
                    new_grid[pos] = '#'
    return new_grid
    
grid = process(data.splitlines())
print('part 1', list(grid.values()).count('#'))

for day in range(100):
    grid = step(grid)
    print(f'day {day+1}', list(grid.values()).count('#'))
