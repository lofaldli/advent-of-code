from aocd import data
lines = data.splitlines()

src = [(x, y) for x, y in map(lambda line: map(int, line.split(', ')), lines)]

min_x = min(x for x, y in src)
max_x = max(x for x, y in src)
min_y = min(y for x, y in src)
max_y = max(y for x, y in src)

def calc_areas(offset):
    grid = dict()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            closest = src[0]
            closest_distance = abs(closest[0] - x) + abs(closest[0] - y)
            for xx, yy in src:
                distance = abs(xx - x) + abs(yy - y)
                if distance < closest_distance:
                    closest = (xx, yy)
                    closest_distance = distance
                elif distance == closest_distance and closest != (xx, yy):
                    closest = None
            grid[(x, y)] = closest
    return grid

def safe_area():
    area = []
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            dists = []
            for xx, yy in src:
                dists.append(abs(xx - x) + abs(yy - y))
            if sum(dists) < 10000:
                area.append((xx,yy))
    return area
            
small_grid = calc_areas(0)
big_grid = calc_areas(1000)

biggest = 0
for s in src:
    small_area = sum(v == s for v in small_grid.values())
    big_area = sum(v == s for v in big_grid.values())
    if small_area != big_area:
        continue
    if small_area >= biggest:
        biggest = small_area
        
print('part 1', biggest)
print('part 2', len(safe_area()))
