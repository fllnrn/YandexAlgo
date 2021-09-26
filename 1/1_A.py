taskCompeteCode = int(input())
iteratorCode = int(input())
checkerCode = int(input())


def getResultCode(taskCompeteCode, iteratorCode, checkerCode):
    if iteratorCode == 0:
        if taskCompeteCode != 0:
            return 3
        else:
            return checkerCode
    if iteratorCode == 1:
        return checkerCode
    if iteratorCode == 4:
        if taskCompeteCode != 0:
            return 3
        else:
            return 4
    if iteratorCode == 6:
        return 0
    if iteratorCode == 7:
        return 1

    return iteratorCode

print(getResultCode(taskCompeteCode, iteratorCode, checkerCode))