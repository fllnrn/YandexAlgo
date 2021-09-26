n = int(input())
diplomas = list(map(int, input().split()))

max_folder = diplomas[0]
sum = max_folder
for i in range(1, n):
    sum += diplomas[i]
    max_folder = max(max_folder, diplomas[i])


print(sum - max_folder)