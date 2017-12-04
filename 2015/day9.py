from aocd import data
from itertools import permutations

def distance(route):
    total = 0
    for i in range(len(route)-1):
        fro, to = route[i:i+2]
        total += dists[tuple(sorted((fro,to)))]
        # print(' -> '.join(route), '=',total) # slower, but fun to watch  
    return total
        
cities = set()
dists = dict()
for line in data.split('\n'):
    fro, _, to, _, dist = line.split()
    cities.add(fro)
    cities.add(to)
    dists[tuple(sorted((fro, to)))] = int(dist)

print('part 1:', min(map(distance, permutations(cities))))
print('part 2:', max(map(distance, permutations(cities))))
