class Box:
    """A box for putting a number in"""
    def __init__(self, number):
        self.number = number

def mix(encrypted, original):
    # iterate boxes in the original order
    for box in original:

        # constantly searching for a box with a number may not be that efficient,
        # but at least it's easier than keeping track of the index of each box
        index = encrypted.index(box)

        # to avoid tricky index arithmetic, we move the current box to the front
        encrypted = encrypted[index:] + encrypted[:index]

        # remove the current box from the front
        current = encrypted.pop(0)

        # calculate the new index of the current box mod the length of the list
        # (after removing the element)
        new_index = box.number % len(encrypted)

        # insert the box at the new position
        encrypted.insert(new_index, current)

    return encrypted

def decrypt(numbers, N=1):
    # for the solution we need to keep track of the position of value 0
    zero_index = numbers.index(0)

    # put each number in a box, this way we can search for them by reference
    # with list.index() in case there are two numbers with the same value
    boxes = tuple(Box(number) for number in numbers)

    # keep track of the box containing the value 0
    zero = boxes[zero_index]

    # make a list of numbers in boxes so that we can mix them
    encrypted = list(boxes)
    for _ in range(N):
        encrypted = mix(encrypted, boxes)

    # find the final index of the box containing the value 0 and compute the answer
    zero_index = encrypted.index(zero)
    for offset in (1000, 2000, 3000):
        index = (zero_index + offset) % len(encrypted)
        yield encrypted[index].number

if __name__ == '__main__':
    from aocd import data
    numbers = tuple(int(x) for x in data.splitlines())

    print('part 1', sum(decrypt(numbers)))

    K = 811589153
    numbers = tuple(n * K for n in numbers)
    print('part 2', sum(decrypt(numbers, N=10)))
