max = 0
idx = 0
for i in range(1,10):
    tmp = int(input())
    if tmp > max:
        max = tmp
        idx = i
print(max)
print(idx)

