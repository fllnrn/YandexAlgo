l, k = map(int, input().split())
positions = list(map(int, input().split()))

can_have_one = l % 2 != 0
mid = 0
if can_have_one:
    mid = int( l / 2)
else:
    mid = int(l/2)-1

left = 0
right = l
for i in range(len(positions)):
    if positions[i] == mid and can_have_one:
        left = positions[i]
        right = positions[i]
        break
    elif positions[i] <= mid:
        left = max(left, positions[i])
    elif positions[i] > mid:
        right = positions[i]
        break

if left == right:
    print(left)
else:
    print(left, right)