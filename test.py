import sys
import datetime

a,b = map(int, input().split())
weekdays = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(weekdays[((a//2) * 31 + (a > 2)*(((a-1)//2) * 30 - 1) + b+4)%7])