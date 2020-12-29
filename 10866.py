import sys
from collections import deque
n = int(input())
li = deque([])
for _ in range(n):
    tmp = list(map(str, sys.stdin.readline().split()))
    try:
        if tmp[0] =="push_front":
            li.appendleft(tmp[1])
        elif tmp[0] =="push_back":
            li.append(tmp[1])
        elif tmp[0] =="pop_front":
            print(li.popleft())
        elif tmp[0] =="pop_back":
            print(li.pop())
        elif tmp[0] =="size":
            print(len(li))
        elif tmp[0] =="empty":
            if not li:
                print(1)
            else:
                print(0)
        elif tmp[0] =="front":
            print(li[0])
        elif tmp[0] =="back":
            print(li[-1])
    except IndexError:
        print(-1)