def roundGrade(grade):
    if grade < 38:
        return grade
    nextFive = grade
    while nextFive%5:
        nextFive += 1
    if nextFive - grade < 3:
        return nextFive
    return grade


#================================================================
for _ in range(int(input())):
    grade = int(input())
    print(roundGrade(grade))