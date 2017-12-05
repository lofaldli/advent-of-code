import re
from aocd import data

pairs = re.compile(r'(([a-z])\2+)')
def valid(pw):
    if sum(c in pw for c in 'iol') != 0:
        return False
    if len(set(pairs.findall(pw))) < 2:
        return False
    for i in range(len(pw)-2):
        a,b,c = pw[i:i+3]
        if ord(a) == ord(b) - 1 == ord(c) - 2:
            return True
    return False

def incr(pw):
    i = len(pw)-1
    while i >= 0:
        cur = pw[i]
        if cur == 'z':
            pw = pw[:i] + 'a' + pw[i+1:]
            i -= 1
        else:
            return pw[:i] + chr(ord(cur)+1) + pw[i+1:]
    return pw

def find_next(pw):
    while True:
        pw = incr(pw)
        if valid(pw):
            return pw

pw = find_next(data)
print('part 1:', pw)
print('part 2:', find_next(pw))
