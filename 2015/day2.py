from aocd import data

def wrapping(dim):
    l,w,h = dim
    a, b, c = l*w, w*h, h*l
    return 2*a + 2*b + 2*c + min(a, min(b, c))

def ribbon(dim):
    l,w,h = dim
    a, b, c = 2*l, 2*w, 2*h
    return a + b + c - max(a, max(b, c)) + l*w*h

lines = data.split('\n')
dims = [tuple(map(int, line.split('x'))) for line in lines]
print('part 1:', sum(map(wrapping, dims)))
print('part 2:', sum(map(ribbon, dims)))
