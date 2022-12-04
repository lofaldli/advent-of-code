from aocd import data

def section(s):
    begin, end = s.split('-')
    return int(begin), int(end)

def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

def overlaps(a, b):
    return b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]

fully = partial = 0
for line in data.splitlines():
    a, b = map(section, line.split(','))
    if contains(a, b) or contains(b, a):
        fully += 1
    if overlaps(a, b) or overlaps(b, a):
        partial += 1
    
print('part 1', fully)
print('part 2', partial)
