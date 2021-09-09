word = input()
dif = 0
left = 0
right = len(word)-1
while left < right:
    if word[left] != word[right]:
        dif += 1
    left += 1
    right -= 1
print(dif)
