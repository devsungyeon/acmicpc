li = []
for i in range(int(input())):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: (x[1],x[0]))
for i in li:
    print(i[0], i[1])