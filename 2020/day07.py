import re
from aocd import data

def parse(line):
    outer, inner = line.split(' bags contain ')
    contents = {c: int(n) for n, c in re.findall('(\d+) (\w+ \w+)', inner)}
    return outer, contents

def search_out(tree, target):
    outer = set([target])
    for k, v in tree.items():
        if target in v:
            outer.update(search_out(tree, k))
    return outer

def search_in(tree, target):
    return sum(v + v * search_in(tree, k) for k, v in tree[target].items())

target = 'shiny gold'
tree = dict(map(parse, data.splitlines()))
print('part 1', len(search_out(tree, target))-1)
print('part 2', search_in(tree, target))
