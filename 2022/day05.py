from time import sleep
from aocd import data

def parse_stacks(lines):
    stacks = {int(n): [] for n in lines[-1].split()}
    for line in reversed(lines[:-1]):
        for i, c  in enumerate(line):
            if c in ' []':
                continue
            index = 1 + int((i-1)//4)
            stacks[index].append(c)
    return stacks

def parse_steps(lines):
    steps = []
    for line in lines:
        _, n, _, src, _, dst = line.split()
        n, src, dst = map(int, [n, src, dst])
        steps.append((n, src, dst))
    return steps

def execute9000(steps, stacks):
    for n, src, dst in steps:
        for _ in range(n):
            stacks[dst].append(stacks[src].pop())
            print(dump(stacks))
            sleep(0.01)

def execute9001(steps, stacks):
    for n, src, dst in steps:
        stacks[dst].extend(stacks[src][-n:])
        stacks[src] = stacks[src][:-n]
        print(dump(stacks))
        sleep(0.01)

def top_crates(stacks):
    return ''.join(s[-1] for s in stacks.values())

def dump(stacks):
    lines = [' '.join(f' {s} ' for s in stacks.keys())]
    max_height = sum(len(stack) for stack in stacks.values()) 

    for i in range(max_height):
        chunks = []
        for stack in stacks.values():
            if i < len(stack):
                chunks.append(f'[{stack[i]}]')
            else:
                chunks.append('   ')
        lines.append(' '.join(chunks))
    return '\n'.join(reversed(lines))

stackinput, stepinput = data.split('\n\n')
steps = parse_steps(stepinput.splitlines())

stacks = parse_stacks(stackinput.splitlines())
execute9000(steps, stacks)
print('part 1', top_crates(stacks))
sleep(3)

stacks = parse_stacks(stackinput.splitlines())
execute9001(steps, stacks)
print('part 2', top_crates(stacks))
