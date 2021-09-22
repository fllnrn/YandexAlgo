n = int(input())
nums = list(map(int, input().split()))
lastSumm = nums[0]
maxSumm = lastSumm
for i in range(1, n):
    if lastSumm < 0:
        lastSumm = 0
    lastSumm += nums[i]
    if lastSumm > maxSumm:
        maxSumm = lastSumm
    
print(maxSumm)