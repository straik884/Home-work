#Вводим слово.
word = input()
#С помощью функции .count посчитаем повтор буквы в слове или строке.
a = word.count('a')
e = word.count('e')
i = word.count('i')
o = word.count('o')
u = word.count('u')
#Суммируем гласные буквы.
sum = (a + e + i + o + u)
#С помощью if создаём условие для каждой буквы.
if a == 0:
    print('False:a')
else:
    print('a=', a)
if e == 0:
    print('False:e')
else:
    print('e=', e)
if i == 0:
    print('False:i')
else:
    print('i=', i)
if o == 0:
    print('False:o')
else:
    print('o=', o)
if u == 0:
    print('False:u')
else:
    print('u=', a)


print('Сумма гласных', sum)
#С помощью функции .len посчитаем количество элиментов в списке,
# вычтем сумму гласных из этого списка, так мы получим сумму согласных.
print('Сумма гласных', len(word)-sum)



