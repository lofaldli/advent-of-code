from collections import Counter
from functools import lru_cache
from aocd import data

@lru_cache
def count_memo(current, adapters):
    if len(adapters) == 0:
        return 1
    value = 0
    for i in range(min(3, len(adapters))):
        if current + 3 >= adapters[i]:
            value += count_memo(adapters[i], adapters[i+1:])
    return value

def count_smart(jumps):
    streak_counts = Counter()
    streak = 0
    for j in jumps:
        if j == 1: 
            streak += 1
        elif j == 3:
            streak_counts[streak] += 1
            streak = 0
    return 2**streak_counts[2] * 4**streak_counts[3] * 7**streak_counts[4]

adapters = sorted(map(int, data.splitlines()))
device = adapters[-1] + 3
jumps = [b-a for a, b in zip([0] + adapters, adapters + [device])]
jump_count = Counter(jumps)
print('part 1', jump_count[1] * jump_count[3])
print('part 2 (memo)', count_memo(0, tuple(adapters + [device])))
print('part 2 (smart)', count_smart(jumps))
