s1 = set(input().split())
count = 0
s2 = input().split()
for i in s2:
    if i in s1:
        count += 1
print(count)