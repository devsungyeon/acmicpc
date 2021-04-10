for i in range(int(input())):
    h,w,n = map(int,input().split())
    print(str((n-1)%h+1),str((n-1)//h+1).zfill(2),sep="")