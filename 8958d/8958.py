n = int(input())
for i in range(n):
    str = input()
    cnt = 0
    ans = 0
    for j in str:
        if j == "O":    cnt += 1
        else:   cnt = 0
        ans += cnt
    print(ans)    