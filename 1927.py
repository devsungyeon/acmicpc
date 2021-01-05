import sys
from queue import PriorityQueue
n = int(input())

li = PriorityQueue()

tmp = n
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not li.empty():
            print(li.get())
        else:
            print(0)
    else:
        li.put(x)