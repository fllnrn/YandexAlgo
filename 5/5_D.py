symbols = input()
opened = 0
for i in range(len(symbols)):
    if symbols[i] == "(":
        opened += 1
    else:
        opened -= 1
    if opened < 0:
        break
print("YES" if opened == 0 else "NO")