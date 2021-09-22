
party = []
votes = []
summ = 0
while True:
    try:
        line = input().split()
        party.append(" ".join(line[:-1]))
        vote = int(line[-1])
        summ += vote
        votes.append(vote)
    except:
        break
first = summ / 450
vacant = 450
seats = []
dic = dict()
for i in range(len(votes)):
    seat = int(votes[i] / first)
    vacant -= seat
    seats.append((votes[i] % first, party[i]))
    dic[party[i]] = seat

seats.sort(reverse=True)
while vacant > 0:
    for par in seats:
        if vacant == 0:
            break
        dic[par[1]] += 1
        vacant -= 1

for par in party:
    print("{0} {1}".format(par, dic[par])) 