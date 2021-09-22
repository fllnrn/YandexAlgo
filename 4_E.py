n = int(input())
messageToMessage = dict()
messages = []
def incrementTitle(num):
    while messageToMessage[num] != -1:
        num = messageToMessage[num]
    theme = messages[num] 
    messages[num] = (theme[0] - 1 , theme[1], theme[2], theme[3])


for i in range(n):
    number = int(input())
    if number == 0:
        title = input()
        desk = input()
        messages.append((0, i, number-1, title))
        messageToMessage[i] = number-1
    else:
        message = input()
        messages.append((0, i, number-1, message))
        messageToMessage[i] = number-1
        incrementTitle(number-1)
messages.sort()
print(messages[0][3])