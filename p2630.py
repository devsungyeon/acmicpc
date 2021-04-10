import sys

n = int(sys.stdin.readline())
li=[]
for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

white = 0
blue = 0

def divpp(li,x,y,n):
    global white
    global blue
    chk = li[x][y]
    for i in range(x,x+n):
        for j in range(y, y+n):
            if chk!= li[i][j]:
                h=n//2
                divpp(li,x,y,h)
                divpp(li,x+h,y,h)
                divpp(li,x,y+h,h)
                divpp(li,x+h,y+h,h)
                return

    if chk==1:
        blue += 1
        return
    elif chk==0:
        white += 1
        return


divpp(li,0,0, n)
print(white)
print(blue)

