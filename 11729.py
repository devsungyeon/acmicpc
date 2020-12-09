def hanoi(n,a,b,c):
    if n==1:
        ans.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        ans.append([a,c])
        hanoi(n-1,b,a,c)

n = int(input())
ans = []
hanoi(n,1,2,3)

print(len(ans))
print("\n".join([' '.join(str(i) for i in row) for row in ans]))
