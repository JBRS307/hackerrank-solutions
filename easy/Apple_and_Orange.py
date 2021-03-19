house = list(map(int, input().rstrip().split()))
appleTree, orangeTree = list(map(int, input().rstrip().split()))
apples, oranges = list(map(int, input().rstrip().split()))
appleTreeDist = list(map(int, input().rstrip().split()))
orangeTreeDist = list(map(int, input().rstrip().split()))

appleDist = [appleTree+appleTreeDist[i] for i in range(apples)]
orangeDist = [orangeTree+orangeTreeDist[i] for i in range(oranges)]

houseApples = 0
houseOranges = 0

for apple in appleDist:
    if apple >= house[0] and apple <= house[1]:
        houseApples+=1
for orange in orangeDist:
    if orange >= house[0] and orange <= house[1]:
        houseOranges+=1

print(houseApples)
print(houseOranges)

