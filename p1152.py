arr = input()
cnt = 0
for i in arr:
    if i == ' ':
        cnt+=1
if arr[0] == ' ':
    cnt-=1
if arr[len(arr)-1] == ' ':
    cnt-=1
print(cnt+1)