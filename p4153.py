while True:
    a = list(map(int,input().split()))
    if a[0] == 0:
        break
    a.sort()
    print("right" if a[2]**2 == a[0]**2 + a[1]**2 else "wrong")