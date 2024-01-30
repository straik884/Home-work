import random

n = random.randint(0,10)
m = random.randint(0,10)
b = random.randint(0,10)
t = random.randint(0,10)



matrix1 = [[random.randint(-500,500) for j in range(n)] for i in range(m)]


matrix2 = [[random.randint(-500,500) for j in range(n)] for i in range(m)]

matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

for x in matrix1:
    print(x)

print()

for y in matrix2:
    print(y)

print()

for r in matrix3:
    print(r)

