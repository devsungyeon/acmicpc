li = []
for i in range(int(input())):
    tmp = list(map(str,input().split()))
    tmp.append(i)
    li.append(tmp)
li.sort(key=lambda x: (int(x[0]),x[2]))
for i in li:
    print(i[0], i[1])