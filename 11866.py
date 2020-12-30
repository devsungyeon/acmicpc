from collections import deque
n, k = map(int, input().split())
deq = deque([i for i in range(1, n+1)])
ans = []
idx = 0
while(deq):
    idx += (k-1)
    idx = idx % len(deq)
    tmp = deq[idx]
    ans.append(tmp)
    deq.remove(tmp)
print("<", end="")
for i in ans[:-1]:
    print(i, end=", ")
print(str(ans[-1]) + ">")