import sys, math
k, n = map(int, sys.stdin.readline().split())
lanlist = []
for _ in range(int(k)):
    lanlist.append(float(sys.stdin.readline()))

maxval = math.floor(sum(lanlist)/n)

def lanlength(val):
    global lanlist
    ret = 0
    for i in lanlist:
        ret += i // val
    return ret

def find(start, end, target):
    mid = (start+end) // 2

    lanlen = lanlength(mid)
    while start <= end:
        if lanlen >= target:
            return find(mid+1, end, target)
        else:
            return find(start, mid-1, target)
    return end

print(find(1, maxval, n))