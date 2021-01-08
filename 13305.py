import sys
n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split())) # n-1
gasstation = list(map(int, sys.stdin.readline().split())) # n
d = [0]*(n-1)

d[0] = roads[0] * gasstation[0]
minval = gasstation[0]
for i in range(1,n-1):
    if gasstation[i] < minval:
        minval = gasstation[i]
    d[i] = d[i-1] + minval * roads[i]
    
print(d[-1])