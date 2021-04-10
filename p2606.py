import sys
nodes = int(input())
edges = int(input())

matrix = [[0]*(nodes+1) for _ in range(nodes+1)]
visited = [0] * (nodes+1)
for _ in range(edges):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(root, li):
    visited[root] = 1
    for i in range(nodes+1):
        if matrix[root][i] != 0:
            matrix[root][i] = matrix[i][root] = 0
            dfs(i, li)

dfs(1, matrix)

print(sum(visited) - 1)