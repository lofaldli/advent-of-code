from aocd import data
from collections import deque

def play(M, N):
    players = [0 for _ in range(N)]
    marbles = deque([0])
    for marble in range(1, M+1):
        if marble % 23 != 0:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            players[(marble-1) % N] += marble + marbles.pop()
            marbles.rotate(-1)
    return max(players)

N, *_, M, _ = data.split()
M, N = int(M), int(N)
 
print('part 1', play(M, N))
print('part 2', play(M*100, N))
