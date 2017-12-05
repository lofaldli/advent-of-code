from aocd import data
from collections import defaultdict

def walk(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]

def layer(step): # (2N-1)^2 is the highest number on layer N
    return ((step**0.5)+1)//2

# https://en.wikipedia.org/wiki/Ulam_spiral
def ulam(x, start=(0,0)):
    pos = start
    dir = (1, 0)
    for step in range(1, x):
        pos = walk(pos, dir)
        if max(map(abs, walk(pos, dir))) > layer(step+1):
            dir = (-dir[1], dir[0]) # turn left
    return pos

number = int(data)
print('part 1:', sum(map(abs, ulam(number))))

pos = (0,0)
mem = defaultdict(int)
mem[pos] = 1
i = 2
while mem[pos] < number:
    pos = ulam(i)
    i+=1
    mem[pos] = sum(map(lambda dir: mem[walk(pos, dir)], ((-1, 1), (0, 1), (1, 1),
                                                         (-1, 0),         (1, 0),
                                                         (-1,-1), (0,-1), (1,-1))))
print('part 2:', mem[pos])
