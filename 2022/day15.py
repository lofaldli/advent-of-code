import collections

def manhattan(pos0, pos1):
    x0, y0 = pos0
    x1, y1 = pos1
    return abs(x0 - x1) + abs(y0 - y1)

def parse(data):
    for line in data.splitlines():
        line = line.replace('=', ' ').replace(',', '').replace(':', '')
        _,_,_, sx, _, sy, *_, bx, _, by = line.split()
        sensor = int(sx), int(sy)
        beacon = int(bx), int(by)
        yield sensor, beacon

def non_overlapping_ranges(distances, y):
    def merge(ranges):
        ranges = collections.deque(ranges)
        not_overlapping = []
        while ranges:
            if len(ranges) == 1:
                # there is only one range, and nothing to overlap with
                not_overlapping.append(ranges.popleft())
                break

            # we always check if the left-most range is overlapping with the next one
            a0, a1 = ranges.popleft()
            b0, b1 = ranges[0]
            if a0-1 <= b0 <= a1+1:
                # they are overlapping, so we update the now left-most range
                ranges[0] = (a0, max(a1, b1))
            else:
                # they are not overlapping, we therefore know that the leftmost range
                # is not overlapping with any other range
                not_overlapping.append((a0, a1))
                
        return not_overlapping

    # we want to find the range of coordinates in the current row
    # that can be seen from each sensor
    ranges = []
    for (x0, y0), distance in distances.items():
        dy = abs(y0 - y)

        if distance > dy:
            dx = distance - dy
            ranges.append((x0-dx, x0+dx))

    # some ranges can be seen some multiple sensors,
    # in that case we merge them
    return merge(sorted(ranges))
                
def part1(distances, y=2000000):
    # find out how many non-overlapping ranges are in this row
    ranges = non_overlapping_ranges(distances, y)
    # calculate the total length of each range
    return sum(x1 - x0 for x0, x1 in ranges)

def part2(distances, y_max=4000000):
    # with my puzzle input the correct y is around 3000000
    # so it's a bit faster to iterate over y in reverse (YMMV)
    for y in reversed(range(y_max+1)):
        ranges = non_overlapping_ranges(distances, y)

        # the beacon can only exist in one place, so it has to be the only row with
        # two non-overlapping ranges
        if len(ranges) == 2:
            # the x-value of the beacon is the end of the first range plus one
            x = ranges[0][1] + 1
            return x, y

if __name__ == '__main__':
    from aocd import data
    distances = dict(
        (sensor, manhattan(sensor, beacon))
        for sensor, beacon in parse(data)
    )

    print('part 1', part1(distances))
    x, y = part2(distances)
    print('part 2', x * 4000000 + y)
