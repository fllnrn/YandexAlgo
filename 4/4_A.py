n = int(input())
di = dict()
for i in range(n):
    color, number = map(int, input().split())

    if color in di:
        di[color] += number
    else:
        di[color] = number
colors = list(di.keys())
colors.sort()
for color in colors:
    print('{0} {1}'.format(color, di[color]))