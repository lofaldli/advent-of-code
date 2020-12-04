from aocd import data

def walk(pos, dir):
    x, y = pos
    return {
        'U': (x + 1, y),
        'D': (x - 1, y),
        'L': (x, y - 1),
        'R': (x, y + 1)
    }[dir]
    
def distance(pos):
    return abs(pos[0]) + abs(pos[1])

def trace(steps):
    path, pos = set(), (0, 0)
    step_count = dict()
    nsteps = 0
    for step in steps.split(','):
        for _ in range(int(step[1:])):
            nsteps += 1
            pos = walk(pos, step[0])
            if pos not in step_count:
                step_count[pos] = nsteps
            path.add(pos)
    return path, step_count
        
def part1(steps1, steps2):
    crossings = trace(steps1)[0].intersection(trace(steps2)[0])
    closest = 1000000000000000
    for crossing in crossings:
        if distance(crossing) < closest:
            closest = distance(crossing)    
    return closest
    
    
def part2(steps1, steps2):
    path1, step_count1 = trace(steps1)
    path2, step_count2 = trace(steps2)
    crossings = path1.intersection(path2)
    closest = 100000000000
    for crossing in crossings:
        dist = step_count1[crossing] + step_count2[crossing]
        if dist < closest:
            closest = dist
    return closest

    
steps1, steps2 = data.splitlines()

print('part 1:', part1(steps1, steps2))
print('part 2:', part2(steps1, steps2))