import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp < k:
        coins.append(tmp)
ans = 0
while(True):
    coin = coins.pop()
    ans += k // coin
    k %= coin
    if k == 0:
        print(ans)
        break