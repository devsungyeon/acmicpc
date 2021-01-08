import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int,list(sys.stdin.readline())[:-1])))

ans = ""
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
        ans += str(firstval)
    else:
        ans += "("
        cut(x, y, n//2, li)
        cut(x, y+n//2, n//2, li)
        cut(x+n//2, y, n//2, li)
        cut(x+n//2, y+n//2, n//2, li)
        ans += ")"

cut(0, 0, n, li)
print(ans)
