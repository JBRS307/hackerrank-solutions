n = int(input())
candles = list(map(int, input().rstrip().split()))
maxItem = max(candles)
print(candles.count(maxItem))