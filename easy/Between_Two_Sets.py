sizeA, sizeB = list(map(int, input().strip().split()))
setA = set(map(int, input().strip().split()))
setB = set(map(int, input().strip().split()))

count = 0
for i in range(1, 101):
    for num in setA:
        if i%num != 0:
            break
    else:
        for num in setB:
            if num%i != 0:
                break
        else:
            count += 1

print(count)