def countSwaps(arr, size):
    m = {}
    beauty = sorted(arr)
    for i in range(size):
        m[arr[i]] = i

    swaps = 0
    for i in range(size):
        if beauty[i] != arr[i]:
            swaps += 1
        
            toSwap = m[beauty[i]]  
            m[arr[i]] = m[beauty[i]]
            arr[i], arr[toSwap] = beauty[i], arr[i]
    return swaps

#====================================================
size = int(input())
arr = list(map(int, input().rstrip().split()))

swapsAsc = countSwaps(arr[:], size)
swapsDesc = countSwaps(arr[::-1], size)

print(min(swapsAsc, swapsDesc))
