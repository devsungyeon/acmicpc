li = []
for i in range(2, 10000):
    chk = True
    for j in li:
        if i % j == 0:
            chk = False
            break
    if chk == True: li.append(i)
m= int(input())
n= int(input())
lians = []
for i in li:
    if i >=m and i <= n:
        lians.append(i)
if len(lians)==0: print(-1)
else:
    print(sum(lians))
    print(min(lians))