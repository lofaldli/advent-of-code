import re, json
from aocd import data

def count(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, dict):
        return 0 if 'red' in obj.values() else sum(map(count, obj.values()))
    if isinstance(obj, list):
        return sum(map(count, obj))
    return 0

print('part 1:', sum(map(int, re.findall(r'-?[0-9]+', data))))
print('part 2:', count(json.loads(data)))


