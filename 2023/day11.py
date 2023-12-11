import itertools

def transpose(lines):
    return ["".join(row) for row in zip(*lines)]

def find_empty(lines):
    return set(
        index for index, row in enumerate(lines) if "#" not in row
    )

def parse(lines):
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            if tile == "#":
                yield (x, y)

def minmax(a, b):
    return min(a, b), max(a, b)

def distance(a, b, empty_rows, empty_columns, expand=1):
    xmin, xmax = minmax(a[0], b[0])
    ymin, ymax = minmax(a[1], b[1])
    base = xmax - xmin + ymax - ymin
    expanded_rows = [1 for row in empty_rows if ymin < row < ymax]
    expanded_columns = [1 for column in empty_columns if xmin < column < xmax]
    return base + expand * (len(expanded_rows) + len(expanded_columns))

from aocd import data
lines = data.splitlines()
empty_rows = set(find_empty(lines))
empty_columns = set(find_empty(transpose(lines)))
galaxies = set(parse(lines))
part1 = part2 = 0
for a, b in itertools.combinations(galaxies, 2):
    part1 += distance(a, b, empty_rows, empty_columns) 
    part2 += distance(a, b, empty_rows, empty_columns, 999999) 
print("part 1", part1)
print("part 2", part2)
