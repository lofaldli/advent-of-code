from aocd import data

NEWS = {'N':1j, 'E':1, 'W':-1, 'S':-1j}

def solve(moves, start=1, use_waypoint=False):
    position = 0 + 0j
    bearing = start
    for direction, units in moves:
        if direction == 'F':
            position += bearing * units
        elif direction == 'L':
            bearing *= 1j**(units / 90)
        elif direction == 'R':
            bearing *= 1j**(-units / 90)
        else:
            if use_waypoint:
                bearing += NEWS[direction] * units
            else:
                position += NEWS[direction] * units

    return round(abs(position.real) + abs(position.imag))

moves = [(line[0], int(line[1:])) for line in data.splitlines()]
print('part 1', solve(moves))
print('part 2', solve(moves, 10 + 1j, True))
