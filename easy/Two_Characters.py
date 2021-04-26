def check(altering):
    for i in range(len(altering)-1):
        if altering[i] == altering[i+1]:
            return False
    return True

#=================================================
length = int(input())
string = input()

setStr = list(set(string))
maxLen = 0
for i in range(len(setStr)):
    for j in range(i+1, len(setStr)):
        altering = [char for char in string if char == setStr[i] or char == setStr[j]]
        if check(altering):
            maxLen = max(maxLen, len(altering))
print(maxLen)

