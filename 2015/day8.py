import re
from aocd import data

def sanitize(s):
    s = re.sub(r'\\x[0-9a-fA-F]{2}', 'x', s)
    s = re.sub(r'\\.', 'x', s)
    return s[1:-1]

def escape(s):
    s = re.sub(r'\\', r'\\\\', s)
    s = re.sub(r'\"', r'\\"', s)
    return '"%s"' %(s)

lines = data.split('\n')
print('part 1:', sum(len(line) - len(sanitize(line)) for line in lines))
print('part 2:', sum(len(escape(line)) - len(line) for line in lines))
