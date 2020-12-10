n = int(input())
li = [ ['*','*','*'], ['*',' ','*'], ['*','*','*'] ]

li = li+li
print(li)
for i in li:
    for j in i:
        print(j, end='')
    print()