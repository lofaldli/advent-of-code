import re
from aocd import data
from collections import namedtuple

Tower = namedtuple('Tower', ['weight', 'children'])
def make_tree(lines):
    towers = dict()
    for line in lines:
        parts = line.split(' -> ')
        name, weight = parts[0].split()
        children = parts[1].split(', ') if len(parts) == 2 else []
        weight = weight.lstrip('(').rstrip(')')
        towers[name] = Tower(int(weight), children)
    return towers

def find_bottom(tree):
    trees = set(tree.keys())
    for _,c in tree.values():
        trees -= set(c)
    return list(trees)[0]

def odd_one_out(items):
    if items.count(max(items)) < items.count(min(items)):
        return items.index(max(items))
    else:
        return items.index(min(items))

def check_tree(name, tree): # very ugly
    t = tree[name]
    ws = list(check_tree(c, tree) for c in t.children)
    if len(set(ws)) > 1: # see if there are children with diffrent weights
        idx = odd_one_out(ws)    # the child on this index is different
        name = t.children[idx]   # it has this name
        weight = tree[name].weight # and this weight
        print(weight - (ws[idx] - ws[idx-1]))
    return t.weight + sum(ws)

tree = make_tree(data.split('\n'))
bottom = find_bottom(tree)
print('part 1:', bottom)
print('part 2:', 'should be the number on the next line')
check_tree(bottom, tree)
