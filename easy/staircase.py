levels = int(input())
spaces = levels - 1
currLvl = 1
for _ in range(levels):
    for _ in range(spaces):
        print(' ', end='')
    spaces -=1
    for _ in range(currLvl):
        print('#', end='')
    currLvl +=1
    print()