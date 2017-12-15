from aocd import data
from collections import namedtuple

Layer = namedtuple('Layer', 'range period')

def severity(layers, delay=0):
    rv = 0
    for t in range(max(layers.keys()) + 1):
        if t in layers.keys() and (t + delay) % layers[t].period == 0:
            rv += (t + delay)*layers[t].range # a bit hacky to add delay here, but it handles
    return rv                                 # the cases when layer 0 is blocking in part 2

layers = {}
for line in data.split('\n'):
    d,r = map(int, line.split(': '))
    layers[d] = Layer(r, 2*r-2) # the period of a triangular wave

print('part 1:', severity(layers))
delay = 0
while severity(layers, delay) != 0:
    delay += 1
print('part 2:', delay)
