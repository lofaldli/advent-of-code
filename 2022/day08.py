import math

directions = (
    ( 0,-1), 
    ( 0, 1), 
    (-1, 0), 
    ( 1, 0),
)


def ray(origin, direction):
    row, col = origin
    drow, dcol = direction
    while True:
        row += drow
        col += dcol
        yield row, col


def visible(pos, trees):
    def trace(origin, direction):
        for pos in ray(origin, direction):
            if pos not in trees:
                return True

            if trees[pos] >= trees[origin]:
                return False
    
    return any(trace(pos, direction) for direction in directions)


def scenic(pos, trees):
    def trace(origin, direction):
        for distance, pos in enumerate(ray(origin, direction)):
            if pos not in trees:
                return distance

            if trees[pos] >= trees[origin]:
                return distance + 1

    return math.prod(trace(pos, direction) for direction in directions)


def parse(data):
    trees = {}
    for row, line in enumerate(data.splitlines()):
        for col, tree in enumerate(line):
            trees[row, col] = int(tree)

    return trees


if __name__ == '__main__':
    from aocd import data

    trees = parse(data)
    print('part 1', sum(visible(pos, trees) for pos in trees))
    print('part 2', max(scenic(pos, trees) for pos in trees))
