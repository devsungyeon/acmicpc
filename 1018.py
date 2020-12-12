# import numpy as np

# def paintingcnt(li):
#     schar = True
#     cnt = 0
#     for i in li:
#         tmp = schar
#         for j in i:
#             if j != ('B' if tmp == True else 'W'):
#                 cnt += 1
#             tmp = not(tmp)
#         schar = not(schar)
#     paint = cnt
#     ################
#     schar = False
#     cnt = 0
#     for i in li:
#         tmp = schar
#         for j in i:
#             if j != ('B' if tmp == True else 'W'):
#                 cnt += 1
#             tmp = not(tmp)
#         schar = not(schar)
#     return min(paint,cnt)

# m,n = map(int,input().split())
# board = []
# ans = 10000000000

# for i in range(m):
#     board.append(list(input()))
# board = np.array(board)

# for i in range(m-8+1):# m
#     for j in range(n-8+1):
#         tmp = board[i:i+8,j:j+8]
#         ans = min(ans, paintingcnt(tmp))
# print(ans)

def splitmatrix(li,a,b):
    splitmatrix = []
    for i in range(a,a+8):
        tmp = []
        for j in range(b,b+8):
            tmp.append(li[i][j])
        splitmatrix.append(tmp)
    return splitmatrix

def paintingcnt(li):
    schar = True
    cnt = 0
    for i in li:
        tmp = schar
        for j in i:
            if j != ('B' if tmp == True else 'W'):
                cnt += 1
            tmp = not(tmp)
        schar = not(schar)
    paint = cnt
    ################
    schar = False
    cnt = 0
    for i in li:
        tmp = schar
        for j in i:
            if j != ('B' if tmp == True else 'W'):
                cnt += 1
            tmp = not(tmp)
        schar = not(schar)
    return min(paint,cnt)

m,n = map(int,input().split())
board = []
ans = 10000000000

for i in range(m):
    board.append(list(input()))

for i in range(m-8+1):# m
    for j in range(n-8+1):
        tmp = splitmatrix(board,i,j)
        ans = min(ans, paintingcnt(tmp))
print(ans)