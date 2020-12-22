import sys

bracket = {"(":")", "[":"]"}

while(True):
    string = input()
    if string == ".":
        sys.exit()
    string = list(str(string))
    stack = []
    try:
        for i in string:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")" or i == "]":
                temp = stack.pop()
                if i != bracket[temp]:
                    stack.append(temp)
                    break
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
    except IndexError:
        print("no")
            

