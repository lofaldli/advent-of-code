import math
import time
import heapq
import functools
import collections

Blizzard = collections.namedtuple('Blizzard', 'pos direction')
moves = {
    '^': ( 0,-1),
    'v': ( 0, 1),
    '<': (-1, 0),
    '>': ( 1, 0),
}

def parse(data):
    def blizzards():
        for y, line in enumerate(data.splitlines()):
            for x, cell in enumerate(line):
                if cell in '^v<>':
                    yield Blizzard((x,y), cell)

    def walls():
        for y, line in enumerate(data.splitlines()):
            for x, cell in enumerate(line):
                if cell == '#':
                    yield x, y

    return frozenset(blizzards()), frozenset(walls())

def reconstruct_path(came_from, current):
    def walk_backwards(current):
        while current in came_from:
            yield current
            current = came_from[current]
    return list(walk_backwards(current))[::-1]

def a_star(start, goal, h, d):
    """https://en.wikipedia.org/wiki/A*_search_algorithm"""
    came_from = {}
    gscore = {start: 0}
    fscore = {start: h(start)}
    open_set = [(fscore[start], start)]

    while open_set:
        _, current = heapq.heappop(open_set)

        # only compare the first two elements of the location
        if current[:2] == goal[:2]:
            return reconstruct_path(came_from, current)

        for neighbor in neighbors(current):
            tentative_gscore = gscore[current] + d(current, neighbor)
            if tentative_gscore < gscore.get(neighbor, math.inf):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_gscore
                fscore[neighbor] = tentative_gscore + h(neighbor)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (fscore[neighbor], neighbor))
    return None

@functools.cache
def bounds(walls):
    return (
        max(x for x, _ in walls),
        max(y for _, y in walls),
    )

@functools.cache
def move(blizzard, walls):
    x_max, y_max = bounds(walls)
    x, y = blizzard.pos
    dx, dy = moves[blizzard.direction]
    x += dx
    y += dy
    if x == 0:
        x = x_max - 1
    if x == x_max:
        x = 1
    if y == 0:
        y = y_max - 1
    if y == y_max:
        y = 1
    pos = x, y
    return Blizzard(pos, blizzard.direction)

@functools.cache
def update(blizzards, walls):
    """Move all blizzards one step"""
    return frozenset(move(blizzard, walls) for blizzard in blizzards)

@functools.cache
def get_state(blizzards, walls, T):
    """Get the state of all blizzards at time T"""
    for t in range(T):
        blizzards = update(blizzards, walls)
    return frozenset(blizzard.pos for blizzard in blizzards)

def neighbors(current):
    """Returns the neigbors of the current tile, one time step in the future"""
    candidates = (
                 ( 0,-1),         
        (-1, 0), ( 0, 0), ( 1, 0),
                 ( 0, 1),         
    )
    x, y, t = current
    yield from ((x+dx, y+dy, t+1) for (dx,dy) in candidates)

def shortest_path(start, goal, blizzards, walls):
    def d(current, neighbor):
        """Cost function"""
        x, y, t = neighbor

        if (x, y) in get_state(blizzards, walls, t):
            return math.inf

        if not (0 <= x <= x_max and 0 <= y <= y_max):
            return math.inf

        if (x, y) in walls:
            return math.inf
        return 1

    def h(pos):
        """Heuristic function"""
        x, y, t = pos
        return abs(x - goal[0]) + abs(y - goal[1])

    return a_star(start, goal, h, d)

def dump(blizzards, walls, current, visited):
    def inv(s):
        return f'\x1b[7m{s}\x1b[m'

    def red(s):
        return f'\x1b[101m{s}\x1b[m'

    def green(s):
        return f'\x1b[102m{s}\x1b[m'

    x_max, y_max = bounds(walls)
    counter = collections.Counter(blizzard.pos for blizzard in blizzards)
    blizzard_dict = dict(blizzards)
    lines = []
    for y in range(y_max+1):
        line = []
        for x in range(x_max+1):
            if (x, y) in blizzard_dict:
                c = 'X' if counter[x,y] > 1 else blizzard_dict[x,y]
            elif (x, y) in walls:
                c = inv(' ')
            elif (x, y) == current:
                c = green('@')
            else:
                c = ' '
            if (x,y) in visited:
                c = red(c)
            line.append(c)
            
        lines.append(''.join(line))
    return '\n'.join(lines)

def animate(start, path, blizzards, walls):
    frame = dump(blizzards, walls, start[:2], [])
    x, y, t = start
    print(f'x = {x:3} y = {y:2} t = {t:3}')
    print(frame)
    time.sleep(3)
    visited = [start[:2]]
    for current in path:
        blizzards = update(blizzards, walls)
        frame = dump(blizzards, walls, current[:2], visited)
        x, y, t = current
        print(f'x = {x:3} y = {y:2} t = {t:3}')
        print(frame)
        time.sleep(0.02)
        visited.append((x,y))
    time.sleep(3)

if __name__ == '__main__':
    from aocd import data
    blizzards, walls = parse(data)
    x_max, y_max = bounds(walls)
    path = []

    start = (1, 0, 0)
    goal = (x_max-1, y_max, None)
    path.extend(
        shortest_path(start, goal, blizzards, walls)
    )
    print('part 1', len(path))

    start = (x_max-1, y_max, len(path))
    goal = (1, 0, None)
    path.extend(
        shortest_path(start, goal, blizzards, walls)
    )

    start = (1, 0, len(path))
    goal = (x_max-1, y_max, None)
    path.extend(
        shortest_path(start, goal, blizzards, walls)
    )
    print('part 2', len(path))

    #animate((1, 0, 0), path, blizzards, walls)
