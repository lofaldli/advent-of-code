import math

def count_ways1(duration, record):
    """Brute force solution"""
    total = 0
    for t in range(1, duration):
        if t * (duration - t) > record:
            total += 1
    return total

def count_ways2(duration, record):
    """Solution using quadratic equations"""
    def quadsolve(a, b, c):
        d = b ** 2 - 4 * a * c
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return min(x1, x2), max(x1, x2)

    first, last = quadsolve(-1, duration, -(record + 1))
    return math.floor(last) - math.ceil(first) + 1

def part1(lines, count_ways):
    def parse(line):
        return [int(x) for x in line.split()[1:]]
    durations = parse(lines[0])
    records = parse(lines[1])
    return math.prod(map(count_ways, durations, records))

def part2(lines, count_ways):
    def parse(line): 
        return int("".join(line.split()[1:]))
    duration = parse(lines[0])
    record = parse(lines[1])
    return count_ways(duration, record)

from aocd import data
lines = data.splitlines()
print("part 1", part1(lines, count_ways2))
print("part 2", part2(lines, count_ways2))
