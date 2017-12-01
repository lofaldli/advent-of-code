import sys

def solve(digits, n):
    sum = 0
    for i in range(len(digits)):
        if digits[i] == digits[(i+n)%len(digits)]:
            sum += digits[i]
    return sum

digits = list(map(int, sys.argv[1]))
print('part 1:', solve(digits, 1))
print('part 2:', solve(digits, len(digits)//2))
