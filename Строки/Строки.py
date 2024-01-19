#Создаем функцию(строку)
def полиндром(string):
#Переворачиваем строку, читиая её с обратной стороны
    reversed_string = string[::-1]
#Сравнивем строку с перевернутой строкой
    return string == reversed_string

Проверка_слова = полиндром(input())
print('yes' if Проверка_слова else 'no')





