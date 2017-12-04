import re 
from aocd import data

def look_and_say(s):
    groups = re.findall(r'(([1-9])\2*)', s)
    return ''.join('%d%d' % (len(s), int(c)) for s,c in groups)

s = data
for i in range(40):
    s = look_and_say(s)
print('part 1', len(s))

for i in range(10):
    s = look_and_say(s)
print('part 2', len(s))
