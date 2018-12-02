from aocd import data

def solve(digits, n):
    return sum(x for x, y in zip(digits, digits[n:]+digits[:n]) if x == y)

digits = list(map(int, data))
print('part 1:', solve(digits, 1))
print('part 2:', solve(digits, len(digits)//2))
