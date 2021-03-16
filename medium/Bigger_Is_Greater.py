for _ in range(int(input())):
    string = input()
    string = list(string)
    #for i in range(len(string)):
        #string[i] = ord(string[i])
    change = 0
    for i in range(len(string)-1, 0, -1):
        if string[i] > string[i-1]:
            change = i-1
            break
    else:
        print('no answer')
        continue
    Min = string[change+1]
    changer = change+1
    for i in range(change+2, len(string)):
        if string[i] > string[change] and string[i] < Min:
            changer = i
            Min = string[i]
    string[change], string[changer] = string[changer], string[change]
    res = string[:change+1]
    res2 = sorted(string[change+1:])
    res += res2
    for char in res:
        print(char, end='')
    print()
    
