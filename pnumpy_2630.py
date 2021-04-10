import sys
import numpy as np

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
linp = np.array(li)

white = 0
blue = 0

def divpp(li):
    global white
    global blue
    if np.all(li == 0):
        white += 1
    elif np.all(li == 1):
        blue += 1
    else:
        l = len(li)
        divpp(li[0:l//2, 0:l//2])
        divpp(li[0:l//2, l//2:l])
        divpp(li[l//2:l, 0:l//2])
        divpp(li[l//2:l, l//2:l])
divpp(linp)
print(white)
print(blue)


