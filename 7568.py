def compare(li):
    for i in li:
        for j in li:
            if i[0]<j[0] and i[1]<j[1]:
                i[2] += 1

li = []
for i in range(int(input())):
    tmp = list(map(int,input().split()))
    tmp.append(1)
    li.append(tmp)
compare(li)
for i in li:
    print(i[2], end=" ")    