n = int(input())
leftright = []
for i in range(n):
    l, r = map(int, input().split())
    leftright.append((min(l,r), max(l,r)))

leftright.sort()
answer = 0
left, right  = leftright[0]
for i in range(n):
    nextleft, nextright = leftright[i]
    if nextleft  <= right:
        right = nextright
        if i == n-1:
            answer += right - left
    else:
        answer += right - left
        left = nextleft
        right = nextright

print(answer)