import time
import itertools

def parse(data):
    for line in data.splitlines():
        if line == 'noop':
            yield line, None
        else:
            instr, value = line.split()
            yield instr, int(value)

def run(program):
    cpi = {
        'noop': 1,
        'addx': 2,
    }
    register = 1
    ip = 0
    timer = 0

    for cycle in itertools.count(1):
        if timer == 0:
            instr, value = program[ip]
            timer = cpi[instr]

        yield cycle, register

        timer -= 1
        if timer == 0:
            if instr == 'noop':
                pass
            elif instr == 'addx':
                register += value
            ip += 1

        if ip == len(program):
            break

def draw(screen, width, height):
    lines = []
    for y in range(height):
        line = ''.join(
            screen.get((x,y), ' ') for x in range(width)
        )
        lines.append(line)
    return '\n'.join(lines)

def render(program, visualize=False):
    screen = {}
    width = 40
    sprite = '.'*width +  '###' + '.'*width
    for cycle, reg in run(program):
        pixel = (cycle - 1) % width
        row = int((cycle-1) // width)

        if abs(pixel - reg) < 2:
            screen[pixel, row] = '#'

        if visualize:
            print('\n'*10)
            print('cycle', cycle)
            print('X    ', reg)
            print(draw(screen, width, row+1))
            print(sprite[width-reg+1:][:width])
            time.sleep(0.1)
    
    print(draw(screen, width, row+1))


if __name__ == '__main__':
    from aocd import data
    program = list(parse(data))
    interesting = [20, 60, 100, 140, 180, 220]
    print('part 1', sum(cycle * reg for cycle, reg in run(program) if cycle in interesting))
    print('part 2:')
    render(program)
