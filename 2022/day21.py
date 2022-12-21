import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def parse(data):
    for line in data.splitlines():
        name, expr = line.split(': ')
        try:
            yield name, int(expr)
        except ValueError:
            yield name, expr.split()

def evaluate(name, exprs):
    """Post-order evaluation"""
    expr = exprs[name]
    if isinstance(expr, int):
        return expr
    else:
        left, op, right = expr
        left = evaluate(left, exprs)
        right = evaluate(right, exprs)
        return OPS[op](left, right)

def evaluate_partial(name, exprs, unknown='humn'):
    """Partial post-order evaluation leaving unknown values as-is"""
    expr = exprs[name]
    if isinstance(expr, int):
        return expr
    else:
        left, op, right = expr
        if left != unknown:
            left = evaluate_partial(left, exprs, unknown)
        if right != unknown:
            right = evaluate_partial(right, exprs, unknown)

        if isinstance(left, str) or isinstance(right, str):
            exprs[name] = left, op, right
            return name
        
        result = OPS[op](left, right)
        exprs[name] = result
        return result

def find_dependants(exprs):
    """Create an inverse mapping of values that depend on each other"""
    for name, expr in exprs.items():
        if isinstance(expr, int):
            continue
        left, op, right = expr
        if isinstance(left, str):
            yield left, name
        if isinstance(right, str):
            yield right, name

def inverse_left(name, op, right):
    """Invert a binary expression, solving for the left value"""
    if op == '+':
        # A = B + C becomes B = A - C
        return (name, '-', right)
    elif op == '-':
        # A = B - C becomes B = A + C
        return (name, '+', right)
    elif op == '*':
        # A = B * C becomes B = A / C
        return (name, '/', right)
    elif op == '/':
        # A = B / C becomes B = A * C
        return (name, '*', right)

def inverse_right(name, op, left):
    """Invert a binary expression, solving for the right value"""
    if op == '+':
        # A = B + C becomes C = A - B
        return (name, '-', left)
    elif op == '-':
        # A = B - C becomes C = B - A
        return (left, '-', name)
    elif op == '*':
        # A = B * C becomes C = A / B
        return (name, '/', left)
    elif op == '/':
        # A = B / C becomes C = B / A
        return (left, '/', name)


def solve_for(name, exprs, dependants):
    """Solve a set of expressions for `name`"""

    # first we find out which expression depends in this value
    dependant = dependants[name]
    left, op, right = exprs[dependant]

    # if the we have reached root, we return the known value
    if dependant == 'root':
        return right if left == name else left

    # recursively determine the depependant value
    dependant = solve_for(dependant, exprs, dependants)

    # inverse the expression to solve for left or right
    if left == name:
        expr = inverse_left(dependant, op, right)
    else:
        expr = inverse_right(dependant, op, left)

    # evaluate the inversed expression
    left, op, right = expr
    return OPS[op](left, right)
    

if __name__ == '__main__':
    from aocd import data
    exprs = dict(parse(data))
    print('part 1', evaluate('root', dict(exprs)))

    # evaluate all expressions without unknown values
    evaluate_partial('root', exprs, 'humn')
    # find which values depend on which
    dependants = dict(find_dependants(exprs))
    # solve for 'humn' with the knowledge that both values in the root expression are equal
    print('part 2', solve_for('humn', exprs, dependants))
