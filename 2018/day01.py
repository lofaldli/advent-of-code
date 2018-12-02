from aocd import data
from itertools import cycle

xs = data.splitlines()

print('part 1:', sum(map(int, xs)))

n, ns = 0, set([0, ])
for x in cycle(map(int, xs)):
    n += x
    if n in ns:
        break
    ns.add(n)
print('part 2:', n)

