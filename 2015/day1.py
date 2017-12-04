from aocd import data
from functools import reduce

brackets = data
print('part 1:', brackets.count('(') - brackets.count(')'))

floor = 0
for i in range(len(brackets)):
    floor += 1 if brackets[i] == '(' else -1 
    if floor < 0:
        break
print('part 2:', i+1)

