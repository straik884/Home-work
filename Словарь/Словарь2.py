a ={}
for x in range(10,-6,-1):
    a[x] = a.get(x,1*x**x)
print(a)