from aocd import data
import subprocess
from collections import defaultdict

def parse(line):
    x, y = line.split(' <-> ')
    return int(x), tuple(map(int, y.split(', ')))

groups = dict()
for l, rs in map(parse, data.split('\n')):
    groups[l] = rs

def graph(groups):
    rv = ['graph {']
    for k,v in groups.items():
        rv.append('%d -- %s' % (k, ','.join(map(str,v))))
    rv.append('}')
    return '\n'.join(rv)

g = graph(groups).encode()
subprocess.run('dot -Tsvg -o tree.svg'.split(), input=g)
print('generated tree.svg, get ready to count')
print('part 1: nodes in tree 0')
print('part 2: number of trees')
