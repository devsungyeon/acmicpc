import sys
sdk = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

def sudoku(index):
    if index == len(zeros):
        for row in sdk:
            print(*row)
        sys.exit(0)
    
    x = zeros[index][0]
    y = zeros[index][1]
    dx = (x // 3) * 3
    dy = (y // 3) * 3

    num_list = [0] + [1 for _ in range(9)]
    for j in range(9):
        if(sdk[x][j]):
            num_list[sdk[x][j]] = 0
        if(sdk[j][y]):
            num_list[sdk[j][y]] = 0
    
    for i in range(dx, dx + 3):
        for j in range(dy, dy + 3):
            check_num = sdk[i][j]
            if(check_num):
                num_list[check_num] = 0
    candidate_list = []
    for i in range(len(num_list)):
        if num_list[i] == 1:
            candidate_list.append(i)
    
    for num in candidate_list:
        sdk[x][y] = num
        sudoku(index + 1)
        sdk[x][y] = 0


sudoku(0)