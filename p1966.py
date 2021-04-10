import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    deq = deque(list(map(int, sys.stdin.readline().split())))
    ans = 1
    while(deq):
        idx = deq.index(max(deq))
        if idx == 0:
            deq.popleft()
            if m == 0:
                print(ans)
                break
            else:
                ans += 1
                m = m-1
                m = (len(deq)+m)%len(deq)
        else:
            deq.append(deq.popleft())
            m = m-1
            m = (len(deq)+m)%len(deq)
            
