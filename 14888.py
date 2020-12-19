import itertools

n = int(input())

varli = list(map(int, input().split()))

expli = ['+', '-', '*', '/']
expnu = list(map(int, input().split()))
expli = [expli[0]]*expnu[0] + [expli[1]]*expnu[1] + [expli[2]]*expnu[2] + [expli[3]]*expnu[3]

expallli = list(set(itertools.permutations(expli, len(expli))))

def add(a,c):
    return a + c

def substract(a,c):
    return a - c

def multiply(a,c):
    return a * c

def divide(a,c):
    if a < 0:
        return -(abs(a)//c)
    return a // c

def calc(varli, expli):
    calcval = varli[0]
    for i in range(len(expli)):
        if expli[i] == '+':
            calcval = add(calcval, varli[i+1])
        elif expli[i] == '-':
            calcval = substract(calcval, varli[i+1])
        elif expli[i] == '*':
            calcval = multiply(calcval, varli[i+1])
        elif expli[i] == '/':
            calcval = divide(calcval, varli[i+1])
    return calcval

maxval = -1000000000
minval = 1000000000
for i in expallli:
    calcval = calc(varli, i)
    maxval = max(maxval, calcval)
    minval = min(minval, calcval)
print(maxval)
print(minval)