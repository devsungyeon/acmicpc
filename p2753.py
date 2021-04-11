year = int(input())
yunyear = 0
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0 :
        yunyear = 1
print(yunyear)