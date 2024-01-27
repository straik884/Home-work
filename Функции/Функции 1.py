def factorial(n):
    f = 1
    for fact in range(1, n + 1):
        f *= fact
    return f



n = int(input())
l = list(range(1, n+1))
l.reverse()
factorials = [factorial(x) for x in l]
print(factorials)




