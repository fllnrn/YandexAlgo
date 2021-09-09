l1 = input().split()
dubles = set()
unic = set()
answer = []
for l in l1:
    if l in dubles:
        pass
    elif l in unic:
        unic.remove(l)
        answer.remove(l)
        dubles.add(l)
    else:
        unic.add(l)
        answer.append(l)
separator = " "
print(separator.join(answer))