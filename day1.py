#!/usr/bin/env python3
import sys

def solve(digits, n):
    sum = 0
    for i in range(len(digits)):
        if digits[i] == digits[(i+n)%len(digits)]:
            sum += digits[i]
    return sum

def golfed(digits, n):
    return sum(x for x, y in zip(digits, digits[n:]+digits[:n]) if x == y)


digits = list(map(int, sys.argv[1]))
print('part 1:', solve(digits, 1))
print('part 2:', solve(digits, len(digits)//2))

print('golfed')
print('part 1:', golfed(digits, 1))
print('part 2:', golfed(digits, len(digits)//2))
