types = list(map(int, input().split()))

house_stack = []
left_store = -1
right_store = -1
max_distance = 0

def findmax():
    global left_store, right_store, max_distance
    for house in house_stack:
        if left_store > -1 and right_store > -1:
            left_d = abs(left_store - house)
            right_d = abs(right_store - house)
            min_distance = min(left_d, right_d)
            max_distance = max(max_distance, min_distance)
            
        else:
            store = max(left_store, right_store)
            max_distance = max(max_distance, abs(store - house))

    if left_store > -1 and right_store > -1:
        left_store = right_store
        right_store = -1
    elif left_store == -1:
        left_store = right_store
        right_store = -1

    house_stack.clear()

for i in range(len(types)):
    if types[i] == 1:
        house_stack.append(i)
    if types[i] == 2:
        if len(house_stack) > 0:
            if left_store == -1:
                right_store = i
            else:
                right_store = i
            findmax()
        elif left_store > -1:
            left_store = i
        else:
            right_store = i
            findmax()


if len(house_stack) > 0:
    findmax()

print(max_distance)