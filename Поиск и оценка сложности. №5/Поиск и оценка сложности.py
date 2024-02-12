#Данная рекурсия вызывается рекурсивно n раз

#прежде чем доходит до базового числа,

#сложность ее будет О(n), такой код называют линейным


def fact_recursive(n):
    if n <= 1:
        return 1
    return n*fact_recursive(n-1)


#Работа сортировки Шеллы зависит от длин списков

# в которых будут находится сортируемые объекты исходного массива n емкостью на каждом шаге

#Его сложность составляет O(n^2)

import random
n = 6
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print('Not sirted')
print(arr)
print('------')


step = len(arr) // 2
while step > 0:
    for i in range(step, n,1):
        value = arr[i]
        current_index = i
        index_to_chack = current_index - step
        while current_index > 0 and arr[index_to_chack] > value:
            arr[current_index] = arr[index_to_chack]
            current_index -= step
            index_to_chack -= step
        arr[current_index] = value
    step = step // 2

print('Sorted')
print(arr)
print('yes')
