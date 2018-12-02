from aocd import data

def unique(phrase):
    return len(phrase) == len(set(phrase))

def anagram(phrase):
    return unique(list(map(lambda s: ''.join(sorted(s)), phrase)))

phrases = list(map(lambda l: l.split(), data.split('\n')))
print('part 1:', sum(map(unique, phrases)))
print('part 2:', sum(map(anagram, phrases)))
