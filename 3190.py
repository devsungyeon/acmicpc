import sys
import collections
collections.deque

n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]
print(board)
k = int(sys.stdin.readline())
apples = []
for _ in range(k):
    apples.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
direction = []
for _ in range(l):
    direction.append(list(map(int, sys.stdin.readline().split())))

