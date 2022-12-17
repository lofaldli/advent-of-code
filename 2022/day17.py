import time
import itertools

shapes = (
    (
        (0, 0), (1, 0), (2, 0), (3, 0)
    ),
    (
                (1, 2),
        (0, 1), (1, 1), (2, 1),
                (1, 0),
    ),
    (
                        (2, 2),
                        (2, 1),
        (0, 0), (1, 0), (2, 0),
    ),
    (
        (0, 3),
        (0, 2),
        (0, 1),
        (0, 0),
    ),
    (
        (0, 1), (1, 1),
        (0, 0), (1, 0),
    ),
)

def draw(top, current, rocks, height=40):
    def row_pixels(y):
        for x in range(7):
            if (x, y) in current:
                yield '@'
            elif (x, y) in rocks:
                yield '#'
            else:
                yield '.'

    def lines():
        bottom = max(0, top+6-height)
        for y in reversed(range(bottom, bottom+height)):
            line = ''.join(row_pixels(y))
            yield '|' + line + '|' 
        yield "+-------+"

    return '\n'.join(lines())
            
def move(shape, offset):
    dx, dy = offset
    return tuple((x+dx, y+dy) for x, y in shape)

def spawn(num_dropped):
    return shapes[num_dropped % len(shapes)]

def simulate(jets, N=2022, visualize=False):
    top = num_dropped = 0
    rocks = set()
    paths = dict()

    shape = spawn(num_dropped)
    current = move(shape, (2, top + 3))
    num_dropped += 1
    path = []

    if visualize:
        print(draw(top, current, rocks))
        print('dropped', num_dropped)
        print('top', top)
        time.sleep(2)

    for step, jet in itertools.cycle(enumerate(jets)):

        dx = -1 if jet == '<' else 1
        if all(0 <= x+dx < 7 and (x+dx, y) not in rocks for (x, y) in current):
            # move the current rock sideways
            current = move(current, (dx, 0))
            path.append(jet)

        if all(y > 0 and (x, y-1) not in rocks for (x, y) in current):
            # move the current rock down
            current = move(current, (0, -1))
            path.append(-1)
        else:
            # the current rock cannot move further down and comes to rest

            # if we have seen the current shape take the same path with the same instructions we are in a cycle
            path = tuple(path)
            if (shape, step, path) in paths:
                # the last time we saw this configuration was the beginning of the cycle
                num_dropped_offset, top_offset = paths[(shape, step, path)]

                # compare the current number of rocks with at the beginning of the cycle
                # to determine how many rocks are dropped per cycle
                cycle_length = num_dropped - num_dropped_offset

                # do the same for the top to find the growth per cycle
                growth_per_cycle = top - top_offset

                # compute the number of complete and partial cycles required to reach N rocks
                complete_cycles, remainder = divmod(N - num_dropped_offset, cycle_length)

                # simulate the number of rocks dropped outside of complete cycles
                rest = simulate(jets, remainder + num_dropped_offset)
                return growth_per_cycle * complete_cycles + rest

            # keep track of the current shape, position in the list of jets and the path taken as it comes to rest
            paths[shape, step, path] = (num_dropped, top)

            rocks.update(current)
            top = max(top, max(y for _, y in current) + 1)
            shape = spawn(num_dropped)
            current = move(shape, (2, top + 3))
            path = []
            num_dropped += 1

        if visualize:
            print(draw(top, current, rocks))
            print('dropped', num_dropped)
            print('top', top)
            time.sleep(1 / num_dropped)

        if num_dropped == N + 1:
            if visualize:
                time.sleep(2)
            return top


if __name__ == '__main__':
    from aocd import data
    print('part 1', simulate(data))
    print('part 2', simulate(data, 1000000000000))
