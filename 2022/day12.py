import time
import math

def draw(start, end, height, path):
    min_x = min(h[0] for h in height)
    max_x = max(h[0] for h in height)
    min_y = min(h[1] for h in height)
    max_y = max(h[1] for h in height)

    lines = []
    for y in range(min_y, max_y+1):
        line = []
        for x in range(min_x, max_x+1):
            pos = (x, y)
            if pos in path:
                line.append(' ')
            elif pos == end:
                line.append('E')
            else:
                line.append(chr(height[pos] + ord('a')))
        lines.append(''.join(line))
    return '\n'.join(lines)

def neighbors(pos):
    x, y = pos
    candidates = [
        (x-1, y), (x+1, y), (x, y-1), (x, y+1)
    ]
    yield from candidates

def reconstruct_path(came_from, current):
    def walk_backwards(current):
        while current in came_from:
            yield current
            current = came_from[current]
    return list(walk_backwards(current))[::-1]

def a_star(start, goal, h, d):
    """https://en.wikipedia.org/wiki/A*_search_algorithm"""
    open_set = [start]
    came_from = {}
    gscore = {start: 0}
    fscore = {start: h(start)}

    while open_set:

        # a heap would be faster, but it is simpler to just keep a sorted list...
        open_set.sort(key=lambda x: fscore[x]) 

        current = open_set[0]
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.pop(0)

        for neighbor in neighbors(current):
            tentative_gscore = gscore[current] + d(current, neighbor)
            if tentative_gscore < gscore.get(neighbor, math.inf):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_gscore
                fscore[neighbor] = tentative_gscore + h(neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)
        #print(draw(start, end, height, reconstruct_path(came_from, current)))
        #time.sleep(0.001)
    return None

def shortest_path(start, goal, height):
    def d(current, neighbor):
        """Cost function"""
        if neighbor not in height or height[neighbor] - height[current] > 1:
            return math.inf
        return 1

    def h(pos):
        """Heuristic function"""
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    return a_star(start, goal, h, d)
    
def parse(data):
    height = {}
    start = end = None
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == 'S':
                start = (x, y)
                c = 'a'
            elif c == 'E':
                end = (x, y)
                c = 'z'
            height[x,y] = ord(c) - ord('a')
    return start, end, height

if __name__ == '__main__':
    from aocd import data
    start, end, height = parse(data)

    path = shortest_path(start, end, height)
    print('part 1', len(path))

    shortest_paths = [shortest_path(pos, end, height) for pos, h in height.items() if h == 0]
    print('part 2', min(len(path) for path in shortest_paths if path is not None))
