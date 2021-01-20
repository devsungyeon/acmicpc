import sys
sys.setrecursionlimit(10**9)
n = int(input())
matrix = [[] for _ in range(n+1)]

#li = [[1, 2, 3],[1, 3 ,2],[2, 4, 5],[3, 5, 11],[3, 6, 9],[4, 7, 1],[4, 8, 7],[5, 9, 15],[5, 10, 4],[6, 11, 6],[6, 12, 10]]

for i in range(n-1):
    path = list(map(int,sys.stdin.readline().split()))
#    path = li[i]
    matrix[path[0]].append([path[1], path[2]])
    matrix[path[1]].append([path[0], path[2]])

def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e, matrix, result)
            
result = [0 for _ in range(n+1)]
DFS(1, matrix, result)
result[1] = 0

idx = result.index(max(result))
result = [0 for _ in range(n+1)]
DFS(idx, matrix, result)
result[idx] = 0
print(max(result))