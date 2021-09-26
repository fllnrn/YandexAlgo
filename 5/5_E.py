i = open("threesum.in", "r")


s = int(i.readline())
amap = list(map(int, i.readline().split()))
bmap = list(map(int, i.readline().split()))
cmap = list(map(int, i.readline().split()))
i.close()

def find():
    for ai in range(1, amap[0] + 1):
        if amap[ai] > s:
            continue
        for bi in range(1, bmap[0] + 1):
            presum = amap[ai] + bmap[bi]
            if presum > s:
                continue
            for ci in range(1, cmap[0] + 1):
                if presum + cmap[ci] == s:
                    return [ai-1, bi-1, ci-1]
    return [-1]


o = open("threesum.out", "w")   
o.write(" ".join(map(str, find())))         
o.close()