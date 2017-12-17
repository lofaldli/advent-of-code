from aocd import data

class Machine:
    def __init__(self, a=0, b=0):
        self.regs = {'a': a, 'b': b}
        self.i = 0

    def run(self, program):
        while 0 <= self.i < len(program):
            op, *args = program[self.i].split(' ')
            if op in ('jmp', 'jie', 'jio'):
                if (op == 'jie' and self.regs[args[0]] % 2 == 0 or
                    op == 'jio' and self.regs[args[0]] == 1):
                    self.i += int(args[1])
                    continue
                elif op == 'jmp':
                    self.i += int(args[0])
                    continue
            if op == 'hlf':
                self.regs[args[0]] = int(self.regs[args[0]] / 2)
            elif op == 'tpl':
                self.regs[args[0]] *= 3
            elif op == 'inc':
                self.regs[args[0]] += 1
            self.i += 1
        return self.regs['b']

program = data.replace(',', '').split('\n')
print('part 1:', Machine().run(program))
print('part 2:', Machine(a=1).run(program))
