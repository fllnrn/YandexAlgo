n, m = map(int, input().split())
x = [ (e, i) for i, e in enumerate(map(int, input().split())) ]
y = [ (e, i+1) for i, e in enumerate(map(int, input().split())) ]
x.sort(reverse=True)
y.sort(reverse=True)
answer = [0]*n

xi = 0
yi = 0
count = 0
while xi < n and yi < m:
    (group, gindex) = x[xi]
    (aud, aindex) = y[yi]
    if aud > group:
        answer[gindex] = aindex
        yi += 1
        count += 1
    xi += 1

print(count)
print( " ".join(map(str, answer)))