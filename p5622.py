li = {chr(i+65):i//3+2 for i in range(26)}
li['S'] = 7
li['V'] = 8
li['Y'] = 9
li['Z'] = 9

print(sum([li[i]+1 for i in input()]))
