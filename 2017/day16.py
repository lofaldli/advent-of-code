from aocd import data

def swap(items, a, b):
    items[a], items[b] = items[b], items[a]

def dance(moves, reps=1):
    progs = list(x for x in 'abcdefghijklmnop')
    seen = []
    for i in range(reps+1):
        s = ''.join(progs)
        if s in seen:
            return seen[reps % i]
        seen.append(s)

        for move in moves:
            fun = move[0]
            if fun == 's':
                x = int(move[1:])
                progs = progs[-x:] + progs[:-x]
            elif fun == 'x':
                a, b = map(int, move[1:].split('/'))
                swap(progs, a, b)
            else:
                a, b = move[1:].split('/')
                swap(progs, progs.index(a), progs.index(b))
    return s
    
moves = data.split(',')
print('part 1:', dance(moves))
print('part 2:', dance(moves, 1000000000))
