from aocd import data

groups = [
    [int(item) for item in group.split()] 
    for group in data.split("\n\n")
]

sorted_sums = sorted([sum(group) for group in groups], reverse=True)

print('part 1', sorted_sums[0])
print('part 2', sum(sorted_sums[:3]))

