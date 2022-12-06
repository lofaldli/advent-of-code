from aocd import data

def find_marker(line, N=4):
    for i in range(N, len(line)):
        if len(set(line[i-N:i])) == N:
            return i
    return -1

print('part 1', find_marker(data))
print('part 2', find_marker(data, 14))
