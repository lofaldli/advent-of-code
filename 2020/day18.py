from operator import add, mul
from aocd import data

def atom(token):
    return {'+': add, '*': mul}.get(token) or int(token)

def read_from_tokens(tokens):
    # borrowed from http://www.norvig.com/lispy.html
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop )
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def read(line):
    line = '(' + line + ')'
    tokens = line.replace('(', ' ( ').replace(')', ' ) ').split()
    return read_from_tokens(tokens)

def eval1(expr):
    if isinstance(expr, list):
        left = eval1(expr.pop(0))
        while len(expr) > 0:
            op = eval1(expr.pop(0))
            right = eval1(expr.pop(0))
            left = op(left, right)
        return left
    else:
        return expr

def factor(expr):
    left = eval2(expr.pop(0))
    while len(expr) > 0 and expr[0] == add:
        expr.pop(0) # pop +
        right = eval2(expr.pop(0))
        left = add(left, right)
    return left

def eval2(expr):
    if isinstance(expr, list):
        left = factor(expr)
        while len(expr) > 0 and expr[0] == mul:
            expr.pop(0) # pop *
            right = factor(expr)
            left = mul(left, right)
        return left
    else:
        return expr

lines = data.splitlines()
print('part 1', sum(eval1(read(line)) for line in lines))
print('part 2', sum(eval2(read(line)) for line in lines))
