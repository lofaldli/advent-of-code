from collections import Counter
from functools import reduce
from aocd import data

numbers = tuple(map(int, data.strip()))
  
w, h = 25, 6
N = w * h
layers = [tuple(numbers[i:i+N]) for i in range(0, len(numbers), N)]

counters = map(Counter, layers)
fewest_zeros = sorted(counters, key=lambda c: c[0])[0]

print('part 1:', fewest_zeros[1] * fewest_zeros[2])

im = reduce(lambda v, e: [p if v[i] == 2 else v[i] for i,p in enumerate(e)], layers)
colors = {0: ' ', 1: '#'}

print('part 2:')
lines = [im[i:i+w] for i in range(0, N, w)]
for line in lines:
  print(''.join(colors[p] for p in line))