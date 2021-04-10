def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

n = int(input())
for i in range(n):
    tmp = int(input())
    li = prime_list(tmp)
    lihalf = [q for q in li if (q <= tmp/2)]
    lihalf.sort(reverse=True)
    for j in lihalf:
        if tmp-j in li:
            print(j, tmp-j)
            break