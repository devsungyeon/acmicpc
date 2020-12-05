n = int(input())
i = 1
if n == 1:
    print(1)
    exit()
while(True):
    if(3*(i-2)*(i-1)+1 < n and n <= 3*(i-1)*i + 1):
        break
    i+=1
print(i)