votes = dict()

while True:
    try:
        candidate, peoples = input().split()
        if candidate in votes:
            votes[candidate] += int(peoples)
        else:
            votes[candidate] = int(peoples)
    except:
        break

names = list(votes.keys())
names.sort()
for name in names:
    print("{0} {1}".format(name, votes[name]))