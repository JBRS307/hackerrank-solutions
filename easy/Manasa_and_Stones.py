n = int(input())
for _ in range(n):
    stones = int(input())-1
    diffA = int(input())
    diffB = int(input())
    possibleLastValues = []
    counterA = stones
    counterB = 0
    if diffA == diffB:
        print(diffA*(stones))
        continue
    for _ in range(stones+1):
        possibleLastValues.append(counterA*diffA+counterB*diffB)
        counterA -= 1
        counterB += 1
    possibleLastValues.sort()
    for value in possibleLastValues:
        print(value, end=' ')
    print()