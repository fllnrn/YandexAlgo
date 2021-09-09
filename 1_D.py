N = int(input())
x = list(map(int, input().split()))

if N % 2 == 0:
    print(int((x[int(N/2 -1)] + x[int(N/2)])/2))
else:
    print(x[int(N/2)])