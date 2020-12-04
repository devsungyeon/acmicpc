t = int(input())
for i in range(t):
    n, s = map(str, input().split())
    n = int(n)
    ans = ''
    for j in range(len(s)):
        ans += s[j]*n
    print(ans)