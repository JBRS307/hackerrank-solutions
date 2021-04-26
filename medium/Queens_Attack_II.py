size, obsts = list(map(int, input().rstrip().split()))
row, column = list(map(int, input().rstrip().split()))
obTop = [size+1, 0]
obBot = [0, 0]
obLeft = [0, 0]
obRight = [0, size+1]
obTopLeft = [size+1, 0]
obTopRight = [size+1, size+1]
obBotRight = [0, size+1]
obBotLeft = [0, 0] 

for i in range(obsts):
    obRow, obColumn = list(map(int, input().rstrip().split()))
    if obRow == row:
        if obColumn < column:
            if obColumn > obLeft[1]:
                obLeft = [obRow, obColumn]
        else:
            if obColumn < obRight[1]:
                obRight = [obRow, obColumn]
    elif obColumn == column:
        if obRow < row:
            if obRow > obBot[0]:
                obBot = [obRow, obColumn]
        else:
            if obRow < obTop[0]:
                obTop = [obRow, obColumn]
    elif abs(obRow - row) == abs(obColumn - column):
        if obRow > row and obColumn > column:
            if obRow < obTopRight[0]:
                obTopRight = [obRow, obColumn]
        elif obRow < row and obColumn > column:
            if obRow > obBotRight[0]:
                obBotRight = [obRow, obColumn]
        elif obRow < row and obColumn < column:
            if obRow > obBotLeft[0]:
                obBotLeft = [obRow, obColumn]
        elif obRow > row and obColumn < column:
            if obRow < obTopLeft[0]:
                obTopLeft = [obRow, obColumn]

moves = 0
moves += obTop[0]-row-1
moves += obRight[1]-column-1
moves += row-obBot[0]-1
moves += column-obLeft[1]-1
moves += min(obTopLeft[0]-row-1, column-obTopLeft[1]-1)
moves += min(obTopRight[0]-row-1, obTopRight[1]-column-1)
moves += min(obBotRight[1]-column-1, row-obBotRight[0]-1)
moves += min(row-obBotLeft[0]-1, column-obBotLeft[1]-1)

print(moves)
