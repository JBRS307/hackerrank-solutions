length, divisor = list(map(int, input().rstrip().split()))
arr = list(map(int, input().rstrip().split()))

remainders = []
for num in arr:
    if num%divisor == 0:
        remainders.append(divisor)
    else:
        remainders.append(num%divisor)

subLength = 0
Min = 1
Max = divisor - 1
if divisor in remainders:
    subLength += 1

while Min < Max:
    left = remainders.count(Min)
    right = remainders.count(Max)
    if left > right:
        subLength += left
    else:
        subLength += right
    Min += 1
    Max -= 1

if Min == Max:
    subLength += 1

print(subLength)

