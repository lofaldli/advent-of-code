from operator import add, mul, eq, lt, ne
from aocd import data

FUN = {
  1: add, 2: mul,
  5: lambda x: ne(x, 0), 6: lambda x: eq(x, 0),
  7: lt, 8: eq
}

class Intcode:
    def __init__(self, prog):
        self.prog = list(map(int, prog.split(',')))
        self.ip = 0
        self.args = []
    
    @property
    def opcode(self):
        return self.prog[self.ip] % 100
        
    @property
    def modes(self):
        _modes = self.prog[self.ip] // 100
        return _modes % 10, (_modes // 10) % 10, (_modes // 100) % 10
        
    def write(self, addr, val):
        self.prog[addr] = val
    
    def arg(self, n=0):
        addr = self.ip + n + 1
        val = self.prog[addr]    
        if self.modes[n] == 0:
            val = self.prog[val]
        return val
        
    def step(self):
        steps = {
            1: 4, 2: 4, 3: 2, 4: 2,
            5: 3, 6: 3, 7: 4, 8: 4
        }
        try:
            self.ip += steps[self.opcode]
        except KeyError:
            raise RuntimeError(f'Invalid opcode {self.opcode}')
        
    def jump(self, addr):
        self.ip = addr
        
    def run(self):
        while self.opcode != 99:
            if self.opcode in (1, 2, 7, 8):
                addr = self.prog[self.ip + 3]
                op = FUN[self.opcode]
                res = int(op(self.arg(0), self.arg(1)))
                self.write(addr, res)
            elif self.opcode in (5, 6):
                op = FUN[self.opcode]
                if op(self.arg()):
                    self.jump(self.arg(1))
                    continue
            elif self.opcode in (3, 4):
                if self.opcode == 3:
                    addr = self.prog[self.ip + 1]
                    self.write(addr, int(input('> ')))
                else:
                    print('OUT:', self.arg())
            else:
                raise RuntimeError(f'Invalid opcode {self.opcode}')
            self.step()

program = data 

print('Welcome to INTCODE')
print('  1: Test program')
print('  5: Thermal radiator controller')
Intcode(program).run()