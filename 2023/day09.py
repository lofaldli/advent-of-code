def parse(data):
    for line in data.splitlines():
        yield tuple(int(x) for x in line.split())

def diff(x):
    return tuple(x[i+1] - x[i] for i in range(len(x) - 1))

def extrapolate(x, direction="forwards"):
    dx = diff(x)
    if not any(dx):
        return x[0]
    if direction == "forwards":
        return x[-1] + extrapolate(dx, direction)
    else:
        return x[0] - extrapolate(dx, direction)

from aocd import data
part1 = part2 = 0
for history in parse(data):
    part1 += extrapolate(history)
    part2 += extrapolate(history, "backwards")
print("part 1", part1)
print("part 2", part2)
