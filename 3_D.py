n = int(input())
belatrice_say = input()
wrong = set()
answer = set()
while belatrice_say != 'HELP':
    nums = list(map(int, belatrice_say.split()))
    august_say = input()
    if august_say == 'NO':
        for num in nums:
            if not (num in wrong):
                if num in answer:
                    answer.remove(num)
                wrong.add(num)
    else:
        for num in nums:
            if not (num in wrong):
                answer.add(num)
    belatrice_say = input()

answer = list(answer)
answer.sort()
print(" ".join(str(x) for x in answer))