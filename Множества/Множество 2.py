tmp1 = int(input('Сколько добавляем в первый список: '))
tm1 = []
for i in range(tmp1):
    age = int(input())
    tm1.append(age)
unic1 = set(tm1)



tmp2 = int(input('Сколько добавляем во второй список: '))
tm2 = []
for i in range(tmp2):
    age = int(input())
    tm2.append(age)
unic2 = set(tm2)

print ('Длина первого списка', len(unic1))
print ('Длина второго списка', len(unic2))
print ('Элементы которые пересекаются в обоих множествах', (unic1 & unic2))

dlinna=  len(unic1)+len(unic2)
print ('Сумма длин обоих списков: ', dlinna)

