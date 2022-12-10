import time

def parse(data):
    for line in data.splitlines():
        direction, steps = line.split()
        yield direction, int(steps)

directions = {
    'U': ( 0, 1),
    'D': ( 0,-1),
    'L': (-1, 0),
    'R': ( 1, 0),
}

def move(pos, direction):
    x, y = pos
    dx, dy = direction
    return x + dx, y + dy

def drag_tail(H, T):
    dx = H[0] - T[0]
    dy = H[1] - T[1]

    if (abs(dx), dy) == (2, 0):
        direction = int(dx/2), 0
    elif (dx, abs(dy)) == (0, 2):
        direction = 0, int(dy/2)
    elif (abs(dx), abs(dy)) == (2, 1):
        direction = int(dx/2), dy
    elif (abs(dx), abs(dy)) == (1, 2):
        direction = dx, int(dy/2)
    elif (abs(dx), abs(dy)) == (2, 2):
        direction = int(dx/2), int(dy/2)
    else:
        direction = 0, 0

    return move(T, direction)

def draw(snake, visited, start=(0,0)):
    grid = {}
    for v in visited:
        grid[v] = '#'
    grid[start] = 's'

    if len(snake) == 2:
        grid[snake[1]] = 'T'
        grid[snake[0]] = 'H'
    else:
        for i in reversed(range(1,len(snake))):
            grid[snake[i]] = str(i)

    grid[snake[0]] = 'H'

    lines = []
    x0,y0 = snake[0]
    for y in range(y0-30, y0+31):
        line = []
        for x in range(x0-60, x0+61):
            line.append(grid.get((x, y), '.'))
        lines.append(''.join(line))
    return '\n'.join(reversed(lines))


def simulate(moves, N=2, visualize=False):
    start = (0,0)
    snake = [start for _ in range(N)]
    visited = set([start])
    for direction, steps in moves:
        for _ in range(steps):
            snake[0] = move(snake[0], directions[direction])
            for i in range(1, len(snake)):
                snake[i] = drag_tail(snake[i-1], snake[i])

            visited.add(snake[-1])

            if visualize:
                print(draw(snake, visited, start))
                time.sleep(0.001)

    return len(visited)


if __name__ == '__main__':
    from aocd import data
    moves = list(parse(data))
    print('part 1', simulate(moves))
    print('part 2', simulate(moves, N=10, visualize=True))
