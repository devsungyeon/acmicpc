import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stack =[]
ans = [-1 for _ in range(n)]

for i in range(n):
    while len(stack)!=0 and a[stack[-1]] < a[i]:
        ans[stack.pop()]=a[i]
    stack.append(i)
print(*ans)
