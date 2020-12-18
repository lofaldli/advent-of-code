from collections import defaultdict
from math import prod
from aocd import data

def parse_rule(line):
    name, rest = line.split(': ')
    ranges = rest.split(' or ')
    rule = set()
    for r in ranges:
        a, b = map(int, r.split('-'))
        rule |= set(range(a,b+1))
    return name, rule

def parse_ticket(line):
    return [int(x) for x in line.split(',')]

def value_invalid(value, rules):
    return all(value not in rule for rule in rules.values())

def ticket_invalid(ticket, rules):
    return any(value_invalid(value, rules) for value in ticket)

def part1(tickets, rules):
    total = 0
    for ticket in nearby_tickets:
        total += sum(value for value in ticket if value_invalid(value, rules))
    return total  

def part2(nearby_tickets, your_ticket, rules):
    fields = [set(rules.keys()) for _ in your_ticket]
    valid_tickets = [t for t in nearby_tickets if not ticket_invalid(t, rules)]
    
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            for key, rule in rules.items():
                if value not in rule:
                    fields[i].remove(key)

    while any(isinstance(field, set) for field in fields):
        for i, f in enumerate(fields):
            if len(f) == 1:
                fields[i] = f.pop()

        for index, field in enumerate(fields):
            if isinstance(field, str):
                other_fields = fields[:index] + fields[index+1:]
                for other in other_fields:
                    if field in other:
                        other.remove(field)

    return prod(your_ticket[index] for index, key in enumerate(fields) if key.startswith('departure '))
     
lines = iter(data.splitlines())

rules = dict()
for line in lines:
    if line == '':
        break
    name, rule = parse_rule(line)
    rules[name] = rule

next(lines) # your ticket:
your_ticket = parse_ticket(next(lines))
next(lines) # <empty line>

next(lines) # nearby tickets:
nearby_tickets = [parse_ticket(line) for line in lines]
print('part 1', part1(nearby_tickets, rules))
print('part 2', part2(nearby_tickets, your_ticket, rules))
