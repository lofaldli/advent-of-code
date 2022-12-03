from aocd import data

SERIAL_NO = int(data)
MEMO = dict()

def power_level(x, y):
    if (x,y) in MEMO.keys():
        return MEMO[(x,y)]
    rack_id = x + 10
    level = rack_id * y
    level += SERIAL_NO
    level *= rack_id
    level = int(format(level, '03d')[-3])
    level -= 5
    MEMO[(x,y)] = level
    return level
    
def search(x, y, size):
    power = 0
    for yy in range(size):
        for xx in range(size):
            power += power_level(x+xx, y+yy)
    return power
    
max_power = -100000000000000
max_pos = (1,1)
for y in range(1,299):
    for x in range(1, 299):
        power = search(x,y,3)
        if power > max_power:
            max_power = power
            max_pos = (x,y)
print('part 1', max_pos)

print("part 2 (press ctrl-c when output doesn't change anymore")

max_power = -100000000000000
max_pos = (1,1,1)
for size in range(1, 301):
  for y in range(1,299):
    for x in range(1, 299):
      power = search(x,y,min(size, min(300-x, 300-y)))
      if power > max_power:
        max_power = power
        max_pos = (x, y, size)
  print(max_pos, max_power)
