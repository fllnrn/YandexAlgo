n = int(input())

parents = dict()



for i in range(n-1):
    bottom, top = input().split()
    parents[bottom] = top
    
answer = []

def getLvl(node):
    lvl = 0
    while node in parents:
        node = parents[node]
        lvl += 1
    return lvl

while True:
    try:
        left, right = input().split()
        a = None
        llvl = getLvl(left)
        rlvl = getLvl(right)

        if llvl > rlvl:
            a = 2
        elif llvl < rlvl:
            a = 1

        while llvl != rlvl:
            if llvl > rlvl:
                left = parents[left]
                llvl -= 1
            else:
                right = parents[right]
                rlvl -= 1
        if left != right:
            a = 0
        answer.append(a)

    except EOFError:
        print(*answer)
        break