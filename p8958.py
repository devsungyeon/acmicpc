for i in range(int(input())):
    count = 0
    summ = 0
    for j in input():
        if j == 'O':
            count += 1
            summ += count
        else:
            count = 0
    print(summ)