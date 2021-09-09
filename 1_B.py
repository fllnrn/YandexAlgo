N, i, j= map(int, input().split())

def func(N, i, j):
    way1 = max(i ,j) - min(i,j)
    way2 = min(i,j) + N - max(i,j)
    return min(way1, way2)-1

print(func(N,i,j))