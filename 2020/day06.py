from aocd import data

groups_of_sets = [[set(g) for g in group.split()] for group in data.split('\n\n')]
print('part 1', sum(len(set.union(*group)) for group in groups_of_sets))
print('part 2', sum(len(set.intersection(*group)) for group in groups_of_sets))
