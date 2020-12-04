from collections import defaultdict, deque
from aocd import data

def parse(line):
    return line.strip().split(')')

V = defaultdict(list)
for c, s in map(parse, data.splitlines()):
    V[c].append(s)

A = defaultdict(set)
stack = deque(['COM'])
while stack:
    c = stack.popleft()
    stack.extend(V[c])
    for s in V[c]:
        A[s] = set([c]) | A[c]
    
print('part 1:', sum(map(len, A.values())))

m = max(len(A[x]) for x in A['YOU'] & A['SAN'])
print('part 2:', len(A['YOU']) + len(A['SAN']) - 2*m - 2)