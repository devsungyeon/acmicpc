c = int(input())
for i in range(c):
    arr = list(map(int, input().split()))
    n = arr[0]
    sc = arr[1:]
    avg = sum(sc) / n
    tmp = 0
    for j in sc:
        if j > avg:
            tmp += 1
    p = (tmp/n*100)
    print('%.3f' % p + '%')