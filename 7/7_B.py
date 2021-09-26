COM = 1
LEV = -1

n = int(input())
events = []
for i in range(n):
    start, dur = map(int, input().split())
    events.append((start, COM))
    events.append((start+dur, LEV))

events.sort()
machinesCount = 0
maxMachines = 0
left = None
for event in events:
    time, etype = event
    if etype == COM:
        machinesCount += 1
        maxMachines = max(maxMachines, machinesCount)
    if etype == LEV:
        machinesCount -= 1

print(maxMachines)
