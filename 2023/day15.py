import re
from collections import defaultdict

def HASH(step):
    current = 0
    for char in step:
        current = (current + ord(char)) * 17
    return current % 256

def HASHMAP(steps):
    pattern = re.compile(r"([a-z]+)([=-])([0-9]?)")
    boxes = defaultdict(dict)
    for step in steps:
        label, op, length = pattern.match(step).groups()
        box = boxes[HASH(label)]
        if op == "=":
            box[label] = int(length)
        else:
            box.pop(label, None)
        
    def power(boxes):
        for box, slots in boxes.items():
            for slot, length in enumerate(slots.values(), start=1):
                yield (box + 1) * slot * length
    return sum(power(boxes))

from aocd import data
steps = data.split(",")
print("part 1", sum(map(HASH, steps)))
print("part 2", HASHMAP(steps))
