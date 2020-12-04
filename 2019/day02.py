from operator import add, mul
from itertools import product
from aocd import data 

def intcode(prog, noun=12, verb=2):
    prog[1], prog[2] = noun, verb
    ip, ops = 0, {1: add, 2: mul}
    while prog[ip] != 99:
        op, a, b, y = prog[ip:ip+4]
        prog[y] = ops[op](prog[a], prog[b])
        ip += 4
    return prog

prog = [int(x) for x in data.split(',')]

print('part 1:', intcode(prog[:])[0])

for noun, verb in product(range(0, 99), range(0, 99)):
    result = intcode(prog[:], noun, verb)
    if result[0] == 19690720:
        break

print('part 2:', 100 * result[1] + result[2])