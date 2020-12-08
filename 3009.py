x=[0]*3
y=[0]*3
x[0],y[0] = map(int,input().split())
x[1],y[1] = map(int,input().split())
x[2],y[2] = map(int,input().split())
print(((max(x)+min(x))*2 - sum(x)), ((max(y)+min(y))*2 - sum(y)))

