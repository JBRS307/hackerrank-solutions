def countFib(t1, t2, n):
    if n == 3:
        return t1 + t2**2
    return countFib(t2, t1+t2**2, n-1)

#===================================================
t1, t2, n = list(map(int, input().strip().split()))

print(countFib(t1, t2, n))