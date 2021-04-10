import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

ans = {-1:0, 0:0, 1:0}
def cut(x, y, n, li):
    global ans
    firstval = li[x][y]
    chk = True
    for i in range(x, x+n):
        if chk == False:
            break
        for j in range(y, y+n):
            if li[i][j] != firstval:
                chk = False
                break
    if chk == True:
        ans[firstval] += 1
    else:
        cut(x, y, n//3, li)
        cut(x, y+n//3, n//3, li)
        cut(x, y+n//3+n//3, n//3, li)

        cut(x+n//3, y, n//3, li)
        cut(x+n//3, y+n//3, n//3, li)
        cut(x+n//3, y+n//3+n//3, n//3, li)

        cut(x+n//3+n//3, y, n//3, li)
        cut(x+n//3+n//3, y+n//3, n//3, li)
        cut(x+n//3+n//3, y+n//3+n//3, n//3, li)
        
cut(0, 0, n, li)
for i in ans:
    print(ans[i])