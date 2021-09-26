f = open("input.txt", "r")


n = int(f.readline())
array = list(map(int, f.readline().split()))
k = int(f.readline())
q = []
for i in range(k):
    left, right = map(int, f.readline().split())
    q.append((left,right))
f.close()

array.sort()

# d = {}
# for i in range(5):
#     if array[i] in d:
#         d[array[i]] += [i]
#     else:
#         d[array[i]] = [i]
o = open("output.txt", "w")   
o.write()       
o.close()