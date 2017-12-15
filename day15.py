from aocd import data

class Gen:
    def __init__(self, factor, start, crit=1):
        self.f, self.p, self.c = factor, start, crit

    def next(self):
        while True:
            self.p = (self.p * self.f) % 2147483647
            if self.p % self.c == 0:
                return self.p

def check(a,b):
    return a & 0xffff == b & 0xffff

a, b = (int(line.split()[-1]) for line in data.split('\n'))

A, B = Gen(16807, a), Gen(48271, b)
print('part 1:', sum(check(A.next(), B.next()) for _ in range(40000000)))
A, B = Gen(16807, a, 4), Gen(48271, b, 8)
print('part 2:', sum(check(A.next(), B.next()) for _ in range(5000000)))
