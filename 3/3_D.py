n = int(input())
belatrice_say = input()
answer = set(range(1, n+1))
while belatrice_say != 'HELP':
    nums = set(map(int, belatrice_say.split()))
    august_say = input()
    if august_say == 'NO':
        for num in nums:
            if num in answer:
                answer.remove(num)
    else:
        if answer:
            for num in list(answer):
                if not(num in nums):
                    answer.remove(num)
    belatrice_say = input()

answer = list(answer)
answer.sort()
print(" ".join(str(x) for x in answer))