l1 = input().split()
s1 = set()

for l in l1:
    if l in s1:
        print('YES')
    else:
        print('NO')
        s1.add(l)