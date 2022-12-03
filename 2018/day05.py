from aocd import data as word

def react(word):
    L = len(word)
    while True:
        for c in set(word.lower()):
            word = word.replace(c.upper() + c, '').replace(c + c.upper(), '')
        if L == len(word):
            break
        L = len(word)
    return word
    
print('part 1', len(react(word)))

short = len(word)
for c in set(word.lower()):
    w = word.replace(c, '').replace(c.upper(), '')
    short = min(short, len(react(w)))
print('part 2', short)
