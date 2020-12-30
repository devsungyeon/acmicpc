from collections import deque
n = int(input())
deq = deque([i for i in range(1, n+1)])

ans = deq.popleft()
while(deq):
    deq.append(deq.popleft())
    ans = deq.popleft()
    
print(ans)