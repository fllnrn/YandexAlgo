freq = dict()
while True:
    try:
        words = input().split()
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    except:
        break

answer = [ (freq[name], name) for name in freq.keys() ]
answer.sort(key=(lambda x: (-x[0], x[1])))
for _, name in answer:
    print(name)