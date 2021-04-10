for i in range(int(input())):
	# i번째 Test Case의 정보 입력
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    # 두 원의 중심좌표간의 거리 의 제곱
    d = (x1-x2)**2 + (y1-y2)**2
    # 두 원이 일치하는 경우
    if (r1 == r2 and d == 0):
        print(-1)
    # 두 원이 두 점에서 만나는 경우
    elif (r1 - r2)**2 < d and d < (r1 + r2)**2:
        print(2)
    # 두 원이 한 점에서 만나는 경우
    elif (r1 - r2)**2 == d or d == (r1 + r2)**2:
        print(1)
    # 두 원이 만나지 않는 경우
    else:
        print("0")