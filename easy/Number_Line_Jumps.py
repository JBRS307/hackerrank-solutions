def checkJumps(kang1, kang2):
    if kang1[1] < kang2[1] or (kang1[1] == kang2[1] and kang1[0] != kang2[0]):
        return 'NO'
    if kang1[0] == kang2[0] and kang1[1] == kang2[1]:
        return 'YES'

    while kang1[0] < kang2[0]:
        kang1[0] += kang1[1]
        kang2[0] += kang2[1]
    
    if kang1[0] == kang2[0]:
        return 'YES'
    return 'NO'
    

#=================================================================
x1, v1, x2, v2 = list(map(int, input().rstrip().split()))

if x1 <= x2:
    kang1 = [x1, v1]
    kang2 = [x2, v2]
else:
    kang1 = [x2, v2]
    kang2 = [x1, v1]

print(checkJumps(kang1, kang2))