import time
import itertools
import collections

neighbors = {
    'N': ((-1,-1), ( 0,-1), ( 1,-1)), # NW N NE
    'S': ((-1, 1), ( 0, 1), ( 1, 1)), # SW S SE
    'W': ((-1,-1), (-1, 0), (-1, 1)), # NW W SW
    'E': (( 1,-1), ( 1, 0), ( 1, 1)), # NE E SE
}

all_neighbors = set(
    itertools.chain.from_iterable(
        neighbors.values()
    )
)

moves = {
    'N': ( 0,-1),
    'S': ( 0, 1),
    'W': (-1, 0),
    'E': ( 1, 0),
}

def bounds(elves):
    return (
        min(x for x, _ in elves),
        max(x for x, _ in elves),
        min(y for _, y in elves),
        max(y for _, y in elves),
    )

def parse(data):
    for y, line in enumerate(data.splitlines()):
        for x, tile in enumerate(line):
            if tile == '#':
                yield x, y

def dump(elves):
    x_min, x_max, y_min, y_max = bounds(elves)
    lines = []
    for y in range(y_min, y_max + 1):
        line = []
        for x in range(x_min, x_max + 1):
            if (x, y) in elves:
                line.append('#')
            else:
                line.append(' ')
        lines.append(''.join(line))
    return '\n'.join(lines)

def move(elf, elves, directions):
    x, y = elf
    # if the elf does not have any neighbors it doesn't move
    if all((x+dx, y+dy) not in elves for (dx, dy) in all_neighbors):
        return x, y

    # check each direction for neighbors and move in the first free direction
    for direction in directions:
        if all((x+dx, y+dy) not in elves for (dx, dy) in neighbors[direction]):
            dx, dy = moves[direction]
            return x+dx, y+dy
    # if the elf has neighbors in all directions it doesn't move
    return x, y

def simulate(elves):
    def make_plans(elves, directions):
        for elf in elves:
            yield elf, move(elf, elves, directions)

    def make_moves(elves, plans):
        # use a Counter to keep track of how many elves plans the same move
        counter = collections.Counter(plans.values())
        for elf in elves:
            plan = plans[elf]
            # only move if no other elf has the same plan
            if counter[plan] == 1:
                yield plan
            else:
                yield elf

    directions = 'NSWE'
    previous = elves
    for num_rounds in itertools.count(1):
        plans = dict(make_plans(elves, directions))
        elves = set(make_moves(elves, plans))
        yield num_rounds, elves
        
        # if all elves are standing in the same place we are done
        if elves == previous:
            break
        previous = elves
        # rotate the directions one step to the left
        directions = directions[1:] + directions[:1]

def part1(elves):
    # simulate 10 rounds
    for num_rounds, elves in simulate(elves):
        if num_rounds == 10:
            break
    # calculate the area of the bounding rectangle and subtract the number of elves
    x_min, x_max, y_min, y_max = bounds(elves)
    area = (x_max - x_min + 1) * (y_max - y_min + 1)
    return area - len(elves)

def part2(elves, visualize=False):
    # the simulation will stop when no elves move anymore
    for num_rounds, elves in simulate(elves):
        if visualize:
            frame = dump(elves)
            print(frame)
            time.sleep(0.01)
    return num_rounds

if __name__ == '__main__':
    from aocd import data
    elves = set(parse(data))
    print('part 1', part1(elves))
    print('part 2', part2(elves))
