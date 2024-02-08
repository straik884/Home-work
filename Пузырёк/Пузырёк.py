import random
n = 5
arr = list()
swappend = True
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print('Not sorted:')
print(arr)
print('------')

for i in range(n):
    #проверка, быд ли произведён обмен элементов
    swapped = False
    for j in range(n-1):
        left = arr[j]
        right = arr[j+1]
        if left > right:
            arr[j] = right
            arr[j+1] = left
            # Обмена если не было во внутренем цилке то список отсортирован
        swapped = True

print('Sorted:')
print(arr)