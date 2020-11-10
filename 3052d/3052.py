n = 10
li = []
for i in range(n):
    li.append(int(input()) % 42)
print(len(set(li)))