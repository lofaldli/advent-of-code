from aocd import data

def spin(steps, n):
    buf, cur = [0], 0
    for i in range(1, n+1):
        cur = (cur + steps) % i + 1
        buf.insert(cur, i)
    return buf

def spin_zero(steps, n): # what if i told you there is no list
    cur = after_zero = 0
    for i in range(1, n+1):
        cur = (cur + steps) % i + 1
        if cur == 1:       # zero will always be first
            after_zero = i # just remember what comes after 
    return after_zero

steps = int(data)
buf = spin(steps, 2017)
print('part 1:', buf[buf.index(2017)+1])
print('part 2:', spin_zero(steps, 50000000))
