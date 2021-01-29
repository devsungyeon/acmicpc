import sys
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(sys.stdin.readline()))

def clear(x,y):
    cnt = 0
    if x-1>=0 and y>=0 and x-1<n and y<n and matrix[x-1][y] == '1':
        matrix[x-1][y] = '0'
        cnt += 1
        cnt += clear(x-1,y)
    if x>=0 and y-1>=0 and x<n and y-1<n and matrix[x][y-1] == '1':
        matrix[x][y-1] = '0'
        cnt += 1
        cnt += clear(x,y-1)
    if x+1>=0 and y>=0 and x+1<n and y<n and matrix[x+1][y] == '1':
        matrix[x+1][y] = '0'
        cnt += 1
        cnt += clear(x+1,y)
    if x>=0 and y+1>=0 and x<n and y+1<n and matrix[x][y+1] == '1':
        matrix[x][y+1] = '0'
        cnt += 1
        cnt += clear(x,y+1)
    return cnt
    
ans = 0
homes = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            matrix[i][j] = '0'
            ans += 1
            homes.append(clear(i,j)+1)

print(ans)
homes.sort()
for i in homes:
    print(i)