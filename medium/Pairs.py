size, target = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))

print(len(set(arr) & set([item+target for item in set(arr)])))
