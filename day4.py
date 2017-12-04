import sys

def unique(phrase):
    return len(phrase) == len(set(phrase))

def anagram(phrase):
    return unique(list(map(lambda s: ''.join(sorted(s)), phrase)))

phrases = list(map(lambda l: l.split(), sys.stdin.readlines()))
print('part 1:', sum(map(unique, phrases)))
print('part 2:', sum(map(lambda p: unique(p) and anagram(p), phrases)))
