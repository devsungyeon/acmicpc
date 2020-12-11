


m,n = map(int,input().split())
board = []
for i in range(m):
    board.append(input())

for i in range(m-8+1):# m
    for j in range(n-8+1):
        #tmp = board[i:i+8,j:j+8]
        print()
print(board[0:1, 1:3])


        