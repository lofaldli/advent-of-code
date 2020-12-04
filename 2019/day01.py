from aocd import data
  
def f(x):
  return x // 3 - 2
  
def f2(x):
  x = f(x)
  return x + f2(x) if x > 0 else 0

lines = data.splitlines()  
print('part 1:', sum(map(f, map(int, lines))))
print('part 2:', sum(map(f2, map(int, lines))))