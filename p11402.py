n, k, m = map(int, input().split())

def fact_p(n, p):
    ans = 1
    for i in range(n):
        ans = ans * i % p
    return ans

N_K = fact_p(n-k, m)
K = fact_p(k,m)

