from aocd import data
from itertools import combinations

words = data.splitlines()

two, three = 0, 0
for w in words:
    c = [w.count(l) for l in set(w)]
    two += 2 in c
    three += 3 in c
print('part 1:', two * three)

for v, w in combinations(words, 2):
    diff = [k != l for k, l in zip(v, w)]
    if sum(diff) == 1:
        i = diff.index(True)
        break
print('part 2:', w[:i] + w[i+1:])
