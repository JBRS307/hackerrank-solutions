heights = list(map(int, input().rstrip().split()))
word = input()

letters = list(map(ord, word))
for i in range(len(letters)):
    letters[i] -= 97
    letters[i] = heights[letters[i]]

print(len(letters) * max(letters))