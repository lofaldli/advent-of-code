from aocd import data

def walk(pos, dir):
	return pos[0]+dir[0],pos[1]+dir[1]

def turn_left(dir):
	return dir[1], -dir[0]

grid = tuple(data.splitlines())
pos = (0, grid[0].index('|'))
dir = (1,0)
word = ''
steps = 0
while True:
	r,c = pos
	if grid[r][c].isalpha():
		word += grid[r][c]
	elif grid[r][c] == '+':
		r,c = walk(pos, turn_left(dir))
		if 0<=r<len(grid) and 0<=c<len(grid[r]) and grid[r][c] != ' ':
			dir = turn_left(dir)
		else:
			dir = turn_left(turn_left(turn_left(dir))) # why not
	elif grid[r][c] == ' ':
		break
	pos = walk(pos, dir)
	steps += 1

print('part 1:', word)
print('part 2:', steps)