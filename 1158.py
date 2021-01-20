import sys
n, k = map(int, sys.stdin.readline().split())
li = [i for i in range(1, n+1)]
idx = k-1
ans = []
while sum(li) != 0:
    idx %= len(li)
    ans.append(li[idx])
    del li[idx]
    idx += k
    idx -= 1
print("<"+", ".join(str(i) for i in ans)+">")