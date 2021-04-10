import sys
n, x, k = map(int, sys.stdin.readline().split())
li = [0]*(n+1)
li[x] = 1
for i in range(k):
    a,b = map(int, sys.stdin.readline().split())
    li[a],li[b] = li[b],li[a]
print(li.index(1))