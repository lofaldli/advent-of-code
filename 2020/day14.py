from aocd import data

def exec1(mem, addr, mask, val):
    val_binary = format(val, '036b')
    bits = ''.join(m if m != 'X' else v for m, v in zip(mask, val_binary))
    mem[addr] = int(bits, 2)

def exec2(mem, addr, mask, val):
    addr_binary = format(addr, '036b')
    bits = [a if m == '0' else m for m, a in zip(mask, addr_binary)]

    binary_addrs = []
    for b in bits:
        if b != 'X':
            if len(binary_addrs) == 0:
                binary_addrs.append([b])
            else:
                for ba in binary_addrs:
                    ba.append(b)
        else:
            if len(binary_addrs) == 0:
                binary_addrs.append(['0'])
                binary_addrs.append(['1'])
            else:
                binary_addrs.extend([ba[:] for ba in binary_addrs])
                N = len(binary_addrs)//2
                new = '0' * N + '1' * N
                for ba, n in zip(binary_addrs, new):
                    ba.append(n)

    addrs = [int(''.join(ba), 2) for ba in binary_addrs]
    for a in addrs:
        mem[a] = val

def run(program, exec):
    mask = 'X' * 36
    mem = dict()
    for op, val in program:
        if op == 'mask':
            mask = val
        else:
            addr = int(op[4:-1])
            exec(mem, addr, mask, int(val))
    return sum(mem.values())

program = [line.split(' = ') for line in data.splitlines()]
print('part 1', run(program, exec1))
print('part 2', run(program, exec2))
