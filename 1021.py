from collections import deque
n, m = map(int, input().split())

def first(li):
    li.popleft()
def second(li):
    li.append(li.popleft())
def third(li):
    li.appendleft(li.pop())

loc = list(map(int, input().split()))
deq = deque([i for i in range(1, n+1)])
ans = 0

for i in loc:
    if deq.index(i) < len(deq)/2:
        while(deq[0] != i):
            second(deq)
            ans += 1
    else:
        while(deq[0] != i):
            third(deq)
            ans += 1
    first(deq)
print(ans)