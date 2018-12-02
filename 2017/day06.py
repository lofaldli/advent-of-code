from aocd import data

def redist(banks):
    dist = max(banks)
    i = banks.index(dist)
    banks[i] = 0
    while dist > 0:
        i = (i+1)%len(banks)
        banks[i] += 1
        dist -= 1

def loop(banks):
    configs = []
    while tuple(banks) not in configs:
        configs.append(tuple(banks))
        redist(banks)
    return len(configs)

banks = list(map(int, data.split()))
print('part 1:', loop(banks))
print('part 2:', loop(banks))
