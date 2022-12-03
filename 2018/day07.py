from collections import defaultdict
from itertools import chain

from aocd import data

def flatten(it):
    return chain.from_iterable(it)

def parse(rows):
    avail = [] # keep track of currently available steps
    steps = defaultdict(list) # a dictionary for keeping track of prerequisite steps

    for _, s1, *_, s2, _, _, in rows:
        steps[s2].append(s1) # add s1 as a dependency to s2

    # all steps without dependencies are available
    avail.extend(set(flatten([v for v in steps.values()])) - set(steps.keys()))
    return steps, avail
    

def do_work(step, steps, avail):
    for k, v in steps.items():
        if step in v:
            v.remove(step) # remove step from dependencies
        if len(v) == 0:
            avail.append(k) # step is available when it has no dependencies
    for s in avail:
        steps.pop(s, None) # remove available steps from dictionary of dependencies

def part1(rows):
    # find the order the steps with sequential execution
    done = ''
    steps, avail = parse(rows)
    for _ in range(10000):
        avail.sort()
        step = avail.pop(0)
        done += step
        if len(steps) == 0:
            break
        do_work(step, steps, avail)
    return done
    
class Worker:
    def __init__(self, task):
        self.task = task
        self.time = ord(task) - ord('A') + 1 + 60
    def work(self):
        self.time -= 1
    

def part2(rows):
    # number of cycles required to complete all steps with 5 parallel workers
    done = ''
    steps, avail = parse(rows)
    workers = []
    for i in range(1000):
        avail.sort()
        while len(workers) < 5 and len(avail) > 0:
            step = avail.pop(0)
            workers.append(Worker(step))
        for w in workers:
            w.work()
            if w.time < 1:
                do_work(w.task, steps, avail)
                done += w.task
        workers = [w for w in workers if w.time > 0]
        if len(avail) == 0 and len(steps) == 0 and len(workers) == 0:
            break
    return i + 1

rows = [line.split() for line in data.splitlines()]
print('part 1', part1(rows))
print('part 2', part2(rows))
