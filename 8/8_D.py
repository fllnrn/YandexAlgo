from typing import Match


n = int(input())
nodes = [[] for i in range(n+1)]

for _ in range(n-1):
    l, r = map(int, input().split())
    nodes[l] += [r]
    nodes[r] += [l]

stack = [n]
heights = [0]*(n+1)
visited = [0]*(n+1)
maxHeight = 0
maxNode = 0
while stack:
    curNode = stack.pop()
    visited[curNode] = 1
    curHeight = heights[curNode]
    for child in nodes[curNode]:
        if visited[child] == 0:
            heights[child] = curHeight + 1
            stack.append(child)
    if maxHeight < curHeight:
        maxHeight = curHeight
        maxNode = curNode

stack = [maxNode]
heights = [0]*(n+1)
visited = [0]*(n+1)
maxHeight = 0
while stack:
    curNode = stack.pop()
    visited[curNode] = 1
    curHeight = heights[curNode]
    for child in nodes[curNode]:
        if visited[child] == 0:
            heights[child] = curHeight + 1
            stack.append(child)
    if maxHeight < curHeight:
        maxHeight = curHeight

print(maxHeight+1)