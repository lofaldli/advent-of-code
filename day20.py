import re
from aocd import data
from collections import namedtuple, defaultdict

Particle = namedtuple('Particle', 'pos vel acc')

def parse(line):
    line = re.sub('[^0-9-,]', '', line)
    nums = tuple(map(int, line.split(',')))
    return Particle(tuple(nums[0:3]), tuple(nums[3:6]), tuple(nums[6:9]))

def dist(vec):
    return sum(map(abs, vec))

def min_dist(particles):
    min_pos, min_vel, min_acc = map(dist, particles[0])
    min_idx = 0
    for i in range(len(particles)):
        p = particles[i]
        if (dist(p.acc) < min_acc or
            dist(p.acc) == min_acc and dist(p.vel) < min_vel or
            dist(p.acc) == min_acc and dist(p.vel) == min_vel and dist(p.pos) < min_pos):
            min_pos, min_vel, min_acc = map(dist, p)
            min_idx = i
    return min_idx

def move(p):
    acc = p.acc
    vel = tuple(map(sum, zip(p.vel, acc)))
    pos = tuple(map(sum, zip(p.pos, vel)))
    return Particle(pos, vel, acc)

def simulate(particles, N=50): # not guaranteed to work, try more N's
    for _ in range(N): 
        particles = list(map(move, particles))
        collisions = defaultdict(list)
        for p in particles:
            collisions[p.pos].append(p)
        for collision in collisions.values():
            if len(collision) > 1:
                for collidee in collision:
                    particles.remove(collidee)
    return len(particles)


particles = list(map(parse, data.splitlines()))
print('part 1:', min_dist(particles))
print('part 2:', simulate(particles))