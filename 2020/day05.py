from aocd import data

T = str.maketrans('FBLR', '0101')
ids = sorted([int(line.translate(T), 2) for line in data.splitlines()])

print('part 1', ids[-1])
print('part 2', [i for i in range(ids[0], ids[-1]) if i not in ids][0])
