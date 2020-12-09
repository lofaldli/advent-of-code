from aocd import data
from itertools import combinations, product

def find_secret(numbers, N):
    for i, n in enumerate(numbers[N:]):
        if n not in map(sum, combinations(numbers[i:i+N], 2)):
            return n

def find_weakness(numbers, secret):
    total = head = tail = 0
    while total != secret:
        while total < secret:
            total += numbers[tail]
            tail += 1
        while total > secret:
            total -= numbers[head]
            head += 1
    weak_list = numbers[head:tail]
    return min(weak_list) + max(weak_list)
    
numbers = list(map(int, data.splitlines()))
secret = find_secret(numbers, 25)
print('part 1', secret)
print('part 2', find_weakness(numbers, secret))
