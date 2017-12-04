from aocd import data

def parse_dir(dir):
    return {'^': (0,1), '<': (-1,0), '>': (1,0), 'v': (0,-1)}[dir]

def move(pos, dir):
    return pos[0]+dir[0], pos[1]+dir[1]

def traverse(start, dirs):
    visited = set()
    pos = start
    for dir in dirs:
        visited.add(pos)
        pos = move(pos, dir)
    return visited

dirs = tuple(map(parse_dir, data))

santa = traverse((0,0), dirs)
print('part 1:', len(santa))

santa = traverse((0,0), dirs[::2])
robo = traverse((0,0), dirs[1::2])
print('part 2:', len(santa | robo))
