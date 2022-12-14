import itertools

def parse(data):
    def parse_points(line):
        for pos in line.split(' -> '):
            x, y = map(int, pos.split(','))
            yield x, y

    def points_to_line(start, end):
        x0, y0 = start
        x1, y1 = end
        if x0 == x1:
            # vertical line
            dy = int((y1-y0)/abs(y1-y0))
            yield from ((x0, y) for y in range(y0, y1+dy, dy))
        else:
            # horizontal line
            dx = int((x1-x0)/abs(x1-x0))
            yield from ((x, y0) for x in range(x0, x1+dx, dx))

    for line in data.splitlines():
        points = list(parse_points(line))
        for start, end in zip(points[:-1], points[1:]):
            yield from points_to_line(start, end)

def drop_sand(source, max_y, obstacles):
    x, y = source
    while y < max_y + 1:
        if (x, y + 1) not in obstacles:
            y += 1
        elif (x - 1, y + 1) not in obstacles:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in obstacles:
            x += 1
            y += 1
        else:
            # sand has come to rest
            return x, y
    # fallen below max_y + 1
    return x, y

def part1(source, max_y, obstacles):
    for i in itertools.count(1):
        _, y = pos = drop_sand(source, max_y, obstacles)
        obstacles.add(pos)
        if y > max_y:
            # a grain of sand is falling into the abyss
            break
    # i-1 grains of sand have fallen before the first one falls to the abyss
    return i - 1

def part2(source, max_y, obstacles):
    for i in itertools.count(1):
        pos = drop_sand(source, max_y, obstacles)
        obstacles.add(pos)
        if pos == source:
            # a grain of sand is blocking the source
            break
    # i grains of sand comes to rest before the source is blocked
    return i

if __name__ == '__main__':
    from aocd import data

    source = (500, 0)
    rocks = set(parse(data))
    max_y = max(y for _, y in rocks)
    print('part 1', part1(source, max_y, set(rocks)))
    print('part 2', part2(source, max_y, set(rocks)))
