import math

class Monkey:
    def __init__(self, items, op, mod, if_true, if_false):
        self.items = items
        self.op = op
        self.mod = mod
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def give(self, x):
        self.items.append(x)

    def take(self):
        return self.items.pop(0)

    def inspect(self):
        item = eval(self.op, None, {'old': self.take()})
        self.inspected += 1
        return item

    def test(self, x):
        return self.if_true if x % self.mod == 0 else self.if_false

def parse(data):
    for chunk in data.split('\n\n'):
        lines = chunk.splitlines()
        index = lines[0].split(' ')[1].strip(':')
        items = lines[1].split(': ')[1].split(', ')
        op = lines[2].split(' = ')[1]
        mod = lines[3].split()[-1]
        if_true = lines[4].split()[-1]
        if_false = lines[5].split()[-1]

        monkey = Monkey([int(i) for i in items], op, int(mod), int(if_true), int(if_false))
        yield int(index), monkey

def simulate(monkeys, rounds=20, divider=3):
    mod = math.prod(m.mod for m in monkeys.values())
    for round_ in range(rounds):
        for index, monkey in monkeys.items():
            while monkey.items:
                item = monkey.inspect()
                item = int(item // divider) % mod
                dest = monkey.test(item)
                monkeys[dest].give(item)

    most_inspected = sorted((monkey.inspected for monkey in monkeys.values()), reverse=True)
    return most_inspected[0] * most_inspected[1]

if __name__ == '__main__':
    from aocd import data
    monkeys = dict(parse(data))
    print('part 1', simulate(monkeys))
    monkeys = dict(parse(data))
    print('part 2', simulate(monkeys, 10000, 1))
