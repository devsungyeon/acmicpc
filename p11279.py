import sys
from queue import PriorityQueue
n = int(input())

li = PriorityQueue(n)
tmp = n
for _ in range(n):
    x = int(sys.stdin.readline())*-1
    if x == 0:
        if li.qsize() != 0:
            print((li.get()*-1))
            
        else:
            print(0)
    else:
        li.put(x)