import sys
n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

s=e=0
ans=1000000
tmp=li[0]
while e<n:
    if tmp == s:
        ans = min(ans, e-s+1)
        e+=1
        if e==n:    break
        s-=1
        tmp+=li[e]
        tmp-=li[s]
    elif tmp > s:
        if s==e:
            s=e=e+1
            if e==n:    break
            tmp=li[e]
        else:
            tmp-=li[s]
            s+=1
    else:
        e+=1
        if e==n:    break
        tmp+=li[e]
if ans==1000000:
    print(0)
else:
    print(ans)
