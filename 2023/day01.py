def find_value(line):
    digits = [x for x in line if x.isdigit()]
    return int(digits[0] + digits[-1])

def find_value2(line):
    first = (len(line), digits[0])
    last = (0, digits[0])
    for symbol in symbols:
        index = line.find(symbol)
        if index == -1: continue
        value = symbol if symbol in digits else str(spelled.index(symbol) + 1)
        first = min(first, (index, value))
        last = max(last, (line.rfind(symbol), value))
    return int(first[1] + last[1])

from aocd import data
digits = "1 2 3 4 5 6 7 8 9 0".split()
spelled = "one two three four five six seven eight nine".split()
symbols = digits + spelled
part1 = part2 = 0
for line in data.splitlines():
    part1 += find_value(line)
    part2 += find_value2(line)
print("part 1", part1)
print("part 2", part2)
