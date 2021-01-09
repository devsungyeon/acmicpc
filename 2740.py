import sys
n, m = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

m, k= map(int, sys.stdin.readline().split())
B = []
for _ in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

C = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for q in range(k):
            C[i][q] = C[i][q] + A[i][j] * B[j][q]

for i in C:
    print(*i)
