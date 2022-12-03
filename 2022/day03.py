from aocd import data
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part1(lines):
    total = 0
    for line in lines:
        first, second = line[:len(line)//2], line[len(line)//2:]
        common = set(first) & set(second)
        for c in common:
            total += priorities.find(c) + 1
    return total

def part2(lines):
    groups = zip(lines[::3], lines[1::3], lines[2::3])
    total = 0
    for a, b, c in groups:
        common = set(a) & set(b) & set(c)
        for c in common:
            total += priorities.find(c) + 1
    return total

lines = data.splitlines()
print('part 1', part1(lines))
print('part 2', part2(lines))

