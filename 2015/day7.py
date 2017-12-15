from aocd import data

def parse_lines(lines):
    wires = dict()
    for line in lines:
        src, tgt = line.split(' -> ')
        try:
            wires[tgt] = int(src)
        except:
            wires[tgt] = src
    return wires

OPS = {
    'NOT': lambda x: ~x if ~x >= 0 else 65536 + ~x,
    'OR': lambda x, y: x | y,
    'AND': lambda x, y: x & y,
    'LSHIFT': lambda x, y: (x << y) % 65536,
    'RSHIFT': lambda x, y: max(x >> y, 0)
}

def get(val): 
    try:
        return int(val) # if its just an integer
    except:
        return wires[val] # if it's the name of a wire

def evaluate(key):
    expr = get(key)
    if isinstance(expr, int):
        return expr

    expr = expr.split(' ')
    if len(expr) == 1:
        res = evaluate(expr[0])
    elif len(expr) == 2:
        res = OPS['NOT'](evaluate(expr[1]))
    elif len(expr) == 3:
        l, op, r = expr
        res = OPS[op](evaluate(l), evaluate(r))
    wires[key] = res
    return res

wires = parse_lines(data.split('\n'))
a = evaluate('a')
print('part 1:', a)
wires = parse_lines(data.split('\n'))
wires['b'] = a
print('part 2:', evaluate('a'))
