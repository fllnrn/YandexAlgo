def solve(dudu):
    leafs = []
    code = []
    for c in dudu:
        if c == 'D':
            code += [0]
        if c == 'U':
            leafs.append(code.copy())
            while code.pop() == 1:
                pass
            code += [1]
    leafs.append(code.copy())
    print(len(leafs))
    for leaf in leafs:
        print("".join([str(x) for x in leaf]))

n = int(input())
trees = []
for _ in range(n):
    trees.append(input())
for tree in trees:
    solve(tree)