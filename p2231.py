n = int(input())
ans = 0
for i in range(n+1):
    a = list(map(int, str(i)))
    ans = i + sum(a)
    if ans == n:
        print(i)
        break

    if i==n:
        print(0)
