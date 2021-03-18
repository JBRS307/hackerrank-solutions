def countSwaps(arr, beauty, size):
    swaps = 0
    for i in range(size):
        if arr[i] != beauty[i]:
            for j in range(i+1, size):
                if arr[j] == beauty[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    break
    return swaps

#====================================================
size = int(input())
arr = list(map(int, input().rstrip().split()))
beauty = sorted(arr)

swaps1 = countSwaps(arr[:], beauty, size)
swaps2 = countSwaps(arr, beauty[::-1], size)

print(min(swaps1, swaps2))
