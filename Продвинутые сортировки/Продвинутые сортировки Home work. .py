#Рекурсия бинарных чисел
def bin_system(n):
    if n < 2:
        print(n, end='')
    else:
        bin_system(n//2)
        print(n % 2, end='')
bin_system(2)

print()
#рекурсия умножения
def mult(a, b):
   if a == 0:
      return 0
   elif a == 1:
      return b
   else:
      return b + mult(a-1, b)
print(mult(3,5))

print()

#рекурсия возведения в сетпень \
def stepen(n,t):
    if t == 1:
        return n
    if t != 1:
        return n * stepen(n, t-1)
print(stepen(3,2))