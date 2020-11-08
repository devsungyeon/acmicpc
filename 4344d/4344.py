c = int(input())

def upperThanAvg(li, avg):
    cnt = 0
    for i in range(li[0]):
        if li[i+1] > avg:   cnt += 1
    return cnt

for i in range(c):
    li = list(map(int, input().split()))
    avg = (sum(li)-li[0]) / li[0]
    upp = upperThanAvg(li, avg)
    ans = upp/li[0]*100
    print(f"{ans:.3f}%")