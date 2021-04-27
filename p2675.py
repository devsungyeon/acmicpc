for _ in range(int(input())):
    r, s = map(str, input().split())
    r = int(r)
    ans = ''
    for q in s:
        ans += q*r
    print(ans)

