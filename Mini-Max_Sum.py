arr = list(map(int, input().rstrip().split()))

minSum = sum(arr) - max(arr)
maxSum = sum(arr) - min(arr)

print(minSum, maxSum)