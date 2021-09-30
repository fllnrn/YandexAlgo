n, s, t = map(int, input().split())
START = 1
END = -1
PRE = -2
times = list(map(int, input().split()))

seats = [] # (time, count)

for newtime in times:
    seats.sort()
    answer = True
    for i in range(len(seats)):
        time, count = seats[i]
        if time >= newtime and time < newtime+t:
            if count+1 > s:
                answer &= False
            else:
                answer &= True
    if answer == True:
        print("YES")
        hasStart = False
        prevCountStart = 0
        hasEnd = False
        prevCountEnd = 0
        prevcount = 0
        repeatStart = False
        repeatEnd = False
        for i in range(len(seats)):
            time, count = seats[i]
            if time == newtime:
                hasStart = True
            if time == newtime+t:
                hasEnd = True
            if time >= newtime and time <= newtime+t:
                seats[i] = (time, count + 1)
            if time > newtime and not repeatStart:
                prevCountStart = prevcount
                repeatStart = True
            if time > newtime+t and not repeatEnd:
                prevCountEnd = prevcount
                repeatEnd = True
            prevcount = count
        if not hasStart:
            seats.append((newtime, prevCountStart + 1))
        if not hasEnd:
            seats.append((newtime+t, prevCountEnd))
    else:
        print("NO")

        
