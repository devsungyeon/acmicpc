n = int(input())
i = 665
while(n!=0):
    i += 1
    if str(i).find('666') != -1:
        n-=1
print(i)