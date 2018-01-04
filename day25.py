from collections import defaultdict

rules = {
    'A': ((1, 1, 'B'), (0,-1, 'F')),
    'B': ((0, 1, 'C'), (0, 1, 'D')),
    'C': ((1,-1, 'D'), (1, 1, 'E')),
    'D': ((0,-1, 'E'), (0,-1, 'D')),
    'E': ((0, 1, 'A'), (1, 1, 'C')),
    'F': ((1,-1, 'A'), (1, 1, 'A'))
}

state = 'A'
slot = 0
tape = defaultdict(int)
for step in range(12794428):
    val, dir, next = rules[state][tape[slot]]
    tape[slot] = val
    slot += dir
    state = next

print('part 1:', sum(tape.values()))
print('part 2: *')