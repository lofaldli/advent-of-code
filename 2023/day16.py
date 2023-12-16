import functools

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

reflections = {
    "/": {
        up: right,
        right: up,
        left: down,
        down: left,
    },
    "\\": {
        up: left,
        left: up,
        right: down,
        down: right,
    }
}

def parse(lines):
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            yield (x, y), value

@functools.cache
def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def trace(beam, mirrors):
    energized = set()
    beams = [beam]
    while beams:
        # take out an active beam
        position, direction = beams.pop()
        # record the beam energizing the current tile
        energized.add((position, direction))
        mirror = mirrors[position]
        if mirror == ".":
            # there are more empty tiles than mirrors, 
            # so we save a bit of time by checking it first
            # even if there is no action to be taken
            pass
        elif mirror in "/\\":
            # change the direction based on the mirror
            reflection = reflections[mirror]
            direction = reflection[direction]
        elif mirror == "|" and direction in (left, right):
            # change the direction and add a new beam in the opposite direction
            direction = up
            beams.append((position, down))
        elif mirror == "-" and direction in (up, down):
            # change the direction and add a new beam in the opposite direction
            direction = left
            beams.append((position, right))
        # move the beam one step in the current direction
        position = move(position, direction)
        if position in mirrors and (position, direction) not in energized:
            # if the beam is still within the map and
            # there is not already a beam with the same direction
            # energizing the current tile
            # add the beam back to the list
            beams.append((position, direction))
    # because multiple beams can energize the same tile, each tile is only considered once
    return set(position for position, directions in energized)

def all_beams(width, height):
    for x in range(width):
        yield ((x, 0), down)
        yield ((x, height - 1), up)
    for y in range(height):
        yield ((0, y), right)
        yield ((width - 1, y), left)

from aocd import data
lines = data.splitlines()
mirrors = dict(parse(lines))
height = len(lines)
width = len(lines[0])
beam = ((0, 0), right)
print("part 1", len(trace(beam, mirrors)))
print("part 2", max(len(trace(beam, mirrors)) for beam in all_beams(width, height)))
