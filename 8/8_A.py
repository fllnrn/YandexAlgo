class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        print("DONE")
        
    def add(self, arg):
        if arg < self.val:
            if self.left:
                self.left.add(arg)
            else:
                self.left = Node(arg)
        elif arg > self.val:
            if self.right:
                self.right.add(arg)
            else:
                self.right = Node(arg)
        else:
            print("ALREADY")

    def search(self, arg):
        if arg > self.val:
            if self.right:
                self.right.search(arg)
            else:
                print("NO")
        elif arg < self.val:
            if self.left:
                self.left.search(arg)
            else:
                print("NO")
        else:
            print("YES")

    def print(self, lvl):
        if self.left:
            self.left.print(lvl+1)
        dots = "."*lvl
        print("".join([dots, str(self.val)]))
        if self.right:
            self.right.print(lvl+1)


tree = None
cmds = []
while True:
    try:
        inpt = input().split()
        if len(inpt) > 0:
            cmd = inpt[0]
        if len(inpt) > 1:
            arg = int(inpt[1])
        cmds.append((cmd, arg))
    except EOFError:
        break
    


for cmd, arg in cmds:
    if cmd == 'ADD':
        if tree:
            tree.add(arg)
        else:
            tree = Node(arg)
    elif cmd == 'SEARCH':
        if tree:
            tree.search(arg)
        else:
            print("NO")
    elif cmd == 'PRINTTREE':
        tree.print(0)
    else:
        break