from aocd import data

neighbor_range = (-1, 0, 1)
NEIGHBORS = []
for dx in neighbor_range:
    for dy in neighbor_range:
        for dz in neighbor_range:
            for dw in neighbor_range:
                neighbor = (dx, dy, dz, dw)
                if any(d != 0 for d in neighbor):
                    NEIGHBORS.append(neighbor)
    

def minmax(it, dim):
    sorted_it = sorted(it, key=lambda x: x[dim])
    return sorted_it[0][dim], sorted_it[-1][dim]

def pos4d(state, w=0):
    min_x, max_x = minmax(state, 0)
    min_y, max_y = minmax(state, 1)
    min_z, max_z = minmax(state, 2)
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                yield x, y, z, w

def count(pos, state):
    x, y, z, w = pos
    total = 0
    for dx, dy, dz, dw in NEIGHBORS:
        x_, y_, z_, w_ = x + dx, y + dy, z + dz, w + dw
        if state.get((x_,y_,z_, w_), '.') == '#':
            total += 1
    return total

def process3d(state, w=0):
    next_state = dict()
    for pos in pos4d(state, w):
        cell = state.get(pos, '.')
        active = count(pos, state)

        if cell == '#' and active in (2,3):
            next_state[pos] = '#'
        elif cell == '.' and active == 3:
            next_state[pos] = '#'

    return next_state

def process4d(state):
    next_state = dict()
    min_w, max_w = minmax(state, 3)
    for w in range(min_w-1, max_w+2):
        next_state.update({**process3d(state, w)})
    return next_state

def run(state, processor):
    for _ in range(6):
        state = processor(state)
    return [v for v in state.values()].count('#')


state = dict()
z = w = 0
for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        state[(x,y,z,w)] = cell

print('part 1', run(state, process3d))
print('part 2', run(state, process4d))
