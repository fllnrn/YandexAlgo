BEG = -1
END = 1

n = int(input())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((min(l,r), BEG))
    events.append((max(l,r), END))

events.sort()
answer = 0
brushes = 0
left = None
for event in events:
    point, etype = event
    if etype == END:
        brushes -= 1
        if brushes == 0:
            answer += point - left
    elif etype == BEG:
        if brushes == 0:
            left = point
        brushes += 1


print(answer) 