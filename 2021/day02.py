from aocd import data

depth = depth2 = distance = 0
for line in data.splitlines():
    d, m = line.split()
    m = int(m)
    if d == 'forward':
        distance += m
        depth2 += depth * m 
    elif d == 'up':
        depth -= m
    elif d == 'down':
        depth += m

print('part 1', depth * distance)
print('part 2', depth2 * distance)
