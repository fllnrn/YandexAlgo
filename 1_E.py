d = int(input())
x, y = map(int, input().split())

if (x >= 0) and (y >= 0) and (y <= (d - x)):
    print(0)
else:
    if x <= d/2 and y <= d/2:
        print(1)
    elif y <= x:
        print(2)
    else:
        print(3)