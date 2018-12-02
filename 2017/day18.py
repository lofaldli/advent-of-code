from aocd import data
from queue import Queue, Empty
from collections import defaultdict

class Worker:
    def __init__(self, program, qout, qin=None, id=0):
        self.program = program
        self.ip = 0
        self.regs = defaultdict(int)
        self.regs['p'] = id
        self.qin = qin
        self.qout = qout
        self.sent = 0
        
    def get(self, x):
        try:
            return int(x)
        except ValueError:
            return self.regs[x]
        
    def run(self):
        self.waiting = False
        while 0 <= self.ip < len(self.program):
            p = self.program[self.ip]
            if len(p) == 3:
                op, x, y = p
                y = self.get(y)
                if op == 'jgz' and self.get(x) > 0:
                    self.ip += y
                    continue
                elif op == 'set':
                    self.regs[x] = y
                elif op == 'add':
                    self.regs[x] += y
                elif op == 'mul':
                    self.regs[x] *= y
                elif op == 'mod':
                    self.regs[x] %= y
            elif len(p) == 2:
                op, x = p
                if op == 'snd':
                    self.qout.put(self.get(x))
                    self.sent += 1
                elif op == 'rcv':
                    if self.qin:
                        try:
                            self.regs[x] = self.qin.get_nowait()
                        except Empty:
                            return
                    else:
                        if self.get(x) != 0:
                            x = 0
                            while not self.qout.empty():
                                x = self.qout.get()
                            return x 
            self.ip += 1
        return True

program = tuple(line.split(' ') for line in data.splitlines())
print('part 1:', Worker(program, Queue()).run())

q_who = Queue()
deja_q = Queue()
w0 = Worker(program, q_who, deja_q, 0)
w1 = Worker(program, deja_q, q_who, 1)

while True:
    if w0.run(): break
    if w1.run(): break
    if w0.qin.empty() and w1.qin.empty():
        break
print('part 2:', w1.sent)
