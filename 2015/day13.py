from aocd import data
from itertools import permutations

scores = dict()
for line in data.split('\n'):
    p1, _, sign, score, *_, p2 = line.rstrip('.').split()
    scores[(p1, p2)] = int(score) if sign == 'gain' else -int(score)

people = set(x for x,y in scores.keys())

def happiness(arr):
    total = 0
    for i in range(len(arr)):
        p1, p2 = arr[i-1], arr[i]
        total += scores[(p1,p2)] + scores[(p2,p1)]
    return total

print('part 1:', max(map(happiness, permutations(people))))

me = 'Myself'
for p in people:
    scores[(me, p)] = 0
    scores[(p, me)] = 0
people.add(me)

print('part 2:', max(map(happiness, permutations(people))))
