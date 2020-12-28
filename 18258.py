import sys
from collections import deque
n = int(input())
li = deque([])
cnt = 0
for _ in range(n):
    tmp = list(map(str, sys.stdin.readline().split()))
    if tmp[0] == "push":
        li.append(tmp[1])
    elif tmp[0] == "pop":
        if not li:
            print(-1)
        else:
            print(li.popleft())
    elif tmp[0] == "size":
        print(len(li))
    elif tmp[0] == "empty":
        if not li:
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if not li:
            print(-1)
        else:
            print(li[0])
    elif tmp[0] == "back":
        if not li:
            print(-1)
        else:
            print(li[-1])