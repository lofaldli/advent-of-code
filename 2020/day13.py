from aocd import data
from math import prod

def earliest(t, buses):
    id, wait = min((id - (t % id), id) for id, _ in buses)
    return id * wait

def chinese_remainder(n, a):
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Using_the_existence_construction
    # https://www.youtube.com/watch?v=zIFehsBHB8o
    total = 0
    N = prod(n)
    for ni, ai in zip(n, a):
        Ni = N // ni
        xi = pow(Ni, -1, ni)
        total += ai * xi * Ni
    return total % N

lines = data.splitlines()
buses = [(int(id), int(id)-offset) for offset, id in enumerate(lines[1].split(',')) if id != 'x']

print('part 1', earliest(int(lines[0]), buses))

n, a = zip(*buses)
print('part 2', chinese_remainder(n, a))    
