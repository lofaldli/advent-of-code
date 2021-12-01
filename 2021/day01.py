from aocd import data

def diff(it):
    return [b-a for a, b in zip(it[:-1], it[1:])]

values = [int(x) for x in data.splitlines()]
print('part 1', sum(x > 0 for x in diff(values)))

rolling_sums = [sum(window) for window in zip(values[:-2], values[1:-1], values[2:])]
print('part 2', sum(x > 0 for x in diff(rolling_sums)))
