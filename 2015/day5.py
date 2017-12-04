import textwrap
from aocd import data

def nice_one(s):
    if sum(map(s.count, 'aeiou')) < 3:
        return False
    if sum(map(s.count, ('ab','cd','pq','xy'))) > 0:
        return False
    pairs = tuple(zip(s, s[1:]+s[:1]))[:-1]
    if sum(map(lambda p: p[0]==p[1], pairs)) == 0:
        return False
    return True

def nice_two(s):
    pairs = tuple(zip(s, s[2:]+s[:2]))[:-2]
    if sum(map(lambda p: p[0]==p[1], pairs)) == 0:
        return False

    for i in range(len(s)-2):
        if s[i:i+2] in s[i+2:]:
            return True

    return False

strings = data.split('\n')
print('part 1:', sum(map(nice_one, strings)))
print('part 2:', sum(map(nice_two, strings)))
