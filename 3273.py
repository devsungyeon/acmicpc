import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())

li.sort()

s = 0
e = len(li)-1

ans = 0
while s < e:
    if li[s] + li[e] == x:
        ans += 1
        s += 1
        e -= 1
    elif li[s] + li[e] > x:
        e -= 1
    elif li[s] + li[e] < x:
        break

print(ans)