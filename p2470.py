import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

s = 0
e = len(li)-1
ans = []
tmp = 10000000000000000000
while s < e:
    if li[s] + li[e] == 0:
        ans = [li[s], li[e]]
        break
    else:
        sumse = li[s] + li[e]
        if abs(sumse) < abs(tmp):
            tmp = sumse
            ans = [li[s], li[e]]
        if sumse < 0:
            s += 1
        else:
            e -= 1
ans.sort()
print(*ans)