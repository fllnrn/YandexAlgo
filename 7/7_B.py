n = int(input())
leftright = []
for i in range(n):
    l, r = map(int, input().split())
    leftright.append((l, l+r))

leftright.sort()
machineCount = 1
nextCount = 1
left, right  = leftright[0]
for i in range(n):
    nextleft, nextright = leftright[i]
    if nextleft  < right:
        nextCount += 1
        right = nextright
    else:
        max(machineCount, nextCount)
        left = nextleft
        right = nextright

print(max(machineCount, nextCount))