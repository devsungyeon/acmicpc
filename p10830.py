import sys
n, b = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

matrixs = []
matrixs.append(matrix)

def multi(matrix, n):
    multi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multi[i][j] += (matrix[i][k]*matrix[k][j])
                multi[i][j] %= 1000
    return multi

binb = list(map(int,list(bin(b))[2:]))
binb.reverse()

for i in range(len(binb)-1):
    matrixs.append(multi(matrixs[i],n))
def multid(a, b, n):
    multid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multid[i][j] += (a[i][k]*b[k][j])
                multid[i][j] %= 1000
    return multid

ans = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
for i in range(len(binb)):
    if binb[i] != 0:
        ans = multid(ans, matrixs[i], n)

for i in ans:
    print(*i)
