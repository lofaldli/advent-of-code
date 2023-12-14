import operator

def parse(data):
    for pattern in data.split("\n\n"):
        yield pattern.splitlines()

def transpose(lines):
    return ["".join(line) for line in zip(*lines)]

def distance(a, b):
    """Compare a and b element-wise and return the number of non-equal items"""
    return sum(map(operator.ne, a, b))

def find_reflection(lines, smudges=0):
    for index in range(1, len(lines)):
        if distance(lines[index-1], lines[index]) > smudges:
            # if two consecutive lines have more than the allowed number of smudges
            # it cannot be a reflection
            continue
        # compare the lines before and after the reflection
        before, after = lines[:index], lines[index:]
        if sum(map(distance, reversed(before), after)) == smudges:
            # return the current index if the number differences
            # matches the number of smudges
            return index
    return None

def summarize(lines, smudges=0):
    num = find_reflection(lines, smudges)
    if num is not None:
        # if a row reflection is found, return the index * 100
        return 100 * num
    # otherwise find the index of the column reflection by transposing the lines
    return find_reflection(transpose(lines), smudges)

from aocd import data
part1 = part2 = 0
for lines in parse(data):
    part1 += summarize(lines)
    part2 += summarize(lines, 1)
print("part 1", part1)
print("part 2", part2)
