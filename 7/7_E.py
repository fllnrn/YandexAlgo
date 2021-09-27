import math
n = int(input())
START = -1
END = 1

events = []
linesEvents = []
for i in range(n):
    r1, r2, f1, f2 = map(float, input().split())
    events.append((f1, START, i))
    events.append((f2, END, i))
    linesEvents.append((min(r1, r2), START))
    linesEvents.append((max(r1, r2), END))

linesOpenedCount = 0
events.sort()
linesOpened = set()
for event in events:
    angle, etype, index = event
    if etype == START:
        linesOpened.add(index)
        linesOpenedCount += 1
    elif etype == END:
        if index in linesOpened:
            linesOpened.remove(index)
            linesOpenedCount -= 1
peresya = []
peresye = (0, 2 * math.pi)
for event in events:
    angle, etype, index = event
    if etype == START:
        linesOpenedCount += 1
        if linesOpenedCount == n:
            peresye = (angle, peresye[1])
    elif etype == END:
        if linesOpenedCount == n:
            peresye = (peresye[0], angle)
            peresya.append(peresye)
            peresye  = (0, 2 * math.pi)
        linesOpenedCount -= 1
if peresye[0]!= 0:
    peresya.append(peresye)

linesEvents.sort()
linesOpenedCount = 0
left = 0
right = 0
for dot in linesEvents:
    x, etype = dot
    if etype == START:
        linesOpenedCount += 1
        if linesOpenedCount == n:
            left = x
    elif etype == END:
        if linesOpenedCount == n:
            right = x
            break
        linesOpenedCount -= 1

area = 0
for p in peresya:
    area += p[1] - p[0]

area = (area * (right**2) / 2) - (area * (left ** 2) / 2)

print(area)