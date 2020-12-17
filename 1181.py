li = []
for i in range(int(input())):
    li.append(input())
li = list(set(li))
li.sort(key=lambda x: (len(x), x))
for i in li:
    print(i)