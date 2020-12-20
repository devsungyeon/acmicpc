n = int(input())
count = 0

def isPromising(q, n):
    for i in range(n):
        if (q[i] == q[n]): return False   # same column
        if ((q[i] - q[n]) == (n - i)): return False   # '\' direction
        if ((q[n] - q[i]) == (n - i)): return False   # '/' direction
    return True

def enumerate(q, n):
    global count
    N = len(q)
    # if n reach the end, plus the count
    if (n == N):
        count+=1
    else:
        for i in range(N):
            q[n] = i
            if isPromising(q, n): enumerate(q, n + 1)   # isPromising is true, then keep it down(recursive)
a = [0]*n
enumerate(a, 0)
print(count)