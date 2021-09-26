m = int(input())
svid = [""]*m
for i in range(m):
    svid[i] = input()
n = int(input())
pod = [""]*n
for i in range(n):
    pod[i] = input()

def Sogl(num):
    answer = 0
    for sv in svid:
        answer +=1
        for ch in sv:
            if ch in num:
                pass
            else:
                answer -= 1
                break
    return answer
maxsogl = 0
maxsoglpod = []
for i in range(n):
    soglcount = Sogl(pod[i])
    if soglcount == maxsogl:
        maxsoglpod.append(pod[i])
    elif soglcount > maxsogl:
        maxsogl = soglcount
        maxsoglpod.clear()
        maxsoglpod.append(pod[i])
    

for num in maxsoglpod:
    print(num)
