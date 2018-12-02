import re
from aocd import data

data = re.sub('!.', '', data)
garbage = re.compile('<.*?>')
level = total = 0
for c in garbage.sub('', data):
    if c == '{':
        level += 1
    elif c == '}':
        total += level
        level -= 1

print('part 1:', total)
print('part 2:', sum(len(x)-2 for x in garbage.findall(data)))
