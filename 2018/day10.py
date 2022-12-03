import re
from aocd import data

lines = data.splitlines()
  
def bounds(points):
  min_x = min(x for x,y in points)
  max_x = max(x for x,y in points)
  min_y = min(y for x,y in points)
  max_y = max(y for x,y in points)
  return min_x, max_x, min_y, max_y
  
def area(points):
  min_x, max_x, min_y, max_y = bounds(points)
  return abs(max_x-min_x) * abs(max_y-min_y)
  
def move(points, vels, t):
  for i, (x,y) in enumerate(points):
    vx, vy = vels[i]
    points[i] = (x+vx*t, y+vy*t)
  
def show(points):
  min_x, max_x, min_y, max_y = bounds(points)
  points = set(points)
  lines = []
  for y in range(min_y, max_y+1):
    line = []
    for x in range(min_x, max_x+1):
      if (x,y) in points:
        line.append('#')
      else:
        line.append(' ')
    lines.append(''.join(line))
  print('\n'.join(lines))

points = []
vels = []
for line in lines:
  x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
  points.append((x,y))
  vels.append((vx,vy))
  
move(points, vels, 10000)
min_t = 10000
min_area = area(points)
for t in range(1, 10000):
  move(points, vels, 1)
  if area(points) < min_area:
    min_area = area(points)
    min_t = t
    
move(points, vels, min_t-t)
print('part 1:')
show(points)
print('part 2', 10000+min_t)
