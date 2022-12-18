import time
import functools

def parse(data):
    for line in data.splitlines():
        yield tuple(map(int, line.split(',')))

@functools.lru_cache
def bounds(cubes):
    return (
        min(x for x,_,_ in cubes),
        max(x for x,_,_ in cubes),
        min(y for _,y,_ in cubes),
        max(y for _,y,_ in cubes),
        min(z for _,_,z in cubes),
        max(z for _,_,z in cubes),
    )

@functools.lru_cache(maxsize=10**4)
def find_neighbors(cube):
    x, y, z = cube
    return (
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1),
    )

def count_blocked(cubes):
    def blocked_sides():
        for cube in cubes:
            for neighbor in find_neighbors(cube):
                if neighbor in cubes:
                    yield 1

    return sum(blocked_sides())

def count_blocked_or_trapped(cubes):
    def blocked_or_trapped_sides():
        for cube in cubes:
            for neighbor in find_neighbors(cube):
                if neighbor in cubes or trapped_pocket(neighbor, cubes):
                    yield 1

    return sum(blocked_or_trapped_sides())

# keep track of all cubes we have checked so far if they are trapped or not
MEMO = dict()
def trapped_pocket(cube, cubes):
    if cube in MEMO:
        # we have already checked this one
        return MEMO[cube]

    x_min, x_max, y_min, y_max, z_min, z_max = bounds(cubes)
    def out_of_bounds(cube):
        x, y, z = cube
        return not (x_min < x < x_max and y_min < y < y_max and z_min < z < z_max)

    # keep track of all cubes belonging to the current room
    room = set([cube])

    while True: 
        # find all neighbors of all cubes that are empty and not already in the room
        neighbors = set()
        for cube in room:
            neighbors.update(
                neighbor for neighbor in find_neighbors(cube)
                if neighbor not in room and neighbor not in cubes
            )

        if len(neighbors) == 0:
            # all room neighbors are either cubes or already in the room
            for cube in room:
                # store each cube in the current room as being trapped
                MEMO[cube] = True
            return True

        if any(out_of_bounds(neighbor) for neighbor in neighbors):
            # at least one room neighbor is out of bounds -> it is not a trapped pocket
            for cube in room:
                # store each cube in the current room as not trapped
                MEMO[cube] = False
            return False

        room.update(neighbors)

def animate(cubes):
    def pixel(p):
        if p in cubes:
            return '#'
        elif trapped_pocket(p, cubes):
            return ' '
        else:
            return '.'

    x_min, x_max, y_min, y_max, z_min, z_max = bounds(cubes)
    def draw(z):
        lines = []
        for y in range(y_min, y_max+1):
            line = ''.join(
                pixel((x,y,z))
                for x in range(x_min, x_max+1)
            )
            lines.append(line)
        plane = '\n'.join(lines)
        print('z =', z, 'trapped =', plane.count(' '))
        print(plane)


    for z in range(z_min, z_max+1):
        draw(z)
        time.sleep(0.5)
    for z in reversed(range(z_min+1, z_max)):
        draw(z)
        time.sleep(0.5)

if __name__ == '__main__':
    from aocd import data
    cubes = frozenset(parse(data))

    total_sides = 6 * len(cubes)
    print('part 1', total_sides - count_blocked(cubes))
    print('part 2', total_sides - count_blocked_or_trapped(cubes))
    #animate(cubes)
