from aocd import data

def parse(line):
    ab, c, pw = line.split()
    a, b = map(int, ab.split('-'))
    return a, b, c[0], pw

p1 = p2 = 0
for a, b, c, pw in map(parse, data.splitlines()):
    if a <= pw.count(c) <= b: 
        p1 += 1
    if (pw[a-1] == c) != (pw[b-1] == c):
        p2 += 1

print('part 1', p1) 
print('part 2', p2)
