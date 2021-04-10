import sys

def find_leaf_node(li):
    cnt = 0 
    for i in li:
        if i == [-1]:
            cnt += 1
    return cnt

def del_node(node, li):
    for i in li[node]:
        if i != -1:
            del_node(i, li)
    li[node] = []

n = int(sys.stdin.readline())
matrix = [[-1] for _ in range(n)]
inputli = list(map(int, sys.stdin.readline().split()))

root = 0
for i in range(n):
    if inputli[i] == -1:
        root = i
    else:
        matrix[inputli[i]].append(i)

del_node_num = int(input())
del_node(del_node_num, matrix)
for i in matrix:
    for j in i:
        if j == del_node_num:
            i.remove(j)
#print(matrix)
print(find_leaf_node(matrix))