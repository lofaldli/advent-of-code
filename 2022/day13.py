import math
import itertools
import functools

def flatten(it):
    return itertools.chain.from_iterable(it)

def parse(data):
    for chunk in data.split('\n\n'):
        lines = chunk.splitlines()
        yield eval(lines[0]), eval(lines[1])

def compare_lists(left, right):
    """Compare two lists return -1 if left is smaller, 1 if right is smaller, 0 if equal"""
    for l, r in itertools.zip_longest(left, right):
        if l is None: 
            # left list is shorter = right order
            return -1
        if r is None: 
            # right list is shorter = wrong order
            return 1 

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                # left value is smaller = right order
                return -1
            if r < l:
                # right value is smaller = wrong order
                return 1

        else:
            if isinstance(l, int):
                # treat left value as list
                l = [l]
            if isinstance(r, int):
                # treat right value as list
                r = [r] 

            result = compare_lists(l, r)
            if result == 0:
                # the ordering cannot be determined, so we continue with the next elements
                continue
            else:
                # the ordering was determined, so we are done
                return result

    # the ordering could not be determined = left and right are equal
    return 0 

def part1(pairs):
    def right_order_indices(pairs):
        for index, (left, right) in enumerate(pairs, 1):
            if compare_lists(left, right) == -1:
                yield index
    return sum(right_order_indices(pairs))

def part2(packets):
    divider_packets = [ [[2]], [[6]] ]
    packets.extend(divider_packets)
    packets.sort(
        key=functools.cmp_to_key(compare_lists)
    )
    return math.prod(packets.index(p) + 1 for p in divider_packets)

if __name__ == '__main__':
    from aocd import data
    pairs = list(parse(data))
    print('part 1', part1(pairs))

    packets = list(flatten(pairs))
    print('part 2', part2(packets))
