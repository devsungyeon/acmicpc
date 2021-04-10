def last_five(q):
    ans = 0
    while q != 0:
        q = q // 5
        ans += q
    return ans

def last_two(q):
    ans = 0
    while q != 0:
        q = q // 2
        ans += q
    return ans

n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    print(min(last_two(n) - last_two(m) - last_two(n-m), last_five(n) - last_five(m) - last_five(n-m)))
