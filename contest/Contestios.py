n, s, t = map(int, input().split())
START = 1
END = -1
times = list(map(int, input().split()))
events = []
for i in range(n):
    events.append((times[i], START, i))
    events.append((times[i] + t, END, i))

events.sort()

clients = [0]*n
nowClients = set()
nowClientsCount = 0
for event in events:
    time, etype, index = event
    if etype == START:
        if nowClientsCount < s:
            nowClients.add(index)
            clients[index] = 1
            nowClientsCount += 1
        else:
            clients[index] = 0
    if etype == END:
        if index in nowClients:
            nowClients.remove(index)
            nowClientsCount -= 1

for client in clients:
    if client == 1:
        print("YES")
    else:
        print("NO")