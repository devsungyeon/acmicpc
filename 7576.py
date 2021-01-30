import sys
from collections import deque
m,n = map(int, input().split())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()
for x in range(n):
    for y in range(m):
        if s[x][y] == 1:
            queue.append([x,y])

days = 0
while queue:
    days += 1 
    a,b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0<=x<n and 0<=y<m and s[x][y] == 0:
            s[x][y] = s[a][b] + 1
            queue.append([x,y])

isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
