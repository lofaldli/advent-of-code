def parse(data):
    numbers = {}
    symbols = {}
    number = ""
    cells = []
    for y, line in enumerate(data.splitlines()):
        for x, value in enumerate(line):
            if value.isdigit():
                number += value
                cells.append((x,y))
            else:
                if number != "":
                    numbers[tuple(cells)] = int(number)
                    number = ""
                    cells = []
                if value != ".":
                    symbols[(x,y)] = value
        if number != "":
            numbers[tuple(cells)] = int(number)
            number = ""
            cells = []
    return numbers, symbols

def adjacent(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

def part_numbers(numbers, symbols):
    for cells, number in numbers.items():
        for cell in cells:
            if any(adjacent(cell, symbol) for symbol in symbols):
                yield number
                break

def gear_ratios(numbers, symbols):
    for symbol_pos, symbol in symbols.items():
        if symbol != "*":
            continue
        adjacent_numbers = []
        for cells, number in numbers.items():
            if any(adjacent(cell, symbol_pos) for cell in cells):
                adjacent_numbers.append(number)
        if len(adjacent_numbers) == 2:
            yield adjacent_numbers[0] * adjacent_numbers[1]

from aocd import data
numbers, symbols = parse(data)
print("part 1", sum(part_numbers(numbers, symbols)))
print("part 2", sum(gear_ratios(numbers, symbols)))
