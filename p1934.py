import sys
t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    multi = a*b
    while max(a,b) % min(a,b) != 0:
        tmp = max(a,b) % min(a,b)
        b = min(a,b)
        a = tmp
    print(int(multi / min(a,b)))