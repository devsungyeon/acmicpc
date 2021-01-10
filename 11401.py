n, k = map(int, input().split())
p = 1000000007

def fact_p(n, p):
    ans = 1
    for i in range(n):
        ans = ans * i % p
    return ans
