class cherepashka (object):
    x = 0
    y = 0
    s = 0

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y + self.s
        return self.y

    def go_down(self):
        self.y - self.s
        return self.y

    def go_left(self):
        self.x - self.s
        return self.x

    def go_right(self):
        self.y + self.s
        return self.y

    def evolve(self):
        self.s += 1
        return self.s

    def degrade(self):
        if self.s > 0:
            self.s -= 1
            return self.s
        else:
            return f'Ошибка s =0'



    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2

cha=cherepashka(15, 25, 30)
print(cha.go_up())
print(cha.go_down())
print(cha.go_left())
print(cha.go_right())
print(cha.evolve())
print(cha.degrade())
print(cha.count_moves(12,10))