def findSort(arr, size):
    left = float('inf')
    right = float('inf')
    operation = ''
    temp = sorted(arr)
    i = 0
    while arr[i] == temp[i]:
        i+=1
        if i == size:
            return 'yes', None, None, None
    left = i
    i+=1
    while arr[i] == temp[i]:
        i+=1
    if i - left == 1:
        while arr[i] < arr[i-1]:
            i+=1
        right = i-1
        operation = 'reverse'
        if right - left == 1:
            operation = 'swap'
    else:
        right = i
        operation = 'swap'
    
    if operation == 'swap':
        arr[left], arr[right] = arr[right], arr[left]
    elif operation == 'reverse':
        try:
            arr[left:right+1] = reversed(arr[left:right+1])
        except:
            arr[left:] = reversed(arr[left:])
    if arr == temp:
        return 'yes', operation, left+1, right+1
    return 'no', None, None, None

    


#===============================================================
size = int(input())
arr = list(map(int, input().rstrip().split()))
command, operation, left, right = findSort(arr, size)
print(command)
if operation != None:
    print(operation, left, right)

