n = int(input())
lines = []
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    if start < n and end > 0:
        lines.append((start, end))
lines.sort(key=lambda x: (x[0], -x[1]))

answer = []
count = 0
left = 0
maxright = 0
currentLine = None
for line in lines:
    if line[0] > left:
        if line[0] <= maxright:
            left = currentLine[1]
            answer.append(currentLine)
        else:
            break
    if line[0] <= left:
        if line[1] > maxright:
            currentLine = line
            maxright = line[1]

    if maxright >= n:
        answer.append(currentLine)
        break
    

if len(answer) == 0 or answer[-1][1] < n:
    print("No solution")
else:
    print(len(answer))
    for l in answer:
        print(*l) 
