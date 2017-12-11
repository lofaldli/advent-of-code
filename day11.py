from aocd import data

# https://www.redblobgames.com/grids/hexagons/#neighbors-cube
DIRS = {         'n': (0, 1,-1),
    'nw': (-1,1,0),          'ne': (1,0,-1),
    'sw': (-1,0,1),          'se': (1,-1,0),          
                 's': (0,-1, 1)}

def dist(a, b=(0,0,0)):
    return max(abs(x-y) for x,y in zip(a,b))

pos = (0,0,0)
max_dist = 0
for dir in data.split(','):
    pos = tuple(map(sum, zip(pos, DIRS[dir])))
    max_dist = max(max_dist, dist(pos))

print('part 1:', dist(pos))
print('part 2:', max_dist)
