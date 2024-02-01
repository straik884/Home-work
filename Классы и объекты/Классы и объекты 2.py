class Kassa (object):
    cash = 0

    def __init__(self, cash):
        self.cash = cash

    def top_up(self, maney):
        self.cash += maney
        return f' В кассе {self.cash}'


    def count_1000(self):
        qwe = self.cash // 1000
        return f'Целых тысяч осталось в кассе: {qwe}'

    def take_away(self, maney):
        if maney <= self.cash:
            self.cash -= maney
            return self.cash
        else:
            return f'Ошибка, в кассе только недостаточно денег'




kassa = Kassa(0)
kassa.top_up(int(input('На сколько хотите пополнить казну сир?')))
print('Пополнение на:',kassa.cash)
print(kassa.count_1000())
print('В казне осталось:', kassa.take_away(int(input('На сколько хотите разграбить казну?'))))