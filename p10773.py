li = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        li.pop()
    else:
        li.append(n)
print(sum(li))