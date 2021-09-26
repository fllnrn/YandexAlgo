n, q = map(int, input().split())
array = list(map(int, input().split()))
presum = [0]*(n+1)
for i in range(n):
    presum[i+1] = presum[i] + array[i]

for _ in range(q):
    left, right = map(int, input().split())
    print(presum[right]-presum[left-1])
