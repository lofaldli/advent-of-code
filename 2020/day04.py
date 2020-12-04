import re
from aocd import data

def check1(line):
    keys = 'byr iyr eyr hgt hcl ecl pid'
    return all(k in line for k in keys.split())

def check2(line):
    def check_hgt(x):
        if x.endswith('cm'):
            return 150 <= int(x[:-2]) <= 193
        if x.endswith('in'):
            return 59 <= int(x[:-2]) <= 76
        return False

    rules = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': check_hgt,
        'hcl': lambda x: re.fullmatch(r'#[a-f0-9]{6}', x) is not None,
        'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
        'pid': lambda x: re.fullmatch(r'[0-9]{9}', x) is not None,
        'cid': lambda x: True
    }

    entries = [x.split(':') for x in line.split()]
    return all(rules[k](v) for k, v in entries)

lines = [e.replace('\n', ' ') for e in data.split('\n\n')]
 
print('part 1', sum(map(check1, lines)))
print('part 2', sum(map(check2, filter(check1, lines))))
