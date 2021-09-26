ITSCAT = 0
END = 1
START = -1

n, m = map(int, input().split())
events = [ (x, ITSCAT, 0) for x in map(int, input().split())]

answer = [0]*m
for i in range(m):
    l, r = map(int, input().split())
    events.append((l, START, i))
    events.append((r, END, i))

events.sort()


cats = 0
for event in events:
    x, etype, index = event
    if etype == START:
        answer[index] = -cats
    elif etype == END:
        answer[index] += cats
    elif etype == ITSCAT:
        cats += 1
        

print(*answer)