next = int(input())
max_n = next
count = 0
while next != 0:
    if next > max_n:
        count = 1
        max_n = next
    elif next == max_n:
        count += 1
    next = int(input())

print(count)