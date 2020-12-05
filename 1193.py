# n = int(input())
# i = 1
# if n == 1:
#     print("1/1")
#     exit()
# while(True):
#     if((i-1)*(i)/2 < n and n <= (i+1)*i/2):
#         break
#     i+=1
# if i%2 == 0:
#     print(str(int(n - (i-1)*i/2)) +"/" +str(int(1+i-(n - (i-1)*i/2))))
# else:
#     print( str(int(1+i-(n - (i-1)*i/2)))+"/"+str(int(n - (i-1)*i/2)))

x,i,s = int(input()),2,1
while x>s:s+=i;i+=1
a = [s-x+1,i-s+x-1][i%2]
print(s-x+1,i-s+x-1,i%2)
print(a, "/",i-a,sep="")